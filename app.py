import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = ""
ENDPOINT_URL = ""

@app.route("/ebay/account-deletion", methods=["GET", "POST"])
def account_deletion():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code", "")
        combined = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
        hash_response = hashlib.sha256(combined.encode()).hexdigest()
        return jsonify({"challengeResponse": hash_response})
    return "",200

if __name__ == "__main__":
    app.run()
