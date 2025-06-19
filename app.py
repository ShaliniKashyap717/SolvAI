import streamlit as st
import numpy as np
import joblib

#loading model
model = joblib.load("logS.pkl")

# setting up page config
st.set_page_config(
    page_title="SolvAI 🌊 | Molecular Solubility Predictor",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="auto"
)

# Header
st.markdown(
    """
    <style>
        .main {background-color: #fdf6f0;}
        h1 {
            font-family: 'Trebuchet MS', sans-serif;
            color: #3b3b3b;
        }
        .stButton button {
            background-color: #00aaff;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧪 SolvAI – Predict Molecular Solubility")
st.markdown(
    "Enter molecular descriptors below and get instant predictions for **aqueous solubility (logS)**. Great for chemistry researchers, biotech folks, and data-driven drug discovery! 🚀"
)

# Input fields
col1, col2 = st.columns(2)

with col1:
    mol_logp = st.number_input("💧 Hydrophobicity", value=1.0, step=0.1)
    mol_wt = st.number_input("⚖️ Molecular Weight", value=200.0, step=1.0)

with col2:
    num_rot_bonds = st.number_input("🔁 Number of Rotatable Bonds", value=3, step=1)
    aromatic_prop = st.slider("🧬 Aromatic Proportion", 0.0, 1.0, 0.3, step=0.01)

# Prediction
if st.button("🧠 Predict Solubility (logS)"):
    features = np.array([[mol_logp, mol_wt, num_rot_bonds, aromatic_prop]])
    prediction = model.predict(features)[0]
    
    st.markdown(f"""
    ### 🧾 Predicted logS: `{prediction:.4f}`  
    > Lower values indicate lower solubility in water.  
    """)
    
    if prediction > -2:
        st.success("🌊 High solubility – This molecule is water-friendly!")
    elif -4 <= prediction <= -2:
        st.warning("💧 Moderate solubility – Not too bad, not too great.")
    else:
        st.error("🧱 Poor solubility – Consider modifying the structure.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit & Logistic Regression| Solubility Predictor")
