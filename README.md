# 🎵 Spotify 2025 Streaming Analytics Dashboard

![Spotify Dashboard Banner](https://img.shields.io/badge/Spotify-2025-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

An interactive, real-time web application built with **Python**, **Streamlit**, and **Plotly** to visualize live Spotify streaming data. This project replicates a professional Power BI-style dashboard with a modern "Glass Morphism" design and connects directly to Spotify's Web API for live data.

---

## 🚀 Live Demo
**https://spotify-2025-dashboard-adpkbnzbmtru9jcyd33llw.streamlit.app/**

---

## ✨ Key Features
* **Live Data:** Real-time connection to Spotify Web API for current Top 50 tracks
* **KPI Overview:** Live metrics for Top Tracks, Artists, and New Releases
* **Interactive Charts:** Dynamic visualizations with Plotly (popularity trends, genre distribution)
* **Artist Insights:** Top 10 artists ranked by followers and popularity
* **New Releases:** Latest album releases from Spotify
* **Premium UI:** Custom CSS with dark theme, glass morphism effects, and Spotify brand colors

---

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/) (Python Framework)
- **Data Visualization:** [Plotly Express](https://plotly.com/python/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
- **API Integration:** Spotify Web API (Client Credentials Flow)
- **Styling:** Custom CSS (Glass Morphism & Spotify Brand Guidelines)

---

## 📂 Project Structure
```text
├── spotify_dashboard.py    # Main Streamlit application with Spotify API integration
├── requirements.txt        # Python dependencies (streamlit, plotly, pandas, requests)
├── .gitignore             # Git ignore file (excludes secrets and cache)
└── README.md              # Project documentation (this file)
```

---

## 🔑 Setup & Installation

### Prerequisites
- Python 3.9 or higher
- Spotify Developer Account (free)

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Get Spotify API Credentials**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Add Redirect URI: `http://127.0.0.1:8501`
   - Copy your Client ID and Client Secret

4. **Run the app**
```bash
streamlit run spotify_dashboard.py
```

5. **Enter credentials** in the sidebar when prompted

---

## ☁️ Deployment (Streamlit Cloud)

The app is deployed on Streamlit Cloud with credentials stored securely in secrets.

### Deploy Your Own:
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Create new app from your repository
4. Add secrets in app settings:
```toml
[spotify]
client_id = "your_client_id"
client_secret = "your_client_secret"
```

---

## 📊 Data Sources

- **Top 50 Global Tracks**: Spotify's official "Top 50 - Global" playlist
- **Artist Data**: Aggregated from multiple popular playlists
- **New Releases**: Spotify's Browse API (new albums endpoint)
- **Genre Distribution**: Derived from artist genre tags

---

## 🎨 Design Features

- **Color Scheme**: Spotify Green (#1DB954), Dark backgrounds (#0E0E0E), Power BI Yellow (#FFC837)
- **Glass Morphism**: Semi-transparent cards with backdrop blur
- **Responsive Layout**: Multi-column layouts with Streamlit columns
- **Interactive Elements**: Hover effects, progress bars, live data refresh

---

## 🔒 Security

- API credentials stored in Streamlit secrets (not in code)
- `.gitignore` prevents accidental credential commits
- Client Credentials Flow (no user authentication required)

---

## 📝 License

MIT License - feel free to use this project for learning or personal use.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 📧 Contact

**Your Name** - [Your GitHub](https://github.com/ShubhamSarje)

Project Link: [https://github.com/ShubhamSarje/https://github.com/ShubhamSarje/Spotify-2025-Dashboard](https://github.com/ShubhamSarje/https://github.com/ShubhamSarje/Spotify-2025-Dashboard)

---

⭐ **Star this repo if you found it helpful!**
