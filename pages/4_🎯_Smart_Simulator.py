# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Page 4: Interactive What-If Decision Simulators
Consumer Smart Plan Recommender + Telecom Tariff Hike Financial Impact Simulator.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("🎯 Interactive What-If Decision Simulators")
st.markdown("Prescriptive decision tools for both Telecom Consumers (Savings) and Telecom Executives (Tariff Hike Elasticity).")

tab1, tab2 = st.tabs(["💡 Smart Plan Optimizer (Consumer)", "📊 Tariff Hike Impact Simulator (Executive)"])

# ----------------- TAB 1: CONSUMER PLAN RECOMMENDER -----------------
with tab1:
    st.subheader("💡 Find Your Optimal Money-Saving Recharge Plan")
    st.markdown("Enter your daily usage pattern to discover the most cost-effective tariff plan:")

    col_inp1, col_inp2, col_inp3 = st.columns(3)
    with col_inp1:
        daily_gb = st.slider("Daily Data Requirement (GB)", min_value=0.5, max_value=3.5, value=1.5, step=0.5)
    with col_inp2:
        preferred_op = st.selectbox("Current Operator", ["Reliance Jio", "Bharti Airtel", "Vodafone Idea", "BSNL"])
    with col_inp3:
        ott_choice = st.selectbox("Preferred OTT Subscription", ["None", "Disney+ Hotstar", "SonyLIV / Zee5"])

    # Recommendation Calculation Logic
    if daily_gb <= 1.0 and ott_choice == "None":
        rec_plan = "28-Day Standard Voice Pack (₹209)"
        monthly_cost = 209
        annual_cost = 209 * 13
        annual_opt = 197 * 5 if preferred_op == "BSNL" else 155 * 13
        savings = annual_cost - annual_opt
    elif daily_gb <= 2.0 and ott_choice == "None":
        rec_plan = "84-Day True 5G Pack (₹719)"
        monthly_cost = 239
        annual_cost = monthly_cost * 13
        annual_opt = 719 * 4.34
        savings = int(annual_cost - annual_opt)
    elif "Hotstar" in ott_choice:
        rec_plan = "84-Day Hotstar Bundled Pack (₹839)"
        annual_cost = (299 * 13) + 499  # Separate plan + standalone Hotstar
        annual_opt = 839 * 4.34
        savings = int(annual_cost - annual_opt)
    else:
        rec_plan = "365-Day Annual Mega Unlimited (₹2999)"
        annual_cost = 399 * 13
        annual_opt = 2999
        savings = int(annual_cost - annual_opt)

    st.success(f"### 🌟 Recommended Plan: **{rec_plan}**")
    m1, m2, m3 = st.columns(3)
    m1.metric("Current Projected Annual Spend", f"₹{int(annual_cost):,}")
    m2.metric("Optimal Annual Spend with Recommendation", f"₹{int(annual_opt):,}")
    m3.metric("Your Total Annual Savings", f"₹{savings:,}", delta=f"Save ₹{savings:,}/year")

# ----------------- TAB 2: TARIFF HIKE IMPACT SIMULATOR -----------------
with tab2:
    st.subheader("📊 Telecom Tariff Hike 'What-If' Financial Sensitivity Model")
    st.markdown("Simulate how a national tariff revision (e.g., 10% – 25% price hike) impacts Gross Revenue vs Customer Churn Loss:")

    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        hike_pct = st.slider("Proposed Tariff Hike Percentage (%)", min_value=5, max_value=30, value=15, step=5)
    with col_sim2:
        elasticity = st.selectbox("Consumer Price Elasticity Sensitivity", ["Low (Essential 5G Demand)", "Moderate (Standard Indian Market)", "High (Heavy Price Sensitivity)"])

    elasticity_multipliers = {
        "Low (Essential 5G Demand)": 0.20,
        "Moderate (Standard Indian Market)": 0.35,
        "High (Heavy Price Sensitivity)": 0.55
    }
    churn_loss_factor = elasticity_multipliers[elasticity]
    projected_churn_pct = hike_pct * churn_loss_factor

    # Baseline calculations
    base_gmv = 24.5  # in Millions INR
    revenue_uplift_pct = hike_pct - projected_churn_pct
    projected_gmv = base_gmv * (1 + (revenue_uplift_pct / 100))
    net_gain = projected_gmv - base_gmv

    col_res1, col_res2, col_res3 = st.columns(3)
    col_res1.metric("Baseline Annual GMV", f"₹{base_gmv:.1f}M")
    col_res2.metric("Projected Annual GMV After Hike", f"₹{projected_gmv:.1f}M", delta=f"+₹{net_gain:.2f}M Gain")
    col_res3.metric("Projected Subscriber Churn", f"{projected_churn_pct:.1f}%", delta=f"-{projected_churn_pct:.1f}% churn", delta_color="inverse")

    # Simulation Chart
    hike_ranges = list(range(5, 35, 5))
    gmv_projections = [base_gmv * (1 + ((h - (h * churn_loss_factor)) / 100)) for h in hike_ranges]

    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter(
        x=hike_ranges, y=gmv_projections,
        mode="lines+markers",
        name="Projected GMV (INR Millions)",
        line=dict(color="#2563eb", width=3),
        marker=dict(size=8, color="#10b981")
    ))
    fig_sim.update_layout(
        title="Net Revenue Trajectory Across Different Tariff Hike Percentages",
        xaxis_title="Tariff Hike Percentage (%)",
        yaxis_title="Projected Annual GMV (₹ Millions)",
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_sim, use_container_width=True)
