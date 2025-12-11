import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sqlite3
import os

st.set_page_config(page_title="Tariff Dashboard", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
<style>
    [data-testid="stMetric"] {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .main-title {
        color: #6c63ff;
        font-size: 2.5em;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Generate sample data
def get_sample_tariffs():
    data = {
        'country': ['US', 'US', 'US', 'China', 'China'],
        'hs_code': ['6204.62.20', '6204.62.20', '6204.62.30', '0201.10.20', '0201.90.20'],
        'product_description': ['Women cotton trousers', 'Women wool trousers', 'Women synthetic trousers', 'Beef fresh/chilled', 'Beef frozen'],
        'rate': [12.5, 15.0, 13.2, 25.0, 47.5],
        'effective_date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-10-01', '2024-12-01'],
    }
    return pd.DataFrame(data)

def get_historical_data():
    """Generate historical tariff data for charts"""
    dates = pd.date_range(start='2018-01-01', end='2025-01-01', freq='M')
    data = {
        'date': dates,
        'us_rate': [5.0, 5.0, 5.2, 6.0, 7.5, 10.0, 12.0, 12.5, 12.5, 12.5, 12.5, 12.5, 
                   12.5, 12.5, 12.5, 12.5, 16.5, 16.5, 16.5, 16.5, 16.5, 16.5, 16.5, 16.5,
                   16.5, 16.5, 25.0, 30.0, 35.0, 40.0, 47.5] + [47.5] * (len(dates) - 31),
        'china_rate': [8.0, 8.0, 8.5, 10.0, 12.0, 15.0, 18.0, 20.0, 20.0, 20.0, 20.0, 20.0,
                      20.0, 20.0, 20.0, 20.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0,
                      18.0, 18.0, 22.0, 25.0, 28.0, 32.0, 38.0] + [38.0] * (len(dates) - 31),
    }
    return pd.DataFrame(data)

def get_changes():
    """Recent tariff changes"""
    data = {
        'hs_code': ['0201.90.20', '0201.10.20', '6204.62.20'],
        'country': ['China', 'China', 'US'],
        'old_rate': [25.0, 20.0, 12.0],
        'new_rate': [47.5, 25.0, 12.5],
        'change_date': ['2024-12-01', '2024-10-01', '2024-06-15'],
        'reason': ['Section 301 escalation', 'Trade war phase 2', 'Routine update']
    }
    return pd.DataFrame(data)

# Title
st.markdown("<h1 class='main-title'>📊 Tariff Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Real-time tracking of US & China tariff rates with historical trends")

# Sidebar
with st.sidebar:
    st.header("🎛️ Filters")
    view_type = st.radio("Select View:", ["Dashboard", "Tariffs", "Changes", "Trends"])
    
    if view_type == "Tariffs":
        country_filter = st.multiselect("Country:", ["US", "China"], default=["US", "China"])
    else:
        country_filter = None

# Load data
tariffs_df = get_sample_tariffs()
historical_df = get_historical_data()
changes_df = get_changes()

# Dashboard View
if view_type == "Dashboard":
    col1, col2, col3, col4 = st.columns(4)
    
    us_count = len(tariffs_df[tariffs_df['country'] == 'US'])
    china_count = len(tariffs_df[tariffs_df['country'] == 'China'])
    avg_us = tariffs_df[tariffs_df['country'] == 'US']['rate'].mean()
    avg_china = tariffs_df[tariffs_df['country'] == 'China']['rate'].mean()
    
    with col1:
        st.metric("🇺🇸 US Tariffs", us_count, "items")
    with col2:
        st.metric("🇨🇳 China Tariffs", china_count, "items")
    with col3:
        st.metric("US Avg Rate", f"{avg_us:.1f}%", f"{avg_us:.1f}%")
    with col4:
        st.metric("China Avg Rate", f"{avg_china:.1f}%", f"{avg_china:.1f}%")
    
    st.divider()
    st.subheader("📈 Quick Trends")
    
    # Simple trend chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=historical_df['date'], y=historical_df['us_rate'],
                            mode='lines', name='US Rate', line=dict(color='#1f77b4', width=2)))
    fig.add_trace(go.Scatter(x=historical_df['date'], y=historical_df['china_rate'],
                            mode='lines', name='China Rate', line=dict(color='#ff7f0e', width=2)))
    fig.update_layout(title="Tariff Rate Trends (2018-2025)",
                     xaxis_title="Date", yaxis_title="Rate (%)",
                     hovermode='x unified', height=400)
    st.plotly_chart(fig, use_container_width=True)

