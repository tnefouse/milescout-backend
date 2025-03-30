from flask import Flask, jsonify
from scrapers.united_scraper import scrape_united
from scrapers.delta_scraper import scrape_delta
import os

app = Flask(__name__)

@app.route('/united')
def united():
    return jsonify(scrape_united())

@app.route('/delta')
def delta():
    return jsonify(scrape_delta())

@app.route('/all')
def all_airlines():
    try:
        united_data = scrape_united()["united_mileageplus"]
    except Exception:
        united_data = []

    try:
        delta_data = scrape_delta()["delta_skymiles"]
    except Exception:
        delta_data = []

    combined = {
        "United MileagePlus": united_data,
        "Delta SkyMiles": delta_data
    }

    return jsonify(combined)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
