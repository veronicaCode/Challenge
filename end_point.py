from flask import request, Flask, render_template, Response, jsonify, json
import json
import check
from balanced_diet import RequestDiet

app = Flask(__name__)
get_diet = RequestDiet()


@app.route("/")
@app.route("/index")
def index():
    return jsonify({"Data_format": {"gender": "Female/Male", "ages": "30"}}), 200

@app.route("/diet", methods=["GET"])
def diet():
    if not check.is_valid_key(request.args):
        return jsonify({"error":"invalid input format."}), 400
    elif not check.is_valid_data(request.args):
        return jsonify({"error": "Invalid data."}), 400

    query_data = check.wrapper(request.args)
    
    return jsonify(get_diet.request(json.dumps(query_data))), 200
