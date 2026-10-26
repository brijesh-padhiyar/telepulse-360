# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Page 2: Pan-India 22 Telecom Circles & Payment Gateway Health
Geospatial market penetration, Circle rankings, and Fintech reliability funnel.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.data_pipeline import load_and_clean_data
from src.metrics_calculator import calculate_gateway_performance

st.title("🗺️ Pan-India 22 Telecom Circles & Payment Gateway Health")
st.markdown("Regional penetration analysis across Indian telecom circles and financial payment gateway diagnostics.")

df = load_and_clean_data()
success_df = df[df['status'] == 'SUCCESS']

# Circle Revenue Leaderboard
st.subheader("📍 Circle Revenue & Market Penetration")
circle_rev = success_df.groupby('circle', observed=True).agg(
    total_gmv=('net_amount', 'sum'),
    recharges=('transaction_id', 'count'),
    arpu=('net_amount', 'mean')
).reset_index().sort_values(by='total_gmv', ascending=False)

fig_circle = px.bar(
    circle_rev, x='total_gmv', y='circle',
    orientation='h',
    color='total_gmv',
    color_continuous_scale="Blues",
    title="Telecom Circles Ranked by Gross Revenue (₹)",
    text_auto='.2s'
)
fig_circle.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", yaxis=dict(autorange="reversed"))
st.plotly_chart(fig_circle, use_container_width=True)

st.markdown("---")

# Payment Gateway Diagnostics
st.subheader("💳 Fintech Payment Gateway Reliability & Drop-off Funnel")
col_gw1, col_gw2 = st.columns([5, 5])

with col_gw1:
    gw_perf = calculate_gateway_performance(df)
    st.dataframe(
        gw_perf.rename(columns={
            "gateway": "Payment Gateway",
            "total_attempts": "Attempts",
            "success_count": "Successful",
            "success_rate_pct": "Success Rate %",
            "avg_latency_ms": "Avg Latency (ms)"
        }),
        use_container_width=True,
        hide_index=True
    )

with col_gw2:
    # Drop-Off Funnel
    total = len(df)
    initiated = total
    gateway_handoff = int(total * 0.965)
    bank_auth = int(total * 0.925)
    successful = len(success_df)

    fig_funnel = go.Figure(go.Funnel(
        y=["Initiated", "Gateway Handoff", "Bank Auth", "Success"],
        x=[initiated, gateway_handoff, bank_auth, successful],
        textinfo="value+percent initial",
        marker=dict(color=["#3b82f6", "#60a5fa", "#93c5fd", "#10b981"])
    ))
    fig_funnel.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_funnel, use_container_width=True)
