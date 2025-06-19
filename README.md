# 🧪 SolvAI – Predict Molecular Solubility Classification

Welcome to **SolvAI**, a stylish Streamlit-powered app that predicts whether a molecule is **soluble or not** in water using molecular descriptors. Ideal for **chemistry researchers**, **biotech innovators**, and **drug discovery enthusiasts**! 🚀

---

## 💡 What is SolvAI?

SolvAI classifies molecules based on their **aqueous solubility (logS)** using a machine learning model trained on curated chemical descriptors. It’s a fast, intuitive tool to support solubility screening and compound design decisions.

---

## 🔬 Input Descriptors

Provide the following molecular properties:

- 💧 **MolLogP** – Hydrophobicity (octanol/water partition coefficient)
- ⚖️ **MolWt** – Molecular Weight
- 🔁 **NumRotatableBonds** – Number of rotatable single bonds in the molecule (more rotatable bonds imply higher flexibility and lower crystallinity)
- 🌿 **AromaticProportion** – Ratio of aromatic atoms to total heavy atoms

---

## 🎯 Prediction Target

- **Solubility Class** – Whether the molecule is predicted to be **soluble** or **insoluble**

---

## 🧠 Model Used

- 📈 **Logistic Regression Classifier** (from `scikit-learn`)
- 📊 Chosen for its **better accuracy** and interpretability over Random Forest in this dataset

---

## 🚀 Live Demo

Try the app 👉 [SolvAI Web App](https://solvai.streamlit.app/)

---

## 🛠️ Tech Stack

- `Python`, `scikit-learn`, `Streamlit`
- Deployed via `Streamlit Cloud`

---



## 🤝 Contribute

Have ideas to improve SolvAI? Pull requests and feature suggestions are always welcome! 🧠

---

## 📌 License

MIT License © Shalini Kashyap
