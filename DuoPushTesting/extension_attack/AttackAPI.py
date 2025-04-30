from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/get-verification-code", methods=["GET"])
def get_verification_code():
    return "Hello World :)"

app.run(host="0.0.0.0", port=1313, debug=True)
