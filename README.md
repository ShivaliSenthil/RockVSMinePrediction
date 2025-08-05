# 💣 Rock vs Mine Prediction App

This is a **Streamlit web app** that predicts whether a sonar signal represents a **Rock (🪨)** or a **Mine (💣)** object, based on 60 frequency-based sonar readings. It uses a trained machine learning model (`model4.pkl`) to make real-time predictions.

---

## 🔗 Live Demo

👉 [Click here to try the app](https://shivali-rock-vs-mine-prediction.streamlit.app/)

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Model](#model)
- [How to Run Locally](#how-to-run-locally)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## 🧭 Overview

This app uses the [UCI Sonar Dataset](https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+(Sonar,+Mines+vs.+Rocks)) which contains:

- **208 samples**
- **60 features** per sample (sonar energy levels at different frequency bands)
- **Binary classification target**:  
  - **`R`** for Rock  
  - **`M`** for Mine

Users input the 60 sonar frequency values, and the app instantly predicts whether it's a Rock or Mine using a trained ML model.

---

## 📊 Dataset

- **Source**: UCI Machine Learning Repository  
- **Name**: Sonar, Mines vs. Rocks  
- **Link**: [Sonar Dataset on UCI](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks))
- **Features**: 60 continuous-valued attributes  
- **Target**: `R` (Rock), `M` (Mine)

---

