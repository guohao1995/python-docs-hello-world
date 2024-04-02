from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Github"

@app.route("/api/headers")
def headers():
    json_res = jsonify({ "message": "Adding custom header.." })
    res = make_response(json_res)
    res.headers['X-Frame-Options'] = 'DENY'
    return res
