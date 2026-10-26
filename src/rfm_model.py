# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Telecom RFM-D Segmentation & Machine Learning Engine
Computes Recency, Frequency, Monetary + Data Appetite (RFM-D) and assigns customer clusters.
"""

import pandas as pd
import numpy as np

def compute_rfmd_features(df):
    """
    Computes Customer-level RFM-D aggregated metrics from transaction logs.
    """
    success_df = df[df['status'] == 'SUCCESS']
    snapshot_date = df['recharge_timestamp'].max() + pd.Timedelta(days=1)

    rfm = success_df.groupby('customer_id').agg(
        operator=('operator', 'first'),
        circle=('circle', 'first'),
        handset=('handset_type', 'first'),
        recency=('recharge_timestamp', lambda x: (snapshot_date - x.max()).days),
        frequency=('transaction_id', 'count'),
        monetary=('net_amount', 'sum'),
        avg_daily_data=('daily_data_gb', 'mean')
    ).reset_index()

    # R Score: lower recency is better (1 to 5)
    rfm['r_score'] = pd.qcut(rfm['recency'].rank(method='first'), q=5, labels=[5, 4, 3, 2, 1])
    # F Score: higher frequency is better (1 to 5)
    rfm['f_score'] = pd.qcut(rfm['frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5])
    # M Score: higher spend is better (1 to 5)
    rfm['m_score'] = pd.qcut(rfm['monetary'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5])
    # D Score: higher data appetite is better (1 to 5)
    rfm['d_score'] = pd.qcut(rfm['avg_daily_data'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5])

    # Convert to numeric for cluster evaluation
    for col in ['r_score', 'f_score', 'm_score', 'd_score']:
        rfm[col] = rfm[col].astype(int)

    # Segment Classification Rule
    def segment_customer(row):
        r, f, m, d = row['r_score'], row['f_score'], row['m_score'], row['d_score']
        if r >= 4 and f >= 4 and m >= 4:
            return "Champions (High Value)"
        elif d >= 4 and f >= 3:
            return "5G Data Addicts"
        elif r <= 2 and f <= 2:
            return "At-Risk / Inactive Sleepers"
        elif m <= 2 and d <= 2:
            return "Budget / Voice-First"
        else:
            return "Loyal Mainstream"

    rfm['segment'] = rfm.apply(segment_customer, axis=1)
    return rfm

def get_cluster_summary(rfm_df):
    """
    Returns summary statistics for each customer segment.
    """
    summary = rfm_df.groupby('segment').agg(
        customer_count=('customer_id', 'count'),
        avg_spend=('monetary', 'mean'),
        avg_orders=('frequency', 'mean'),
        avg_recency_days=('recency', 'mean'),
        avg_data_gb=('avg_daily_data', 'mean')
    ).round(1).reset_index()

    summary['share_pct'] = (summary['customer_count'] / summary['customer_count'].sum() * 100).round(1)
    return summary.sort_values(by='avg_spend', ascending=False)
