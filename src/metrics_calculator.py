# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Business Metrics & KPI Calculation Engine
Pure Python / Pandas calculations for ARPU, GMV, Churn % and Gateway Latency.
"""

import pandas as pd
import numpy as np

def calculate_executive_kpis(df):
    """
    Returns high-level business indicators for C-suite executive dashboard.
    """
    total_tx = len(df)
    success_df = df[df['status'] == 'SUCCESS']
    failed_df = df[df['status'] == 'FAILED']

    total_gmv = success_df['net_amount'].sum()
    success_rate = (len(success_df) / total_tx * 100) if total_tx > 0 else 0
    unique_subscribers = df['customer_id'].nunique()
    
    # ARPU (Average Revenue Per User)
    arpu = (total_gmv / unique_subscribers) if unique_subscribers > 0 else 0
    avg_ticket_size = success_df['net_amount'].mean() if len(success_df) > 0 else 0
    avg_latency = df['latency_ms'].mean() if total_tx > 0 else 0
    churn_risk_subscribers = df[df['is_churn_risk'] == 1]['customer_id'].nunique()
    churn_rate = (churn_risk_subscribers / unique_subscribers * 100) if unique_subscribers > 0 else 0

    return {
        "total_gmv": total_gmv,
        "total_transactions": total_tx,
        "success_rate": success_rate,
        "unique_subscribers": unique_subscribers,
        "arpu": arpu,
        "avg_ticket_size": avg_ticket_size,
        "avg_latency": avg_latency,
        "churn_rate": churn_rate,
        "churn_risk_subscribers": churn_risk_subscribers
    }

def calculate_operator_breakdown(df):
    """
    Returns comparative operator performance matrix.
    """
    success_df = df[df['status'] == 'SUCCESS']
    breakdown = success_df.groupby('operator', observed=True).agg(
        total_revenue=('net_amount', 'sum'),
        total_recharges=('transaction_id', 'count'),
        subscribers=('customer_id', 'nunique'),
        avg_price=('price_inr', 'mean')
    ).reset_index()

    breakdown['arpu'] = (breakdown['total_revenue'] / breakdown['subscribers']).round(1)
    breakdown['market_share_pct'] = (breakdown['total_revenue'] / breakdown['total_revenue'].sum() * 100).round(1)
    return breakdown.sort_values(by='total_revenue', ascending=False)

def calculate_gateway_performance(df):
    """
    Evaluates payment gateway latency and reliability.
    """
    perf = df.groupby('gateway', observed=True).agg(
        total_attempts=('transaction_id', 'count'),
        success_count=('status', lambda s: (s == 'SUCCESS').sum()),
        avg_latency_ms=('latency_ms', 'mean')
    ).reset_index()

    perf['success_rate_pct'] = (perf['success_count'] / perf['total_attempts'] * 100).round(1)
    perf['avg_latency_ms'] = perf['avg_latency_ms'].round(0)
    return perf.sort_values(by='success_rate_pct', ascending=False)
