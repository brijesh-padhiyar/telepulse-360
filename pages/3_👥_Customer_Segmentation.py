# -*- coding: utf-8 -*-
"""
TELEPULSE 360° - Page 3: Telecom RFM-D Customer Segmentation & Machine Learning
Customer persona profiling, 3D cluster visualization, and targeted marketing export.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_pipeline import load_and_clean_data
from src.rfm_model import compute_rfmd_features, get_cluster_summary

st.title("👥 Telecom RFM-D Customer Segmentation")
st.markdown("Advanced Subscriber Profiling using Recency ($R$), Frequency ($F$), Monetary ($M$), and Daily Data Appetite ($D$).")

df = load_and_clean_data()

@st.cache_data(ttl=3600)
def get_rfm_data(data):
    return compute_rfmd_features(data)

rfm_df = get_rfm_data(df)
summary_df = get_cluster_summary(rfm_df)

# Segment Summary KPIs
st.subheader("🎯 Customer Segment Distribution")
st.dataframe(
    summary_df.rename(columns={
        "segment": "Customer Segment",
        "customer_count": "Subscribers",
        "avg_spend": "Avg Annual Spend (₹)",
        "avg_orders": "Avg Recharges / Year",
        "avg_recency_days": "Avg Recency (Days)",
        "avg_data_gb": "Avg Daily Data (GB)",
        "share_pct": "Share %"
    }),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# 3D Scatter Plot (Recency vs Frequency vs Monetary)
st.subheader("🌐 3D Interactive Cluster Space (RFM-D)")
fig_3d = px.scatter_3d(
    rfm_df.sample(min(2500, len(rfm_df))),
    x='recency', y='frequency', z='monetary',
    color='segment',
    size='avg_daily_data',
    hover_data=['operator', 'circle'],
    opacity=0.75,
    title="3D Spatial Distribution: Recency vs Frequency vs Monetary (Size = Daily GB)",
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig_3d.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    scene=dict(
        xaxis_title="Recency (Days)",
        yaxis_title="Frequency (Recharges)",
        zaxis_title="Monetary Value (₹)"
    ),
    margin=dict(l=10, r=10, t=30, b=10)
)
st.plotly_chart(fig_3d, use_container_width=True)

# Export Leads to CSV for Marketing Campaigns
st.markdown("---")
st.subheader("📥 Export Targeted Customer Leads")
selected_seg = st.selectbox("Select Segment to Export", rfm_df['segment'].unique())
seg_export = rfm_df[rfm_df['segment'] == selected_seg]

st.write(f"Total Customers in **{selected_seg}**: **{len(seg_export):,}**")
csv_data = seg_export.to_csv(index=False).encode('utf-8')
st.download_button(
    label=f"Download {selected_seg} Leads (CSV)",
    data=csv_data,
    file_name=f"{selected_seg.replace(' ', '_').lower()}_leads.csv",
    mime="text/csv"
)
