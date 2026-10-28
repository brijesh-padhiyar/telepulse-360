# SARDAR PATEL UNIVERSITY (SPU)
## DEPARTMENT OF COMPUTER SCIENCE & INFORMATION TECHNOLOGY
### BCA (4-YEAR HONOURS) PROGRAMME • SEMESTER 7 (OJT - 6 CREDITS)

---

# 📱 TELEPULSE 360°
## Pan-India Telecom Intelligence, ARPU Analytics & Silent Churn Prediction Platform
**An Enterprise Big Data Analytics Portal on 50,000+ Mobile Subscriber Transactions across Reliance Jio, Bharti Airtel, Vodafone Idea & BSNL**

---

### 📄 OFFICIAL PROJECT DOSSIER & PROGRESS REPORT
- **Candidate Name:** Brijesh Padhiyar
- **Degree:** Bachelor of Computer Applications (BCA 4-Year Honours)
- **Semester & Course:** Semester 7 • On-Job Training (OJT - 6.0 Credits)
- **Host Institution:** Sardar Patel University (SPU), Vallabh Vidyanagar, Gujarat
- **Host Organization:** Enterprise Data Analytics & IT Solutions Facility
- **Academic Year:** 2026 – 2027
- **Submission Deadline:** 24 November 2026 (SPU Circular Mandate)

---

## 📑 TABLE OF CONTENTS (SPU 10-SECTION FORMAT)
1. **Coverpage**
2. **Certificate of Authenticity & OJT Completion**
3. **Acknowledgement**
4. **Table of Contents**
5. **Introduction & Industry Background**
   - 5.1 Overview of Indian Telecommunications Landscape
   - 5.2 Four-Way Operator Dynamic (Jio, Airtel, Vi, BSNL)
   - 5.3 Problem Statement & Business Drivers
6. **Objectives of the On-Job Training**
   - 6.1 Academic & Credit Objectives (6.0 Credits / 180 Certified Hours)
   - 6.2 Technical Objectives (Python, Vectorized Computing, RFM-D Modeling)
7. **Learning Experience & Progressive Sprint Diary**
   - 7.1 Progressive Sprint Log (Day 1 to Day 10)
   - 7.2 Day 1 Milestone: Environment Setup, PyCharm Kernel & Data Schema Design
8. **Learning Outcomes & Architectural Deliverables**
9. **Conclusions & Executive Insights**
10. **Attachments & Technical Appendices**
    - 10.1 Environment Verification Output
    - 10.2 14-Column Master Data Schema Specifications

---

## 1. COVERPAGE & EXECUTIVE PROJECT CHARTER

### 📱 TELEPULSE 360°: Pan-India Telecom Intelligence, ARPU Analytics & Churn Platform
**Big Data Analytics on 50,000+ Transactions across Reliance Jio, Bharti Airtel, Vodafone Idea & BSNL across 22 Indian Circles**

#### ⚠️ 1.1 The Core Problem Statement (Telecom Industry Crisis)
India's 1.15-billion wireless market is locked in a fierce four-way battle with three critical business blindspots:
1. **The ARPU Divide:** Bharti Airtel commands premium ARPU (~₹214/month) driven by affluent postpaid users, while Reliance Jio (~₹185/month) relies on massive volume. Vi (~₹150) and BSNL (~₹95) struggle with revenue stagnation and capital expenditure deficits.
2. **Silent Churn Decay:** Millions of prepaid subscribers do not port out via MNP; instead, they "silently churn" by delaying pack renewals past their 28-day or 84-day validity window (>7 days lag), causing silent revenue decay.
3. **Evening Payment Latency Spikes:** Over 90% of recharges happen via UPI (PhonePe, GPay, Paytm) where peak evening traffic (8 PM – 11 PM) triggers 2.5%–4.0% gateway timeouts, resulting in lost recharge conversions and user frustration.

#### 🎯 1.2 Project Purpose & Strategic Mission (Why We Are Building This)
The purpose of **TELEPULSE 360°** is to engineer a unified, interactive intelligence platform that delivers dual-value:
- **For Telecom Leadership (C-Suite):** Empower executives with real-time ARPU tracking, early silent-churn warning indicators, payment gateway drop-off diagnostics, and 4D subscriber segmentation.
- **For Mobile Consumers:** Provide an algorithmic Smart Plan Recommender that analyzes daily cellular appetite to recommend the most cost-effective annual subscription pack.
- **For Academic Excellence:** Demonstrate industry-ready software engineering by building an enterprise-scale, zero-SQL, pure-Python modern data application adhering to SPU BCA Semester 7 OJT standards.

