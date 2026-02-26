import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import base64
from datetime import datetime

st.set_page_config(page_title="Spotify Analytics", layout="wide", page_icon="🎵")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #0E0E0E 0%, #1A1A1A 100%);
        color: white;
    }
    div[data-testid="stMetric"] {
        background: rgba(45, 45, 45, 0.8);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-weight: 700;
    }
    .stMetric label {
        color: #B3B3B3 !important;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #1DB954 !important;
        font-size: 32px !important;
    }
    hr {
        border-color: #1DB954 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_str = f"{client_id}:{client_secret}"
    auth_base64 = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        'Authorization': f'Basic {auth_base64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    
    try:
        response = requests.post(auth_url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()['access_token'], None
    except Exception as e:
        return None, str(e)

def get_top_tracks(token, limit=50):
    playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'limit': limit, 'market': 'US'}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        tracks = []
        for idx, item in enumerate(data['items'][:limit], 1):
            track = item['track']
            if track:
                tracks.append({
                    'Rank': idx,
                    'Song': track['name'],
                    'Artist': ', '.join([a['name'] for a in track['artists']]),
                    'Album': track['album']['name'],
                    'Popularity': track['popularity'],
                    'Duration': f"{track['duration_ms']//60000}:{(track['duration_ms']%60000)//1000:02d}",
                    'Release': track['album']['release_date']
                })
        return pd.DataFrame(tracks), None
    except Exception as e:
        return None, str(e)

def get_top_artists(token):
    playlist_ids = ["37i9dQZEVXbMDoHDwVN2tF", "37i9dQZEVXbNG2KDcFcKOF"]
    all_artists = {}
    
    for pid in playlist_ids:
        url = f"https://api.spotify.com/v1/playlists/{pid}/tracks"
        headers = {'Authorization': f'Bearer {token}'}
        params = {'limit': 50, 'market': 'US'}
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            
            for item in response.json()['items']:
                if item['track']:
                    for artist in item['track']['artists']:
                        if artist['id'] not in all_artists:
                            all_artists[artist['id']] = {'name': artist['name'], 'count': 1}
                        else:
                            all_artists[artist['id']]['count'] += 1
        except:
            continue
    
    top_ids = [aid for aid, _ in sorted(all_artists.items(), key=lambda x: x[1]['count'], reverse=True)[:10]]
    
    if not top_ids:
        return None, "No data"
    
    url = "https://api.spotify.com/v1/artists"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'ids': ','.join(top_ids)}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        artists = []
        for artist in response.json()['artists']:
            artists.append({
                'Artist': artist['name'],
                'Followers': artist['followers']['total'] / 1_000_000,
                'Popularity': artist['popularity'],
                'Genres': ', '.join(artist['genres'][:2]) if artist['genres'] else 'N/A'
            })
        return pd.DataFrame(artists), None
    except Exception as e:
        return None, str(e)

def get_new_releases(token, limit=20):
    url = "https://api.spotify.com/v1/browse/new-releases"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'limit': limit, 'country': 'US'}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        releases = []
        for album in response.json()['albums']['items']:
            releases.append({
                'Album': album['name'],
                'Artist': ', '.join([a['name'] for a in album['artists']]),
                'Release': album['release_date'],
                'Tracks': album['total_tracks'],
                'Type': album['album_type'].title()
            })
        return pd.DataFrame(releases), None
    except Exception as e:
        return None, str(e)

# Get credentials
try:
    client_id = st.secrets["spotify"]["client_id"]
    client_secret = st.secrets["spotify"]["client_secret"]
    from_secrets = True
except:
    st.sidebar.title("🔐 Spotify API")
    st.sidebar.info("Add credentials in app secrets or enter below")
    client_id = st.sidebar.text_input("Client ID")
    client_secret = st.sidebar.text_input("Client Secret", type="password")
    from_secrets = False

# Main UI
st.title("🎵 Spotify Live Analytics")
st.caption(f"📊 {datetime.now().strftime('%B %d, %Y - %I:%M %p')}")
st.divider()

# Auth
if from_secrets:
    if 'token' not in st.session_state:
        with st.spinner("🔐 Connecting..."):
            token, error = get_spotify_token(client_id, client_secret)
            if token:
                st.session_state['token'] = token
                st.session_state['auth'] = True
            else:
                st.error(f"❌ Failed: {error}")
                st.stop()
