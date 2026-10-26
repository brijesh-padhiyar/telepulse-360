# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - High-Speed Pure Python / Pandas Data Pipeline
Reads raw 50,000+ CSV transactions, performs clean typing, calculates temporal features,
and prepares optimized Parquet data for the Streamlit dashboard.
"""

import os
import pandas as pd
import numpy as np

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RAW_CSV = os.path.join(DATA_DIR, "raw", "telecom_transactions.csv")
PROCESSED_PARQUET = os.path.join(DATA_DIR, "processed", "cleaned_telecom.parquet")

def load_and_clean_data(force_refresh=False):
    """
    Loads raw CSV or cached Parquet with automated cleaning and feature engineering.
    """
    if not force_refresh and os.path.exists(PROCESSED_PARQUET):
        try:
            return pd.read_parquet(PROCESSED_PARQUET)
        except Exception:
            pass

    if not os.path.exists(RAW_CSV):
        raise FileNotFoundError(f"Raw data not found at: {RAW_CSV}. Run scripts/data_generator.py first.")

    # Ingest 50,000+ rows
    df = pd.read_csv(RAW_CSV)

    # 1. Datetime parsing & temporal features
    df['recharge_timestamp'] = pd.to_datetime(df['recharge_timestamp'])
    df['date'] = df['recharge_timestamp'].dt.date
    df['year_month'] = df['recharge_timestamp'].dt.to_period('M').astype(str)
    df['month_name'] = df['recharge_timestamp'].dt.strftime('%b %Y')
    df['hour'] = df['recharge_timestamp'].dt.hour
    df['day_name'] = df['recharge_timestamp'].dt.day_name()
    df['is_weekend'] = df['recharge_timestamp'].dt.weekday.isin([5, 6]).astype(int)

    # 2. Type casting & categorical optimization
    cat_cols = ['operator', 'circle', 'handset_type', 'plan_category', 'payment_mode', 'gateway', 'status']
    for col in cat_cols:
        df[col] = df[col].astype('category')

    # 3. Numeric cleaning
    df['price_inr'] = pd.to_numeric(df['price_inr'], errors='coerce').fillna(0)
    df['net_amount'] = pd.to_numeric(df['net_amount'], errors='coerce').fillna(0)
    df['daily_data_gb'] = pd.to_numeric(df['daily_data_gb'], errors='coerce').fillna(0)
    df['latency_ms'] = pd.to_numeric(df['latency_ms'], errors='coerce').fillna(1000)

    # 4. Churn delay window feature (without SQL!)
    # Sorting by customer and timestamp to find gap between recharges
    df = df.sort_values(by=['customer_id', 'recharge_timestamp'])
    df['prev_recharge'] = df.groupby('customer_id')['recharge_timestamp'].shift(1)
    df['recharge_gap_days'] = (df['recharge_timestamp'] - df['prev_recharge']).dt.total_seconds() / (24 * 3600)
    df['recharge_gap_days'] = df['recharge_gap_days'].round(1).fillna(0)

    # Flag silent churn risk (gap > plan validity + 7 grace days)
    df['is_churn_risk'] = ((df['recharge_gap_days'] > (df['validity_days'] + 7)) & (df['recharge_gap_days'] > 0)).astype(int)

    # Save to processed Parquet for instant dashboard caching
    os.makedirs(os.path.dirname(PROCESSED_PARQUET), exist_ok=True)
    try:
        df.to_parquet(PROCESSED_PARQUET, index=False)
    except Exception:
        pass

    return df

if __name__ == "__main__":
    df = load_and_clean_data(force_refresh=True)
    print(f"Data pipeline ready! Processed {len(df)} rows across {df['operator'].nunique()} operators.")