#### 🛠️ 1.3 What We Will Do in the Project (5-Stage Implementation)
1. **Stage 1 (Data Synthesis Engine):** Synthesize 50,000+ realistic transaction records across 21 tariff packs, 18,000 subscribers, and 22 circles calibrated against actual TRAI market shares (Jio 44%, Airtel 33%, Vi 19%, BSNL 4%).
2. **Stage 2 (Pure-Python Zero-SQL ETL):** Build an automated Pandas data pipeline for type-casting, null imputation, timestamp parsing, and memory optimization without external databases.
3. **Stage 3 (Business KPI Mathematics):** Formulate vectorized algorithms for ARPU benchmarking, Gross Transaction Value (GMV), silent renewal lag days, and gateway failure funnels.
4. **Stage 4 (Machine Learning 4D RFM-D):** Develop an enhanced K-Means clustering algorithm incorporating Daily Data Appetite (D) alongside traditional Recency, Frequency, and Monetary scores.
5. **Stage 5 (C-Suite Streamlit Portal):** Deploy an interactive multi-page web application featuring choropleth geospatial maps, 3D cluster visualizers, and a "What-If" Tariff Hike sensitivity simulator.

#### 👤 1.4 Trainee & Institutional Profile
- **Candidate Name:** Brijesh Padhiyar
- **SPU Enrollment No:** SPU-BCA-2026-XXXX
- **Degree Programme:** BCA (4-Year Honours) • Semester 7 (6.0 Credits)
- **Host Institution:** Sardar Patel University (SPU), Vallabh Vidyanagar, Gujarat
- **Host Organization:** Enterprise Data Analytics & IT Solutions Facility
- **Certified Hours:** Strictly 180 Verified Practical Hours
- **Mandatory Submission Deadline:** 24 November 2026 (SPU Circular)

---


## 2. CERTIFICATE OF OJT COMPLETION
This is to certify that **Brijesh Padhiyar** (Enrollment No: SPU-BCA-2026-XXXX), student of **BCA Semester 7**, has satisfactorily undertaken and completed the compulsory On-Job Training (OJT) carrying **6.0 Credits (180 Certified Hours)** under the guidance of industry mentors and faculty coordinators.

The candidate has actively designed and developed the capstone data analytics portal titled **"TELEPULSE 360°: Pan-India Telecom Intelligence & ARPU Analytics Platform"** adhering strictly to Sardar Patel University regulations.

- **Student Signature:** `_________________________`
- **Industry Mentor (Seal & Sign):** `_________________________`
- **SPU Faculty Coordinator / HOD:** `_________________________`

---

## 3. ACKNOWLEDGEMENT
I express my deepest gratitude to the **Department of Computer Science & IT, Sardar Patel University (SPU)** for structuring the 4-Year BCA curriculum with an industry-immersive On-Job Training component.

I extend special thanks to my **Industry Mentor** and **Faculty Coordinator** for their invaluable guidance in shaping the system architecture, mathematical benchmarking (TRAI standards), and exploratory data analytics methodologies employed in TELEPULSE 360°.

---

## 5. INTRODUCTION & INDUSTRY BACKGROUND

### 5.1 Indian Telecommunications Dynamic
The Indian mobile communications market represents one of the world's most hyper-competitive digital ecosystems, serving over 1.15 billion active wireless subscribers. The market operates under a four-player structure:
1. **Reliance Jio (44% Volume Leader):** Revolutionized digital connectivity via nationwide 4G/5G standalone networks and budget data bundles.
2. **Bharti Airtel (33% ARPU Leader):** Commands industry-leading Average Revenue Per User (~₹214/month) driven by premium postpaid and quality urban subscribers.
3. **Vodafone Idea (19% Value Focus):** Focusing on subscriber retention and network upgrades across high-density metro corridors.
4. **BSNL (4% Public Service Provider):** Providing critical telecommunications connectivity across remote, rural, and strategically vital borders.

### 5.2 Problem Statement
Telecommunications operators face three critical data challenges:
1. **Silent Churn Risk:** Subscribers who delay their recharge past their validity window without formally porting out.
2. **Payment Gateway Latency & Drop-offs:** High-volume evening recharge failures across UPI (PhonePe, Google Pay, Paytm) vs Cards.
3. **Multi-Dimensional Subscriber Segmentation:** Traditional RFM models ignore cellular data appetite. An enhanced 4D RFM-D model (Recency, Frequency, Monetary + Daily Data Appetite) is required.

---

## 6. OBJECTIVES OF THE ON-JOB TRAINING
1. **Fulfill SPU Degree Mandates:** Achieve 6.0 certified academic credits through 180 verified hours of professional data analytics.
2. **Pure-Python Data Architecture:** Engineer a zero-SQL in-memory analytics pipeline using Pandas, NumPy, Scikit-Learn, and Plotly.
3. **National Scope:** Model and analyze 50,000+ realistic subscriber transactions across all 22 TRAI Telecom Circles.

