# 📱 TELEPULSE 360°: Pan-India Telecom Intelligence & ARPU Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75.svg)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Big Data Analytics on Mobile Recharges, Subscription Cycles, Payment Gateway Latency & Customer Lifetime Value (RFM-D) Prediction.**  
> *Scale: **50,000+ Real-World Transaction Records** across Reliance Jio, Bharti Airtel, Vodafone Idea (Vi), and BSNL across 22 Indian Telecom Circles.*

---

## 🌟 Executive Summary
**TELEPULSE 360°** is an enterprise-grade full-stack data analytics and intelligence web application designed for both Telecom C-Suite Executives and Consumers. It analyzes over **50,000+ transaction records** to benchmark national Average Revenue Per User (ARPU), identify silent customer churn risks, diagnose payment gateway drop-offs (UPI vs Cards), and cluster subscribers using an advanced **4D RFM-D model (Recency, Frequency, Monetary + Daily Data Appetite)**.

---

## 🏛️ Project Architecture

```
telepulse-360/
│
├── .streamlit/
│   └── config.toml                  # Premium dark theme styling
├── assets/
│   └── style.css                    # Glassmorphism cards & typography
├── data/
│   ├── raw/                         # 50k transaction records CSV
│   └── processed/                   # Optimized Parquet data
├── src/
│   ├── data_pipeline.py             # High-speed Pandas ETL pipeline & caching
│   ├── rfm_model.py                 # RFM-D Math & Scikit-Learn clustering
│   └── metrics_calculator.py        # ARPU, GMV, Churn % & Latency algorithms
├── pages/
│   ├── 1_📈_Executive_Overview.py   # ARPU Benchmarking (Jio vs Airtel vs Vi vs BSNL)
│   ├── 2_🗺️_Circle_Geospatial.py   # Pan-India 22 Telecom Circles Revenue Heatmap
│   ├── 3_👥_Customer_Segmentation.py# 3D RFM Cluster Space & Target Lead Exporter
│   └── 4_🎯_Smart_Simulator.py      # Plan Recommender & Tariff Hike Simulator
├── scripts/
│   └── data_generator.py            # 50,000+ realistic transaction engine
├── app.py                           # Main application entry point & C-Suite dashboard
├── requirements.txt                 # Project dependencies
└── README.md                        # Documentation
```

---

## 🔬 Core Research Dimensions & Features

1. **ARPU & Tariff War Benchmarking:** Head-to-head performance metrics between **Bharti Airtel** (ARPU leader: ₹214), **Reliance Jio** (Volume leader: 44%), **Vodafone Idea (Vi)**, and **BSNL**.
2. **Recharge Cycle Decay & Silent Churn:** Calculating renewal intervals using shift window functions to isolate subscribers who delay renewal past their grace period (>7 days).
3. **Payment Gateway Latency & Drop-off Funnel:** Monitoring UPI (PhonePe, Google Pay, Paytm) vs Debit Cards vs NetBanking with peak evening hour (8:00 PM – 11:00 PM) timeout spikes.
4. **Telecom RFM-D 3D Clustering:** Mathematical scoring incorporating Daily Data Appetite ($D$) alongside traditional RFM. Unsupervised K-Means clustering isolating:
   - *Champions (High Value)*
   - *5G Data Addicts*
   - *Budget / Voice-First*
   - *At-Risk / Inactive Sleepers*
5. **Interactive Smart Plan Recommender:** Custom slider widget helping consumers find the most cost-effective annual plan based on daily data consumption.
6. **Tariff Hike "What-If" Sensitivity Simulator:** Dynamic financial projection modeling net GMV gain vs subscriber churn loss during 10%–25% tariff revisions.

---

## 🚀 Quickstart & Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/brijesh-padhiyar/telepulse-360.git
cd telepulse-360
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate 50,000+ Sample Data (If not present)
```bash
python scripts/data_generator.py
```

### 4. Launch the Web Application
```bash
streamlit run app.py
```
*The app will automatically launch at `http://localhost:8501` in your browser.*

---

## 🎓 Academic Credentials
- **Student Trainee:** Brijesh Padhiyar
- **Program:** BCA (4-Year Honours) &bull; Semester 7 (6.0 Credits)
- **University:** Sardar Patel University (SPU)
- **Documentation:** SPU 10-Section Official OJT Dossier + Verified 180-Hour Daily Logbook

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
