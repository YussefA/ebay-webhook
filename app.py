import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = "djoijoijfhwuqlkvoidhfosoidjhfohosknohpobpxqar"
ENDPOINT_URL = "https://ebay-webhook-jdvg.onrender.com"

@app.route("/ebay/account-deletion", methods=["GET", "POST"])
def account_deletion():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code", "")
        combined = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
        hash_response = hashlib.sha256(combined.encode()).hexdigest()
        return jsonify({"challengeResponse": hash_response})
    return "",200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
