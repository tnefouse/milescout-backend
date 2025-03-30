from flask import Flask, jsonify
from scrapers.united_scraper import scrape_united
from scrapers.delta_scraper import scrape_delta

app = Flask(__name__)

@app.route("/")
def home():
    return "MileScout Backend is Live"

@app.route("/united")
def united():
    return scrape_united()

@app.route("/delta")
def delta():
    return scrape_delta()

@app.route("/all")
def all_airlines():
    try:
        united_offers = scrape_united()["united_mileageplus"]
    except:
        united_offers = []

    try:
        delta_offers = scrape_delta()["delta_skymiles"]
    except:
        delta_offers = []

    return jsonify({
        "united_mileageplus": united_offers,
        "delta_skymiles": delta_offers
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
