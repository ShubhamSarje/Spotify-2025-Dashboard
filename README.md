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
* **Live Data:** Real-time connection to Spotify Web API for current Top 50 Global tracks
* **KPI Overview:** Live metrics for Top Tracks, Popular Artists, and New Releases
* **Interactive Charts:** Dynamic visualizations with Plotly (popularity trends, genre distribution)
* **Artist Rankings:** Top 10 artists ranked by followers and popularity scores
* **New Releases:** Latest album releases from Spotify's catalog
* **Premium UI:** Custom CSS with dark theme, glass morphism effects, and Spotify brand colors (#1DB954)

---

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/) - Python web framework
- **Data Visualization:** [Plotly Express](https://plotly.com/python/) - Interactive charts
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/) - Data processing
- **API Integration:** Spotify Web API (Client Credentials Flow)
- **HTTP Client:** Requests library for API calls
- **Styling:** Custom CSS (Glass Morphism & Spotify Brand Guidelines)

---

## 📂 Project Structure
```text
Spotify-2025-Dashboard/
├── spotify_dashboard.py    # Main Streamlit application with Spotify API integration
├── requirements.txt        # Python dependencies (streamlit, plotly, pandas, requests)
├── .gitignore             # Git ignore file (excludes secrets and cache)
└── README.md              # Project documentation (this file)
```

---

## 🔑 Setup & Installation

### Prerequisites
- Python 3.9 or higher
- Spotify Developer Account (free) - [Sign up here](https://developer.spotify.com/)

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/ShubhamSarje/Spotify-2025-Dashboard.git
cd Spotify-2025-Dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Get Spotify API Credentials**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Click "Create App"
   - Fill in app details:
     - App name: "Spotify Analytics Dashboard"
     - App description: "Personal analytics dashboard"
     - Redirect URI: `http://127.0.0.1:8501`
   - Accept terms and click "Create"
   - Copy your **Client ID** and **Client Secret**

4. **Run the application**
```bash
streamlit run spotify_dashboard.py
```

5. **Enter credentials** in the sidebar when the app opens

---

## ☁️ Deployment on Streamlit Cloud

This app is deployed on Streamlit Cloud with credentials stored securely.

### Deploy Your Own Version:

1. **Fork this repository** on GitHub

2. **Go to [Streamlit Cloud](https://share.streamlit.io)**

3. **Create new app:**
   - Repository: `ShubhamSarje/Spotify-2025-Dashboard` (or your fork)
   - Branch: `main`
   - Main file: `spotify_dashboard.py`

4. **Add secrets** in app settings (⚙️ → Secrets):
```toml
[spotify]
client_id = "your_client_id_here"
client_secret = "your_client_secret_here"
```

5. **Deploy!** The app will automatically build and launch

---

## 📊 Data Sources

All data is fetched in real-time from Spotify Web API:

- **Top 50 Global Tracks**: Spotify's official "Top 50 - Global" playlist (updated daily)
- **Artist Data**: Aggregated from multiple popular playlists and artist endpoints
- **Popularity Scores**: Spotify's proprietary popularity metric (0-100)
- **New Releases**: Spotify's Browse API (new albums endpoint, updated weekly)
- **Genre Distribution**: Derived from artist genre tags via Artists API

### API Endpoints Used:
- `/v1/playlists/{id}/tracks` - Playlist tracks
- `/v1/artists` - Artist details (followers, genres, popularity)
- `/v1/browse/new-releases` - New album releases

---

## 🎨 Design Features

### Color Palette
- **Primary**: Spotify Green (#1DB954)
- **Secondary**: Power BI Yellow (#FFC837)
- **Accent**: Coral (#FF6B6B)
- **Background**: Dark gradient (#0E0E0E → #1A1A1A)
- **Text**: White (#FFFFFF) and Light Gray (#B3B3B3)

### UI Components
- **Glass Morphism Cards**: Semi-transparent panels with backdrop blur
- **Gradient Backgrounds**: Smooth color transitions
- **Interactive Charts**: Hover tooltips, zoom, and pan functionality
- **Progress Bars**: Visual popularity indicators
- **Responsive Layout**: Multi-column layouts with Streamlit columns
- **Custom Metrics**: KPI cards with delta indicators

---

## 📈 Dashboard Sections

1. **Header KPIs**: Total tracks, artists, new releases, and API status
2. **Popularity Trend Chart**: Area chart showing Top 50 track popularity distribution
3. **Top Artists**: Horizontal bar chart ranked by follower count
4. **Top Songs**: Vertical bar chart of most popular tracks
5. **Genre Distribution**: Donut chart showing genre percentages
6. **Data Tables**: Sortable tables with detailed track and album information

---

## 🔒 Security & Best Practices

- ✅ API credentials stored in Streamlit secrets (never in code)
- ✅ `.gitignore` prevents accidental credential commits
- ✅ Client Credentials Flow (no user authentication required)
- ✅ Environment variables for sensitive data
- ✅ HTTPS-only for production deployment
- ✅ Rate limiting handled by Spotify API

---

## 🚀 Features Roadmap

- [ ] Historical data tracking (store daily snapshots)
- [ ] User authentication for personalized playlists
- [ ] Export data to CSV/Excel
- [ ] More playlist comparisons
- [ ] Audio features analysis (tempo, energy, danceability)
- [ ] Regional trends (country-specific data)

---

## 🐛 Known Issues

- API rate limits may affect data refresh frequency
- Some tracks may have missing data (handled gracefully)
- Genre distribution limited to artist genres (not track-level)

---

## 📝 License

MIT License

Copyright (c) 2025 Shubham Sarje

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact

**Shubham Sarje**

- GitHub: [@ShubhamSarje](https://github.com/ShubhamSarje)
- Project Link: [https://github.com/ShubhamSarje/Spotify-2025-Dashboard](https://github.com/ShubhamSarje/Spotify-2025-Dashboard)
- Live Demo: [https://spotify-2025-dashboard-adpkbnzbmtru9jcyd33llw.streamlit.app/](https://spotify-2025-dashboard-adpkbnzbmtru9jcyd33llw.streamlit.app/)

---

## 🙏 Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) for providing free access to music data
- [Streamlit](https://streamlit.io/) for the amazing Python web framework
- [Plotly](https://plotly.com/) for beautiful interactive visualizations

---

## ⭐ Show Your Support

If you found this project helpful or interesting, please consider giving it a star! ⭐

---

**Built with ❤️ by Shubham Sarje**
