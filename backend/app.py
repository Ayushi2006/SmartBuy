# app.py
from flask import Flask, request, jsonify
from assistant import shopping_assistant

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    products = shopping_assistant(query)
    return app.response_class(
        response=json.dumps(products, indent=4),
        status=200,
        mimetype='application/json'
    )

if __name__ == "__main__":
    import json
    app.run(debug=True)