# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Page 1: Executive ARPU & Tariff War Benchmarking
Deep competitive comparison between Reliance Jio, Bharti Airtel, Vodafone Idea, and BSNL.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.data_pipeline import load_and_clean_data
from src.metrics_calculator import calculate_operator_breakdown

st.title("📈 Executive ARPU & Tariff War Benchmarking")
st.markdown("Head-to-head comparison of Indian Telecom Operators on Average Revenue Per User, Ticket Size, and Subscriber Quality.")

df = load_and_clean_data()
success_df = df[df['status'] == 'SUCCESS']

# Comparative Operator Table
st.subheader("🏆 Operator Performance Leaderboard")
op_df = calculate_operator_breakdown(df)

col1, col2 = st.columns([6, 4])
with col1:
    st.dataframe(
        op_df.rename(columns={
            "operator": "Telecom Operator",
            "total_revenue": "Net Revenue (₹)",
            "total_recharges": "Recharges",
            "subscribers": "Active Users",
            "arpu": "ARPU (₹)",
            "market_share_pct": "Market Share %"
        }),
        use_container_width=True,
        hide_index=True
    )

with col2:
    fig_arpu = px.bar(
        op_df, x='operator', y='arpu',
        color='operator',
        text='arpu',
        title="ARPU Benchmarking (INR / User)",
        color_discrete_map={
            "Reliance Jio": "#0284c7",
            "Bharti Airtel": "#dc2626",
            "Vodafone Idea": "#d97706",
            "BSNL": "#059669"
        }
    )
    fig_arpu.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
    st.plotly_chart(fig_arpu, use_container_width=True)

st.markdown("---")

# Ticket Size Distribution (Box Plot)
st.subheader("📊 Recharge Ticket Size Distribution by Operator")
fig_box = px.box(
    success_df, x='operator', y='price_inr',
    color='operator',
    points=False,
    title="Price Distribution & Outlier Spread (Boxplot)",
    color_discrete_map={
        "Reliance Jio": "#0284c7",
        "Bharti Airtel": "#dc2626",
        "Vodafone Idea": "#d97706",
        "BSNL": "#059669"
    }
)
fig_box.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
st.plotly_chart(fig_box, use_container_width=True)

# Peak Hour Traffic Heatmap
st.subheader("🔥 24-Hour Peak Load & Traffic Congestion")
hour_day = df.groupby(['day_name', 'hour'])['transaction_id'].count().reset_index()
pivot_heatmap = hour_day.pivot(index='day_name', columns='hour', values='transaction_id').fillna(0)

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_heatmap = pivot_heatmap.reindex(days_order)

fig_heat = px.imshow(
    pivot_heatmap,
    labels=dict(x="Hour of Day (00:00 - 23:00)", y="Day of Week", color="Recharge Volume"),
    color_continuous_scale="Viridis",
    title="Recharge Server Traffic Heatmap (Peak Hours: 8:00 PM – 11:00 PM)"
)
fig_heat.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_heat, use_container_width=True)
