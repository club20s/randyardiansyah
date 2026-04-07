from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/theory")
def theory():
    return render_template("theory.html")

@app.route("/case-studies")
def case_studies_page():
    return render_template("case-studies.html")

@app.route("/dither")
def dither():
    return render_template("dither.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
