from flask import Flask, jsonify
from scrapers.delta_scraper import scrape_delta
from scrapers.united_scraper import scrape_united
import os

app = Flask(__name__)

@app.route("/delta")
def delta():
    try:
        print("🔄 Delta route hit")
        result = scrape_delta()
        print(f"✅ Delta result: {result}")
        return jsonify(result)
    except Exception as e:
        print(f"❌ Error in /delta: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/united")
def united():
    try:
        print("🔄 United route hit")
        result = scrape_united()
        print(f"✅ United result: {result}")
        return jsonify(result)
    except Exception as e:
        print(f"❌ Error in /united: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/all")
def all_airlines():
    combined = {}
    for airline, scraper in {
        "Delta SkyMiles": scrape_delta,
        "United MileagePlus": scrape_united
    }.items():
        try:
            print(f"🔍 Scraping {airline}")
            combined[airline] = scraper().get(list(scraper().__dict__.keys())[0], [])
        except Exception as e:
            print(f"❌ Failed to scrape {airline}: {e}")
            combined[airline] = []
    return jsonify(combined)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