---

## 7. LEARNING EXPERIENCE & PROGRESSIVE SPRINT LOG

### 7.1 Day 1: Project Genesis, PyCharm Kernel Setup & Master Schema Formulation
- **Date:** 28 October 2026
- **Module:** Architecture Initialization & Environment Verification
- **Hours Certified:** 6.0 Hours (2.0h Conceptual Mastery + 4.0h Hands-on Implementation)

#### Verified Implementation Progress:
1. **Environment Setup:** Configured PyCharm Professional with standard Python 3.14.5 runtime, Jupyter kernel (`ipykernel 7.4.0`), Pandas 3.1.0, and NumPy 2.5.4.
2. **Executed Cell 1 Output in `analysis.ipynb`:**
```text
============================================================
🚀 TELEPULSE 360° : ENVIRONMENT & LIBRARIES LOADED
============================================================
🐍 Python Version : 3.14.5
📦 Pandas Version : 3.1.0
📦 NumPy Version  : 2.5.4
📂 Workspace Root : E:\Venom\telepulse-360
============================================================
```
3. **14-Column Master Data Schema Formulation:** Formalized `data/data_schema.json` capturing transaction IDs, customer loyalty identifiers, operators, 22 circles, validity durations, data usage telemetry, payment gateways, and network generations.
4. **Executed Cell 2 Output in `analysis.ipynb` (Schema Inspection):**
```text
=================================================================
📊 PROJECT       : TELEPULSE 360°
🎯 DOMAIN        : Pan-India Telecom Intelligence & ARPU Analytics
📈 TARGET SCALE  : 50,000 Transactions
🔢 TOTAL COLUMNS : 14 Columns
=================================================================
```

#### 📋 Formal 14-Column Enterprise Data Dictionary:
| # | Column Name | Technical Data Type | Telecom Domain Description & Purpose |
| :-: | :--- | :--- | :--- |
| **1** | `transaction_id` | String (Alpha-Numeric) | Unique 12-char identifier (`TXN202610260001`) for payment reconciliation |
| **2** | `customer_id` | String (Unique ID) | Unique subscriber ID (`CUST_004812`) to track lifetime recharge cycles & churn |
| **3** | `transaction_date`| DateTime (ISO 8601) | Full timestamp of recharge (date, hour, peak evening minutes) |
| **4** | `operator` | Categorical | Service provider name (Reliance Jio, Bharti Airtel, Vodafone Idea, BSNL) |
| **5** | `circle` | Categorical | 22 TRAI Licensed Service Areas (Gujarat, Mumbai, Delhi, Karnataka, etc.) |
| **6** | `plan_type` | Categorical | Plan tier: Daily Data (1.5GB/2GB/3GB), Annual (365d), 5G Booster, Top-Up |
| **7** | `amount_inr` | Float64 (Numeric) | Gross Transaction Value (GMV) in Indian Rupees (₹19 to ₹3,599) |
| **8** | `validity_days` | Integer (Discrete) | Validity period of the purchased telecom pack (28, 56, 84, 336, 365 days) |
| **9** | `data_allowance_gb`| Float64 (Numeric) | Total cellular high-speed data quota bundled in the plan (GB) |
| **10**| `daily_avg_usage_gb`| Float64 (Numeric) | Actual daily subscriber data usage telemetry (0.1 GB to 8.5 GB/day) |
| **11**| `payment_gateway` | Categorical | Payment instrument: UPI (PhonePe, GPay, Paytm), Cards, NetBanking |
| **12**| `payment_status` | Categorical | Settlement status: Success, Gateway Timeout, Bank Decline, User Abandoned |
| **13**| `latency_ms` | Integer (Time) | Round-trip payment network latency in milliseconds (120ms to 9,500ms) |
| **14**| `network_generation`| Categorical | Primary handset connection: 4G LTE, 5G Standalone, 5G Non-Standalone, 3G/2G |

5. **TRAI Market Calibration & Volume Allocation (Step 3):**
   - Established realistic Indian telecommunications market distributions calibrated against TRAI standards.
   - Formulated the statistical allocation matrix for the 50,000 synthetic records to be generated on Day 2:

#### 🌐 TRAI Telecom Market Share & ARPU Calibration Matrix:
| Telecom Operator | Real Market Share (%) | Benchmark ARPU (INR) | Allocated 50,000 Sample | Est. Sample Monthly GMV |
| :--- | :---: | :---: | :---: | :---: |
| **Reliance Jio** | 44% | Rs. 185.00 | 22,000 rows | Rs. 40.7 Lakhs |
| **Bharti Airtel** | 33% | Rs. 214.00 | 16,500 rows | Rs. 35.3 Lakhs |
| **Vodafone Idea (Vi)** | 19% | Rs. 150.00 | 9,500 rows | Rs. 14.2 Lakhs |
| **BSNL** | 4% | Rs. 95.00 | 2,000 rows | Rs. 1.9 Lakhs |
| **TOTAL SCALE** | **100%** | **Weighted: Rs. 184.3** | **50,000 Records** | **Rs. 92.1 Lakhs** |

