from flask import Flask, jsonify
from scrapers.united_scraper import get_united_offers

app = Flask(__name__)

@app.route("/united")
def united():
    offers = get_united_offers()
    return jsonify({"United MileagePlus": offers})
@app.route("/delta")
def delta():
    from scrapers.delta_scraper import scrape_delta
    try:
        offers = scrape_delta()
        return jsonify({"delta_skymiles": offers})
    except Exception:
        return jsonify({"delta_skymiles": []})

@app.route("/")
def home():
    return "MileScout backend is live!"

if __name__ == "__main__":
    app.run(debug=False)
