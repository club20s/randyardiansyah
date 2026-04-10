from flask import Flask, render_template
import os

app = Flask(__name__)

# ============================================
# CASE STUDIES DATA
# ============================================

case_studies = [
    {
        "title": "Skripsi IT - Text To Image",
        "category": "AI & Programming",
        "role": "Developer",
        "year": "2024",
        "image": "/static/images/02randy.jpeg",
        "description": "Pengembangan sistem text-to-image menggunakan Stable Diffusion API. Project ini mengeksplorasi bagaimana AI dapat memahami prompts bahasa natural dan menghasilkan visual yang konsisten. Implemented di Google Colab dengan Python untuk accessibility dan reproducibility.",
        "link": "https://colab.research.google.com/drive/1TpDNeSrHazXwYj8acuhk3JMOpUKoDRtb"
    },
    {
        "title": "Fashion Editorial",
        "category": "Photography",
        "role": "Photographer & Art Director",
        "year": "2023",
        "image": "/static/images/01randy.jpeg",
        "description": "Kolaborasi dengan brand lokal untuk menciptakan editorial fashion yang menggabungkan estetika minimalisme dengan lighting dramatis. Konsep visual berfokus pada texture, color grading, dan storytelling yang kuat dalam setiap frame.",
        "link": "#"
    },
    {
        "title": "Sistem Visual Brand",
        "category": "Graphic Design",
        "role": "Designer & Brand Strategist",
        "year": "2024",
        "image": "/static/images/05randy.jpeg",
        "description": "Pengembangan comprehensive visual identity system yang mencakup typography, color palette, iconography, dan design patterns. System dirancang untuk scalability dan konsistensi across all touchpoints, dari print hingga digital.",
        "link": "https://scrapbox.io/WarenBergg1995/"
    },
    {
        "title": "Data Landscape Visualization",
        "category": "Data Visualization",
        "role": "Data Viz Designer & Researcher",
        "year": "2024",
        "image": "/static/images/04randy.png",
        "description": "Visualisasi interaktif yang mengeksplorasi relationship antara natural landscapes dan data. Project menggunakan teknologi web dan creative coding untuk membuat pengalaman yang immersive dan educational tentang environmental data.",
        "link": "#"
    }
]

# ============================================
# CLIENTS & JOURNEY
# ============================================

clients = [
    "Universitas Handayani Makassar",
    "Stable Diffusion",
    "Studi Independen",
    "Makassar Developer Enthusiast",
    "Google Colab",
    "Teknik Informatika (2020 - 2025)",
    "AI Text To Image (2024)",
    "Camp RuangGuru & LearningX (2024)",
    "Web Design (2023 - Now)",
    "python"
]

# ============================================
# FLASK ROUTES
# ============================================

@app.route("/")
def index():
    """Home page dengan portfolio grid"""
    return render_template("index.html", clients=clients)

@app.route("/theory")
def theory():
    """Halaman Theory dan Research"""
    return render_template("theory.html")

@app.route("/case-studies")
def case_studies_page():
    """Halaman Case Studies dengan detailed project information"""
    return render_template("case-studies.html", case_studies=case_studies)

# DITHER ROUTE
@app.route("/dither")
def dither():
    return render_template("dither.html")

# ============================================
# DEVELOPMENT CONFIG
# ============================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

