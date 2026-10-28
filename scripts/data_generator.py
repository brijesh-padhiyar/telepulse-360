# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Synthetic Indian Telecom Transaction Data Generator
Generates 50,000+ realistic transaction records across Reliance Jio, Bharti Airtel,
Vodafone Idea, and BSNL across 22 Indian Telecom Circles adhering strictly to the
14-column master enterprise data schema.
"""

import os
import random
import datetime
from pathlib import Path
import pandas as pd
import numpy as np

def generate_telecom_dataset(num_records=50000, num_customers=18000, output_path="data/raw/telecom_transactions.csv", seed=42):
    random.seed(seed)
    np.random.seed(seed)

    print(f"🚀 Initializing TELEPULSE 360° Data Synthesis Engine ({num_records:,} records)...")

    # 1. Customer Identification Pool
    customer_pool = [f"CUST_{i:06d}" for i in range(1, num_customers + 1)]

    # 2. Operators & TRAI Market Share Weights
    operators = ["Reliance Jio", "Bharti Airtel", "Vodafone Idea", "BSNL"]
    op_weights = [0.44, 0.33, 0.19, 0.04]

    # 3. 22 Indian Telecom Circles
    circles = [
        "Maharashtra & Goa", "Delhi NCR", "Mumbai", "Gujarat", "Karnataka",
        "Tamil Nadu", "Andhra Pradesh & Telangana", "Uttar Pradesh (East)",
        "Uttar Pradesh (West)", "West Bengal & Kolkata", "Rajasthan", "Madhya Pradesh & CG",
        "Punjab & Haryana", "Bihar & Jharkhand", "Kerala", "Assam & North East", "Odisha", "Jammu & Kashmir"
    ]

    # 4. Realistic Tariff Packs per Operator
    OPERATOR_PLANS = {
        "Reliance Jio": [
            {"plan_type": "5G Unlimited Booster", "amount": 61, "validity_days": 28, "data_gb": 10.0, "prob": 0.15},
            {"plan_type": "Daily Data (1.5GB/day)", "amount": 239, "validity_days": 28, "data_gb": 42.0, "prob": 0.40},
            {"plan_type": "Daily Data (2GB/day)", "amount": 299, "validity_days": 28, "data_gb": 56.0, "prob": 0.25},
            {"plan_type": "Daily Data (1.5GB/day)", "amount": 666, "validity_days": 84, "data_gb": 126.0, "prob": 0.12},
            {"plan_type": "Annual Plan (365 Days)", "amount": 2999, "validity_days": 365, "data_gb": 912.5, "prob": 0.04},
            {"plan_type": "Budget Voice / Top-Up", "amount": 155, "validity_days": 28, "data_gb": 2.0, "prob": 0.04}
        ],
        "Bharti Airtel": [
            {"plan_type": "5G Unlimited Booster", "amount": 65, "validity_days": 28, "data_gb": 12.0, "prob": 0.14},
            {"plan_type": "Daily Data (1.5GB/day)", "amount": 265, "validity_days": 28, "data_gb": 42.0, "prob": 0.38},
            {"plan_type": "Daily Data (2GB/day)", "amount": 359, "validity_days": 28, "data_gb": 56.0, "prob": 0.28},
            {"plan_type": "Daily Data (1.5GB/day)", "amount": 719, "validity_days": 84, "data_gb": 126.0, "prob": 0.12},
            {"plan_type": "Annual Plan (365 Days)", "amount": 3359, "validity_days": 365, "data_gb": 912.5, "prob": 0.05},
            {"plan_type": "Budget Voice / Top-Up", "amount": 179, "validity_days": 28, "data_gb": 2.0, "prob": 0.03}
        ],
        "Vodafone Idea": [
            {"plan_type": "Daily Data (1.5GB/day)", "amount": 249, "validity_days": 28, "data_gb": 42.0, "prob": 0.45},
            {"plan_type": "Daily Data (2GB/day)", "amount": 319, "validity_days": 28, "data_gb": 56.0, "prob": 0.30},
            {"plan_type": "Daily Data (1.5GB/day)", "amount": 719, "validity_days": 84, "data_gb": 126.0, "prob": 0.15},
            {"plan_type": "Annual Plan (365 Days)", "amount": 2899, "validity_days": 365, "data_gb": 547.5, "prob": 0.03},
            {"plan_type": "Budget Voice / Top-Up", "amount": 155, "validity_days": 28, "data_gb": 1.0, "prob": 0.07}
        ],
        "BSNL": [
            {"plan_type": "Budget Voice / Top-Up", "amount": 107, "validity_days": 35, "data_gb": 3.0, "prob": 0.40},
            {"plan_type": "Daily Data (2GB/day)", "amount": 199, "validity_days": 30, "data_gb": 60.0, "prob": 0.35},
            {"plan_type": "Daily Data (1.5GB/day)", "amount": 397, "validity_days": 150, "data_gb": 300.0, "prob": 0.18},
            {"plan_type": "Annual Plan (365 Days)", "amount": 1999, "validity_days": 365, "data_gb": 600.0, "prob": 0.07}
        ]
    }

    # 5. Payment Instruments & Share
    gateways = ["UPI (PhonePe)", "UPI (Google Pay)", "UPI (Paytm)", "Credit/Debit Card", "Net Banking"]
    gw_weights = [0.46, 0.35, 0.11, 0.05, 0.03]

    start_date = datetime.datetime(2026, 8, 1, 0, 0, 0)
    records = []

    for i in range(1, num_records + 1):
        txn_id = f"TXN2026{i:08d}"
        cust_id = random.choice(customer_pool)
        op = random.choices(operators, weights=op_weights, k=1)[0]
        circ = random.choice(circles)
        
        # Plan selection
        p_choices = OPERATOR_PLANS[op]
        plan = random.choices(p_choices, weights=[p["prob"] for p in p_choices], k=1)[0]
        
        # Timestamp with realistic peak evening traffic (8 PM - 11 PM)
        day_offset = random.randint(0, 85)
        hour = random.choices(range(24), weights=[1,1,1,1,1,2,3,4,5,6,6,5,5,5,5,6,7,8,10,10,9,7,4,2], k=1)[0]
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        dt = start_date + datetime.timedelta(days=day_offset, hours=hour, minutes=minute, seconds=second)
        
        # Daily usage telemetry
        daily_usage = round(max(0.1, min(8.5, random.gauss(plan["data_gb"] / plan["validity_days"] * 0.9, 0.5))), 2)
        
        # Gateway selection & Latency modeling
        gw = random.choices(gateways, weights=gw_weights, k=1)[0]
        if "UPI" in gw:
            base_lat = random.randint(350, 1400)
        elif "Card" in gw:
            base_lat = random.randint(1100, 3200)
        else:
            base_lat = random.randint(2100, 5800)
            
        # Success vs Gateway Failure probability
        if random.random() < 0.958:
            status = "Success"
            latency = base_lat
        else:
            status = random.choice(["Gateway Timeout", "Bank Decline", "User Abandoned"])
            latency = base_lat + random.randint(1500, 3500)
            
        # Network Generation
        if op == "Reliance Jio":
            net = random.choices(["5G Standalone", "4G LTE"], weights=[0.58, 0.42], k=1)[0]
        elif op == "Bharti Airtel":
            net = random.choices(["5G Non-Standalone", "4G LTE"], weights=[0.52, 0.48], k=1)[0]
        elif op == "Vodafone Idea":
            net = random.choices(["4G LTE", "3G/2G Legacy"], weights=[0.88, 0.12], k=1)[0]
        else:
            net = random.choices(["3G/2G Legacy", "4G LTE"], weights=[0.72, 0.28], k=1)[0]
            
        records.append({
            "transaction_id": txn_id,
            "customer_id": cust_id,
            "transaction_date": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "operator": op,
            "circle": circ,
            "plan_type": plan["plan_type"],
            "amount_inr": float(plan["amount"]),
            "validity_days": int(plan["validity_days"]),
            "data_allowance_gb": float(plan["data_gb"]),
            "daily_avg_usage_gb": float(daily_usage),
            "payment_gateway": gw,
            "payment_status": status,
            "latency_ms": int(latency),
            "network_generation": net
        })

    df = pd.DataFrame(records)
    
    # Save to CSV
    out_dir = Path(output_path).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅ Generated {len(df):,} transactions ({file_size_mb:.2f} MB)")
    print(f"📁 Output Saved: {output_path}")
    return df

if __name__ == "__main__":
    generate_telecom_dataset()
