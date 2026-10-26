# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Pan-India Telecom Intelligence & ARPU Analytics Platform
Main Streamlit Application & Executive C-Suite Dashboard Shell.
"""

import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Modular local imports
from src.data_pipeline import load_and_clean_data
from src.metrics_calculator import calculate_executive_kpis, calculate_operator_breakdown

# 1. Page Configuration
st.set_page_config(
    page_title="TELEPULSE 360° | Telecom Intelligence",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load Custom CSS
css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 3. Data Loading with Performance Caching
@st.cache_data(ttl=3600, show_spinner="Loading 50,000+ Telecom Records...")
def get_dataset():
    return load_and_clean_data()

try:
    df_raw = get_dataset()
except Exception as e:
    st.error(f"Error loading dataset: {e}. Please ensure data generator has run.")
    st.stop()

# 4. Sidebar Dynamic Filter Controls
st.sidebar.title("📱 TELEPULSE 360°")
st.sidebar.caption("Pan-India Telecom Intelligence & ARPU Engine")
st.sidebar.markdown("---")

# Operator Filter
operators_list = ["All Operators"] + sorted(list(df_raw['operator'].unique()))
selected_operator = st.sidebar.selectbox("Select Telecom Operator", operators_list)

# Circle Filter
circles_list = ["All Circles"] + sorted(list(df_raw['circle'].unique()))
selected_circle = st.sidebar.selectbox("Select Telecom Circle", circles_list)

# Handset Filter
handset_list = ["All Handsets"] + sorted(list(df_raw['handset_type'].unique()))
selected_handset = st.sidebar.selectbox("Select Handset Technology", handset_list)

# Filter Data Reactively
filtered_df = df_raw.copy()
if selected_operator != "All Operators":
    filtered_df = filtered_df[filtered_df['operator'] == selected_operator]
if selected_circle != "All Circles":
    filtered_df = filtered_df[filtered_df['circle'] == selected_circle]
if selected_handset != "All Handsets":
    filtered_df = filtered_df[filtered_df['handset_type'] == selected_handset]

# 5. Header Banner
st.markdown("""
<div class="section-banner">
    <div class="section-title">Executive Telecom C-Suite Dashboard</div>
    <div class="section-subtitle">Real-time Gross Merchandise Value (GMV), ARPU Benchmarking & Churn Diagnostics (Jio &bull; Airtel &bull; Vi &bull; BSNL)</div>
</div>
""", unsafe_allow_html=True)

# 6. Calculate Dynamic KPIs
kpis = calculate_executive_kpis(filtered_df)

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.metric("Total Revenue (GMV)", f"₹{kpis['total_gmv']/1e6:.2f}M", delta="Active 2026")
with c2:
    st.metric("National ARPU", f"₹{kpis['arpu']:.1f}", delta=f"{'+₹24 vs Benchmark' if kpis['arpu'] > 180 else '-₹12 vs Benchmark'}")
with c3:
    st.metric("Success Rate", f"{kpis['success_rate']:.1f}%", delta=f"{kpis['total_transactions']:,} txns")
with c4:
    st.metric("Active Subscribers", f"{kpis['unique_subscribers']:,}", delta="100% Verified")
with c5:
    st.metric("Silent Churn Risk", f"{kpis['churn_rate']:.1f}%", delta=f"{kpis['churn_risk_subscribers']:,} users", delta_color="inverse")

st.markdown("---")

# 7. Core Analytics Charts
col_left, col_right = st.columns([6, 4])

with col_left:
    st.subheader("📈 Monthly Revenue Trend & Transaction Velocity")
    # Group by month
    monthly_trend = filtered_df[filtered_df['status'] == 'SUCCESS'].groupby('year_month').agg(
        revenue=('net_amount', 'sum'),
        transactions=('transaction_id', 'count')
    ).reset_index()

    fig_trend = go.Figure()
    fig_trend.add_trace(go.Bar(
        x=monthly_trend['year_month'], y=monthly_trend['revenue'],
        name="Gross Revenue (INR)", marker_color="#2563eb", yaxis="y1"
    ))
    fig_trend.add_trace(go.Scatter(
        x=monthly_trend['year_month'], y=monthly_trend['transactions'],
        name="Recharge Volume", line=dict(color="#10b981", width=3), yaxis="y2"
    ))
    fig_trend.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(title="Gross Revenue (₹)"),
        yaxis2=dict(title="Transaction Count", overlaying="y", side="right"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col_right:
    st.subheader("🍩 Operator Market Share")
    op_breakdown = calculate_operator_breakdown(filtered_df)
    fig_donut = px.pie(
        op_breakdown, values='total_revenue', names='operator',
        hole=0.55,
        color='operator',
        color_discrete_map={
            "Reliance Jio": "#0284c7",
            "Bharti Airtel": "#dc2626",
            "Vodafone Idea": "#d97706",
            "BSNL": "#059669"
        }
    )
    fig_donut.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=20, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2)
    )
    st.plotly_chart(fig_donut, use_container_width=True)

# 8. Plan Category & Payment Mode Distribution
c_bottom1, c_bottom2 = st.columns(2)

with c_bottom1:
    st.subheader("⚡ Popularity by Plan Category")
    plan_cat = filtered_df[filtered_df['status'] == 'SUCCESS'].groupby('plan_category')['net_amount'].sum().reset_index()
    fig_cat = px.bar(
        plan_cat, x='plan_category', y='net_amount',
        color='plan_category',
        color_discrete_sequence=px.colors.qualitative.Prism,
        text_auto='.2s'
    )
    fig_cat.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
    st.plotly_chart(fig_cat, use_container_width=True)

with c_bottom2:
    st.subheader("💳 Payment Mode & Channel Share")
    pmode_cat = filtered_df.groupby('payment_mode')['transaction_id'].count().reset_index()
    fig_pmode = px.bar(
        pmode_cat, x='transaction_id', y='payment_mode',
        orientation='h',
        color='transaction_id',
        color_continuous_scale="Viridis"
    )
    fig_pmode.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
    st.plotly_chart(fig_pmode, use_container_width=True)

# Footer Info
st.markdown("---")
st.caption("TELEPULSE 360° &bull; BCA Semester 7 OJT Capstone Platform &bull; Developed by Brijesh Padhiyar &bull; Sardar Patel University (SPU)")
