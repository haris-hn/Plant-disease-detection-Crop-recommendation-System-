# 🌿 AgriSmart — Intelligent Farming Companion

> **Final Year Project** — Agriculture University Faisalabad  
> A smart AI-powered web application to help farmers detect plant diseases and get personalized crop recommendations.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Usage](#usage)
- [Models](#models)
- [Dataset](#dataset)
- [Authentication](#authentication)
- [Screenshots](#screenshots)
- [Contact](#contact)

---

## 🌱 Overview

**AgriSmart** is a Python-based web application built with **Streamlit** that leverages machine learning and deep learning to assist farmers with two core tasks:

1. **Plant Disease Detection** — Upload an image of a plant leaf and get an instant AI diagnosis across 38 disease classes.
2. **Crop Recommendation** — Enter soil parameters (N, P, K, temperature, humidity, pH, rainfall) and receive a personalized crop suggestion.

The app uses **Google OAuth 2.0** for secure authentication, ensuring only authenticated users can access the dashboard.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Google OAuth Login | Secure sign-in with Google accounts |
| 🌿 Plant Disease Detection | AI image classification across 38 plant/disease combinations |
| 🌾 Crop Recommendation | ML-based crop suggestion from soil and climate parameters |
| 🔍 Crop Database Search | Lookup growing information for any supported crop |
| 👤 User Profile | View Google account details within the app |
| 📱 Responsive Design | Glassmorphism UI with mobile-friendly layout |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | Streamlit, Custom CSS (Glassmorphism) |
| **Backend** | Python 3.x |
| **Deep Learning** | TensorFlow / Keras (CNN — `trained_model.keras`) |
| **Machine Learning** | Scikit-learn (Random Forest — `model.pkl`) |
| **Data Processing** | NumPy, Pandas, Pillow (PIL) |
| **Authentication** | Google OAuth 2.0 (`streamlit-oauth`) |
| **Fonts** | Google Fonts (Poppins, Montserrat, Playfair Display) |

---

## 📁 Project Structure

```
fyph/
│
├── main.py                          # Entry point — Login page with Google OAuth
│
├── pages/
│   └── home.py                      # Main dashboard (Disease, Crop, About, Contact, Profile tabs)
│
├── images/
│   ├── banner.png
│   ├── contact_banner.png
│   ├── email.png
│   ├── location.png
│   └── phone.png
│
├── model.pkl                        # Trained ML model for crop recommendation
├── standscaler.pkl                  # Standard Scaler for feature normalization
├── minmaxscaler.pkl                 # MinMax Scaler for feature normalization
├── crop_info.pkl                    # Crop details and growing information
│
├── trained_model.keras              # CNN model for plant disease detection
├── training_hist.json               # Model training history/metrics
│
├── punjab_crop_recommendation_dataset.csv   # Dataset used for crop model training
│
├── home_page.jpeg                   # Home tab hero image
├── background.jpg                   # App background image
│
└── README.md                        # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.9+**
- pip (Python package manager)
- A Google Cloud project with **OAuth 2.0** credentials configured

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fyph
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit streamlit-oauth tensorflow numpy pillow scikit-learn pandas requests
   ```

### Running the App

```bash
streamlit run main.py
```

The app will open at **http://localhost:8501** in your browser.

> ⚠️ Make sure the Google OAuth redirect URI is set to `http://localhost:8501/` in your Google Cloud Console.

---

## 🖥️ Usage

### 1. Login
- Open the app and click **"Continue with Google"**
- Sign in with your Google account
- You'll be redirected to the dashboard automatically

### 2. Disease Recognition (Tab 2)
- Navigate to the **Disease Recognition** tab
- Upload a clear image of a plant leaf (`.jpg`, `.jpeg`, `.png`)
- Click **"Analyze Image"** to get an AI diagnosis
- If a disease is detected, recommended actions are displayed

### 3. Crop Recommendation (Tab 3)
- Navigate to the **Crop Recommendation** tab
- Fill in your soil parameters:
  - **N** — Nitrogen level (0–150)
  - **P** — Phosphorus level (0–150)
  - **K** — Potassium level (0–150)
  - **Temperature** (°C)
  - **Humidity** (%)
  - **pH Level** (0–14)
  - **Rainfall** (mm)
- Click **"Get Recommendation"** to see the best crop for your conditions
- Search the crop database for growing tips

### 4. Profile (Tab 6)
- View your Google account information
- Click **"Logout"** to sign out securely

---

## 🤖 Models

### Plant Disease Detection
- **Architecture:** Convolutional Neural Network (CNN) built with TensorFlow/Keras
- **Input:** 128×128 RGB leaf images
- **Output:** 38 classes (plant + disease combinations)
- **File:** `trained_model.keras`

**Supported disease classes include:**
- Apple: Scab, Black Rot, Cedar Rust, Healthy
- Tomato: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Mosaic Virus, and more
- Corn, Grape, Potato, Peach, Pepper, Strawberry, and others (38 total classes)

### Crop Recommendation
- **Algorithm:** Random Forest Classifier (Scikit-learn)
- **Input Features:** N, P, K, Temperature, Humidity, pH, Rainfall
- **Output:** One of 10 recommended crops
- **File:** `model.pkl`

**Supported crops:** Wheat, Rice, Sugarcane, Cotton, Maize, Barley, Millet, Chickpea, Sunflower, Potato

**Preprocessing:**
- `minmaxscaler.pkl` — MinMax normalization applied first
- `standscaler.pkl` — Standard scaling applied after MinMax

---

## 📊 Dataset

- **File:** `punjab_crop_recommendation_dataset.csv`
- **Region:** Punjab, Pakistan
- **Features:** Soil nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall
- **Labels:** Crop type suitable for the given conditions

---

## 🔐 Authentication

The app uses **Google OAuth 2.0** via the `streamlit-oauth` library.

| Setting | Value |
|---|---|
| OAuth Provider | Google |
| Scope | `openid email profile` |
| Redirect URI | `http://localhost:8501/` |
| Token Validation | Google UserInfo API |

> ⚠️ **Security Note:** The `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in `main.py` should be moved to environment variables (`.env` file or Streamlit secrets) before deploying to production.

**Recommended for production:**
```toml
# .streamlit/secrets.toml
GOOGLE_CLIENT_ID = "your-client-id"
GOOGLE_CLIENT_SECRET = "your-client-secret"
```

---

## 📄 License

This project was developed as a **Final Year Project** at Agriculture University Faisalabad. All rights reserved.

---


