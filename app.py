# app.py
from flask import Flask, render_template
import random
import json

app = Flask(__name__)

# Load quotes from a JSON file
with open("quotes.json", "r") as f:
    quotes = json.load(f)

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
