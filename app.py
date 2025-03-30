from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/united')
def united_offers():
    data = {
        "united_mileageplus": [
            { "store": "sephora.com", "miles_per_dollar": "6x" },
            { "store": "nike.com", "miles_per_dollar": "4x" },
            { "store": "apple.com", "miles_per_dollar": "3x" },
            { "store": "macys.com", "miles_per_dollar": "5x" },
            { "store": "ulta.com", "miles_per_dollar": "7x" }
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)