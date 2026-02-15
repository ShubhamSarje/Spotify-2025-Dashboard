import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Spotify 2025 Analytics", layout="wide")

# --- CUSTOM CSS FOR SPOTIFY LOOK ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(180deg, #0E0E0E 0%, #1A1A1A 100%);
        color: white;
    }
    
    /* Glass Morphism Cards */
    div[data-testid="stMetric"] {
        background: rgba(45, 45, 45, 0.8);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    /* Titles and Headers */
    h1, h2, h3 {
        font-family: 'Circular', sans-serif;
        color: #FFFFFF !important;
    }
    
    /* Spotify Green Highlights */
    .stMetric label {
        color: #B3B3B3 !important;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #1DB954 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA GENERATION ---
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
streaming_data = pd.DataFrame({
    'Month': months,
    'Streams': [2.1, 2.5, 3.2, 3.8, 4.1, 4.5, 5.2, 5.8, 6.1, 6.5, 7.2, 8.0]
})

# --- HEADER SECTION ---
st.title("🎵 Spotify 2025 Streaming Analytics")
st.caption("Annual Performance Report | January - December 2025")
st.divider()

# --- KEY METRICS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Streams", "45.2B", "+15%")
col2.metric("Total Artists", "1.5M", "+5%")
col3.metric("Total Songs", "60M", "+12%")
col4.metric("Avg Streams/Song", "753", "🔥 High")

# --- MAIN VISUALS ---
st.write("### Monthly Streaming Trends 2025")
fig_line = px.area(streaming_data, x='Month', y='Streams', 
                   color_discrete_sequence=['#1DB954'])
fig_line.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="white",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
)
st.plotly_chart(fig_line, use_container_width=True)

# --- BOTTOM ROW ---
left_col, right_col = st.columns(2)

with left_col:
    st.write("### Top 10 Artists")
    artists = pd.DataFrame({
        'Artist': ['Taylor Swift', 'Drake', 'Beyoncé', 'The Weeknd', 'Bad Bunny'],
        'Streams (B)': [3.5, 3.1, 2.8, 2.5, 2.2]
    })
    fig_bar = px.bar(artists, x='Streams (B)', y='Artist', orientation='h',
                     color_discrete_sequence=['#1DB954'])
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_bar, use_container_width=True)

with right_col:
    st.write("### Genre Distribution")
    genres = ['Pop', 'Hip-Hop', 'Rock', 'Electronic', 'Indie']
    values = [30, 25, 20, 15, 10]
    fig_pie = px.pie(values=values, names=genres, 
                     color_discrete_sequence=['#1DB954', '#168B46', '#FFC837', '#FF6B6B', '#00D084'],
                     hole=0.6)
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_pie, use_container_width=True)

# --- TRACK TABLE ---
st.write("### Top 20 Tracks - 2025")
df_tracks = pd.DataFrame({
    'Rank': range(1, 6),
    'Song Name': ['Midnight City', 'Neon Dreams', 'Cyberpunk Love', 'Retro Grade', 'Echoes'],
    'Artist': ['Synth Wave', 'The Future', 'Digital Nomad', 'Bass Drop', 'Vocalist'],
    'Streams': ['1.2B', '1.1B', '1.0B', '950M', '900M']
})
st.table(df_tracks)