else:
    if st.sidebar.button("🔄 Connect", type="primary"):
        if client_id and client_secret:
            with st.spinner("Authenticating..."):
                token, error = get_spotify_token(client_id, client_secret)
                if token:
                    st.session_state['token'] = token
                    st.session_state['auth'] = True
                    st.sidebar.success("✅ Connected!")
                    st.rerun()
                else:
                    st.sidebar.error(f"❌ {error}")
        else:
            st.sidebar.error("⚠️ Enter credentials")
    
    if st.session_state.get('auth'):
        st.sidebar.success("🟢 Connected")
    else:
        st.sidebar.warning("🔴 Not Connected")

if not st.session_state.get('auth'):
    st.warning("⚠️ Connect to Spotify API")
    st.info("Get credentials from https://developer.spotify.com/dashboard")
    st.stop()

token = st.session_state['token']

# Fetch data
with st.spinner("📡 Loading data..."):
    df_tracks, _ = get_top_tracks(token, 50)
    df_artists, _ = get_top_artists(token)
    df_releases, _ = get_new_releases(token, 20)

# Metrics
c1, c2, c3, c4 = st.columns(4)
if df_tracks is not None:
    c1.metric("Tracks", len(df_tracks), f"⭐ {df_tracks['Popularity'].mean():.0f}")
else:
    c1.metric("Tracks", "Error", "⚠️")

if df_artists is not None:
    c2.metric("Artists", len(df_artists), f"📈 {df_artists['Followers'].mean():.1f}M")
else:
    c2.metric("Artists", "Error", "⚠️")

if df_releases is not None:
    c3.metric("Releases", len(df_releases), "🆕")
else:
    c3.metric("Releases", "Error", "⚠️")

c4.metric("Status", "Live", "✅")

st.write("")

# Chart
if df_tracks is not None:
    st.write("### 📈 Popularity Trend")
    fig = px.area(df_tracks, x='Rank', y='Popularity', color_discrete_sequence=['#1DB954'])
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(30,30,30,0.3)',
        font=dict(color="white"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        margin=dict(l=40, r=40, t=20, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)

# 3 columns
left, mid, right = st.columns(3)

with left:
    st.write("### 🎤 Artists")
    if df_artists is not None:
        fig = px.bar(df_artists.sort_values('Followers'), y='Artist', x='Followers',
                     orientation='h', color='Popularity',
                     color_continuous_scale=['#2D2D2D', '#1DB954'])
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(30,30,30,0.3)',
            font=dict(color="white", size=10),
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

with mid:
    st.write("### 🎵 Songs")
    if df_tracks is not None:
        top10 = df_tracks.head(10)
        fig = px.bar(top10, x='Song', y='Popularity',
                     color='Popularity',
                     color_continuous_scale=['#FF6B6B', '#FFC837', '#1DB954'])
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(30,30,30,0.3)',
            font=dict(color="white", size=9),
            showlegend=False,
            xaxis=dict(tickangle=-45),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

with right:
    st.write("### 🎼 Genres")
    if df_artists is not None:
        genres = []
        for g in df_artists['Genres']:
            if g != 'N/A':
                genres.extend([x.strip() for x in g.split(',')])
        if genres:
            counts = pd.Series(genres).value_counts().head(8)
            fig = go.Figure(data=[go.Pie(
                labels=counts.index,
                values=counts.values,
                hole=0.5,
                marker=dict(colors=['#1DB954', '#FFC837', '#FF6B6B', '#4ECDC4',
                                   '#9B59B6', '#E67E22', '#3498DB', '#95A5A6'])
            )])
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color="white", size=10),
                legend=dict(orientation="h", y=-0.1),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

# Tables
st.write("### 🏆 Top 50 Tracks")
if df_tracks is not None:
    st.dataframe(
        df_tracks,
        use_container_width=True,
        height=500,
        column_config={
            "Rank": st.column_config.NumberColumn("🏆", format="%d"),
            "Popularity": st.column_config.ProgressColumn("⭐", min_value=0, max_value=100)
        }
    )

st.write("### 🆕 New Releases")
if df_releases is not None:
    st.dataframe(df_releases, use_container_width=True, height=400)

# Footer
st.divider()
f1, f2, f3 = st.columns(3)
f1.caption("🎵 Spotify API")
f2.caption(f"🔄 {datetime.now().strftime('%I:%M %p')}")
if f3.button("🔄 Refresh"):
    st.rerun()