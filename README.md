# Titanic Dataset Analysis and Dashboard

## Overview

This project automates downloading, cleaning, and analyzing the Titanic dataset using Python. It features a Streamlit dashboard for interactive data exploration and a simple Machine Learning model to predict passenger survival.

---

## Features

- **Automated dataset download** from Kaggle using the Kaggle API  
- **Data cleaning and preprocessing** including filling missing values and standardizing columns  
- **Interactive Streamlit dashboard** with plots showing survival distribution, passenger class impact, and age distribution  
- **Machine Learning model (Random Forest)** trained to predict survival, showing model accuracy and sample predictions  
- **Footer with clickable LinkedIn and GitHub links**

---

## Setup and Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd titanic-project
Install dependencies

Make sure you have Python 3.7+ installed.

bash
Copiar
Editar
pip install -r requirements.txt
If you don't have a requirements.txt, install manually:

bash
Copiar
Editar
pip install pandas streamlit seaborn matplotlib scikit-learn kaggle
Set up Kaggle API credentials

Go to Kaggle Account

Scroll to API section and click Create New API Token

Place the downloaded kaggle.json file in:

makefile
Copiar
Editar
C:\Users\<your-username>\.kaggle\kaggle.json
Or set environment variable KAGGLE_CONFIG_DIR to the folder where kaggle.json is located.

Running the Project
Download and clean the dataset

Run your main script (e.g. main.py) which downloads and cleans the Titanic dataset:

bash
Copiar
Editar
python main.py
Launch the Streamlit dashboard

bash
Copiar
Editar
streamlit run titanic_dashboard.py
The dashboard will open in your browser at http://localhost:8501.

Project Structure
downloadTitanicCsv.py — Script to download Titanic dataset from Kaggle

dataCleasing.py — Script for cleaning and preprocessing the dataset

main.py — Main orchestrator script to download and clean data

titanic_dashboard.py — Streamlit dashboard with visualizations and ML model

Titanic-Dataset.csv — Raw dataset (downloaded)

Titanic-Dataset-Cleaned.csv — Cleaned dataset (generated)

Notes
The ML model is a Random Forest trained on cleaned data, optimized to run quickly using caching in Streamlit.

Modify the code to add more interactivity or improve ML models as needed.

Author
Lucas G. Romão

LinkedIn: https://www.linkedin.com/in/lucasg-romao/

GitHub: https://github.com/lucasromaodev