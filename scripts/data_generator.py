# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Big Data Generator Engine
Generates 50,000+ Realistic Pan-India Telecom Recharge Transaction Records
Multi-Operator: Reliance Jio, Bharti Airtel, Vodafone Idea (Vi), BSNL across 22 Circles.
"""

import os
import csv
import random
import datetime

# Output directory
output_dir = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
os.makedirs(output_dir, exist_ok=True)

# 22 Indian Telecom Circles with relative population/market weight
CIRCLES = [
    ("Maharashtra & Goa", 0.11), ("Gujarat", 0.09), ("Delhi-NCR", 0.08),
    ("Mumbai", 0.07), ("UP East", 0.09), ("UP West", 0.06),
    ("Bihar & Jharkhand", 0.08), ("Karnataka", 0.07), ("Tamil Nadu", 0.07),
    ("Andhra Pradesh & Telangana", 0.07), ("Kolkata", 0.04), ("West Bengal", 0.04),
    ("Rajasthan", 0.05), ("Punjab", 0.04), ("Madhya Pradesh & CG", 0.06),
    ("Kerala", 0.05), ("Haryana", 0.03), ("Odisha", 0.03),
    ("Assam", 0.02), ("North East", 0.01), ("Himachal Pradesh", 0.01), ("J&K", 0.01)
]

OPERATORS = ["Reliance Jio", "Bharti Airtel", "Vodafone Idea", "BSNL"]
OPERATOR_WEIGHTS = [0.44, 0.34, 0.14, 0.08]

PLANS = [
    # (Plan ID, Plan Name, Price INR, Validity Days, Daily Data GB, OTT Benefit, Category)
    ("P19", "Data Booster 1GB", 19, 1, 1.0, "None", "Booster"),
    ("P29", "Data Booster 2GB", 29, 1, 2.0, "None", "Booster"),
    ("P65", "Data Booster 4GB", 65, 1, 4.0, "None", "Booster"),
    ("P155", "Basic Voice & 1GB", 155, 24, 0.04, "None", "Voice"),
    ("P209", "Daily 1GB Unlimited", 209, 22, 1.0, "None", "Standard"),
    ("P239", "Daily 1.5GB True 5G", 239, 28, 1.5, "5G Unlimited", "Standard"),
    ("P299", "Daily 2.0GB Unlimited", 299, 28, 2.0, "Hotstar Mobile", "Entertainment"),
    ("P399", "Daily 3.0GB Power Pack", 399, 28, 3.0, "Hotstar + SonyLIV", "Entertainment"),
    ("P479", "Mid-Term 1.5GB Daily", 479, 56, 1.5, "None", "Value"),
    ("P539", "Mid-Term 2.0GB Daily", 539, 56, 2.0, "5G Unlimited", "Value"),
    ("P666", "Quarterly 1.5GB Daily", 666, 84, 1.5, "None", "LongTerm"),
    ("P719", "Quarterly 2.0GB Daily", 719, 84, 2.0, "5G Unlimited", "LongTerm"),
    ("P839", "Quarterly 2.0GB + OTT", 839, 84, 2.0, "Disney+ Hotstar", "Entertainment"),
    ("P107", "BSNL Grace Extension", 107, 35, 0.1, "None", "Validity"),
    ("P197", "BSNL Long Validity", 197, 70, 2.0, "Zing Music", "Validity"),
    ("P2999", "Annual Mega Unlimited", 2999, 365, 2.5, "Hotstar + Prime Mobile", "Annual")
]

PAYMENT_MODES = ["UPI (PhonePe)", "UPI (Google Pay)", "UPI (Paytm)", "Credit/Debit Card", "NetBanking", "Paytm Wallet", "Amazon Pay"]
PAYMENT_WEIGHTS = [0.35, 0.28, 0.14, 0.10, 0.05, 0.05, 0.03]

GATEWAYS = ["Razorpay", "BillDesk", "Paytm Switch", "PhonePe Gateway"]

def generate_telecom_data(num_records=52000):
    print(f"Generating {num_records} realistic Indian Telecom transactions...")
    
    start_date = datetime.datetime(2026, 1, 1)
    end_date = datetime.datetime(2026, 11, 24)
    time_span = int((end_date - start_date).total_seconds())

    # Pre-generate 12,000 unique customers
    num_customers = 12000
    customers = []
    for i in range(1, num_customers + 1):
        cust_id = f"CUST_{i:06d}"
        op = random.choices(OPERATORS, weights=OPERATOR_WEIGHTS)[0]
        circle = random.choices([c[0] for c in CIRCLES], weights=[c[1] for c in CIRCLES])[0]
        handset = random.choices(["5G Smartphone", "4G Smartphone", "Feature Phone"], weights=[0.55, 0.38, 0.07])[0]
        customers.append((cust_id, op, circle, handset))

    # Transactions CSV path
    trans_csv = os.path.join(output_dir, "telecom_transactions.csv")
    
    with open(trans_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "transaction_id", "customer_id", "operator", "circle", "handset_type",
            "plan_id", "plan_name", "price_inr", "validity_days", "daily_data_gb",
            "ott_benefit", "plan_category", "payment_mode", "gateway",
            "recharge_timestamp", "status", "latency_ms", "discount_inr", "net_amount"
        ])

        for i in range(1, num_records + 1):
            tx_id = f"TXN_{2026}_{i:07d}"
            cust = random.choice(customers)
            cust_id, op, circle, handset = cust
            
            # Select plan based on operator characteristics
            if op == "BSNL":
                plan = random.choice([p for p in PLANS if "BSNL" in p[1] or p[2] < 300])
            elif handset == "5G Smartphone" and op in ["Reliance Jio", "Bharti Airtel"]:
                plan = random.choices(PLANS, weights=[0.1, 0.1, 0.05, 0.02, 0.05, 0.22, 0.15, 0.08, 0.05, 0.05, 0.06, 0.04, 0.02, 0.0, 0.0, 0.01])[0]
            else:
                plan = random.choice(PLANS)

            plan_id, plan_name, price, validity, daily_data, ott, cat = plan
            
            pmode = random.choices(PAYMENT_MODES, weights=PAYMENT_WEIGHTS)[0]
            gateway = random.choice(GATEWAYS)
            
            # Timestamp generation (with realistic peak hour weights: 8 PM - 11 PM)
            rand_seconds = random.randint(0, time_span)
            tx_time = start_date + datetime.timedelta(seconds=rand_seconds)
            if random.random() < 0.40:  # Bias 40% towards evening hours
                tx_time = tx_time.replace(hour=random.choice([19, 20, 21, 22]))

            # Failure rate logic: Peak evening hours have higher timeouts
            is_peak = (tx_time.hour in [20, 21, 22])
            if "UPI" in pmode:
                fail_prob = 0.06 if is_peak else 0.025
                latency = random.randint(300, 1800) if not is_peak else random.randint(1200, 4800)
            elif "Card" in pmode:
                fail_prob = 0.08 if is_peak else 0.04
                latency = random.randint(800, 2500)
            else:
                fail_prob = 0.04
                latency = random.randint(400, 1600)

            status = "FAILED" if random.random() < fail_prob else "SUCCESS"
            
            # Discount logic
            discount = random.choice([0, 0, 0, 10, 15, 20]) if "UPI" in pmode and price >= 239 else 0
            net_amount = max(price - discount, 0) if status == "SUCCESS" else 0

            writer.writerow([
                tx_id, cust_id, op, circle, handset,
                plan_id, plan_name, price, validity, daily_data,
                ott, cat, pmode, gateway,
                tx_time.strftime("%Y-%m-%d %H:%M:%S"), status, latency, discount, net_amount
            ])

            if i % 10000 == 0:
                print(f"Generated {i}/{num_records} rows...")

    print(f"Successfully generated: {trans_csv} ({os.path.getsize(trans_csv) / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    generate_telecom_data(52000)