6. **22 Indian Telecom Circles Framework:**
   - Categorized all 22 Licensed Service Areas into Metro, Circle A, Circle B, and Circle C corridors to capture regional recharge volume velocity and network transitions.

#### ✅ Day 1 Milestone Status: 100% COMPLETED
- Environment verified (`Python 3.14.5`, `Pandas 3.1.0`, `NumPy 2.5.4`).
- Master 14-Column Data Schema locked in `data/data_schema.json`.
- TRAI Market parameters & ARPU benchmarks registered in `analysis.ipynb`.
- Repository synced & pushed to GitHub (`main` branch).
### 7.2 Day 2 Milestone: 50,000+ Synthetic Telecom Data Generation Engine
- **Date:** 29 October 2026
- **Module:** Probabilistic Data Synthesis & Payment Gateway Simulation
- **Hours Certified:** 6.0 Hours (2.0h Modeling Theory + 4.0h Synthesis Pipeline)

#### Verified Implementation Progress:
1. **Operator-Specific Tariff Pack Catalog:**
   - Established 21 distinct tariff tiers reflecting true telecom product packaging across Jio, Airtel, Vi, and BSNL (from ₹19/₹61 boosters to ₹3359 annual packs).
   - Modeled Airtel's premium pricing (₹265 / 1.5GB/day) vs Jio's aggressive pricing (₹239 / 1.5GB/day) to accurately induce real-world ARPU bifurcation.

2. **Payment Gateway Reliability & NPCI Benchmarking:**
   - Integrated realistic digital payment instrument usage shares and baseline latency distributions:
     - **PhonePe (UPI):** 46% share, 2.5% failure rate, mean latency ~780ms.
     - **Google Pay (UPI):** 35% share, 2.8% failure rate, mean latency ~820ms.
     - **Paytm (UPI):** 11% share, 3.8% failure rate, mean latency ~950ms.
     - **Credit/Debit Cards:** 5% share, 6.2% failure rate, mean latency ~1950ms.
     - **Net Banking:** 3% share, 7.5% failure rate, mean latency ~3200ms.

3. **Executed Cell 4 Output in `analysis.ipynb`:**
```text
======================================================================
📦 OPERATORS CONFIGURED      : 4 (Jio, Airtel, Vi, BSNL)
📋 TOTAL TARIFF PACKS        : 21 Distinct Plans
💳 PAYMENT MODES REGISTERED  : 5 Instruments (UPI, Cards, NetBanking)
======================================================================
```

4. **Executed Cell 5 Output in `analysis.ipynb` (50,000 Records Synthesized):**
```text
🚀 Initializing TELEPULSE 360° Data Synthesis Engine (50,000 records)...
✅ Generated 50,000 transactions (7.49 MB)
📁 Output Saved: data/raw/telecom_transactions.csv
=================================================================
📊 DATASET SHAPE : 50,000 Rows × 14 Columns
=================================================================

🏢 OPERATOR MARKET SHARE VERIFICATION (TRAI Target vs Actual):
operator
Reliance Jio     44.08%   (TRAI Benchmark: 44.0%)
Bharti Airtel    33.13%   (TRAI Benchmark: 33.0%)
Vodafone Idea    18.82%   (TRAI Benchmark: 19.0%)
BSNL              3.97%   (TRAI Benchmark:  4.0%)

💳 PAYMENT STATUS DISTRIBUTION:
payment_status
Success            95.71%
Gateway Timeout     1.49%
User Abandoned      1.46%
Bank Decline        1.34%

📶 NETWORK GENERATION DISTRIBUTION:
network_generation
4G LTE               52.02%
5G Standalone        25.73%   (Jio 5G SA Dominance)
5G Non-Standalone    17.19%   (Airtel 5G NSA Deployment)
3G/2G Legacy          5.06%   (BSNL & Legacy Feature Phones)
```

#### ✅ Day 2 Milestone Status: 100% COMPLETED
- 50,000 complete transactions synthesized with 18,000 subscriber pool.
- Full 14-column enterprise schema populated with zero nulls.
- Raw transactional baseline exported to `data/raw/telecom_transactions.csv`.
- Official SPU Project Report Dossier compiled to PDF & HTML formats.
- **Next Milestone:** Day 3 — Pure Pandas ETL Pipeline, Cleaning & Column Optimization (`src/data_pipeline.py`).

---

*(Report dossier will be progressively extended after each verified milestone)*