# Tariffs View
elif view_type == "Tariffs":
    st.subheader("📋 Current Tariffs")
    
    if country_filter:
        filtered_df = tariffs_df[tariffs_df['country'].isin(country_filter)]
    else:
        filtered_df = tariffs_df
    
    # Format display
    display_df = filtered_df[['country', 'hs_code', 'product_description', 'rate', 'effective_date']].copy()
    display_df['rate'] = display_df['rate'].apply(lambda x: f"{x}%")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    st.info(f"📊 Total: {len(filtered_df)} tariffs displayed")

# Changes View
elif view_type == "Changes":
    st.subheader("📝 Recent Changes")
    
    for idx, row in changes_df.iterrows():
        col1, col2, col3 = st.columns([2, 2, 2])
        with col1:
            st.write(f"**{row['hs_code']}**")
            st.caption(row['country'])
        with col2:
            st.write(f"**{row['old_rate']}%** → **{row['new_rate']}%**")
            change = row['new_rate'] - row['old_rate']
            if change > 0:
                st.error(f"↑ +{change}%", icon="📈")
            else:
                st.success(f"↓ {change}%", icon="📉")
        with col3:
            st.write(row['change_date'])
            st.caption(row['reason'])
        st.divider()

# Trends View
elif view_type == "Trends":
    st.subheader("📊 Historical Trends")
    
    col1, col2 = st.columns(2)
    with col1:
        chart_type = st.selectbox("Chart Type:", ["Line", "Area"])
    with col2:
        date_range = st.slider("Date Range:", 
                              min_value=historical_df['date'].min().date(),
                              max_value=historical_df['date'].max().date(),
                              value=(historical_df['date'].min().date(), 
                                    historical_df['date'].max().date()))
    
    # Filter data by date range
    mask = (historical_df['date'].dt.date >= date_range[0]) & \
           (historical_df['date'].dt.date <= date_range[1])
    filtered_hist = historical_df[mask]
    
    # Create chart
    fig = go.Figure()
    
    if chart_type == "Line":
        fig.add_trace(go.Scatter(x=filtered_hist['date'], y=filtered_hist['us_rate'],
                                mode='lines', name='US Rate', line=dict(color='#1f77b4', width=3)))
        fig.add_trace(go.Scatter(x=filtered_hist['date'], y=filtered_hist['china_rate'],
                                mode='lines', name='China Rate', line=dict(color='#ff7f0e', width=3)))
    else:  # Area
        fig.add_trace(go.Scatter(x=filtered_hist['date'], y=filtered_hist['us_rate'],
                                mode='lines', name='US Rate', fill='tozeroy',
                                line=dict(color='#1f77b4')))
        fig.add_trace(go.Scatter(x=filtered_hist['date'], y=filtered_hist['china_rate'],
                                mode='lines', name='China Rate', fill='tozeroy',
                                line=dict(color='#ff7f0e')))
    
    fig.update_layout(title="Tariff Rates Over Time",
                     xaxis_title="Date", yaxis_title="Rate (%)",
                     hovermode='x unified', height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Current US Rate", f"{filtered_hist['us_rate'].iloc[-1]:.1f}%")
    with col2:
        st.metric("Current China Rate", f"{filtered_hist['china_rate'].iloc[-1]:.1f}%")
    with col3:
        st.metric("US Peak", f"{filtered_hist['us_rate'].max():.1f}%")
    with col4:
        st.metric("China Peak", f"{filtered_hist['china_rate'].max():.1f}%")

# Footer
st.divider()
st.caption("🚀 Tariff Dashboard | Data updates daily at 00:00 GMT | Sample data showing 2018-2025 trends")
