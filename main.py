from flask import Flask, request, jsonify

app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Please provide both 'a' and 'b'"}), 400

    return jsonify({
        "a": a,
        "b": b,
        "sum": a + b
    }), 200



if __name__ == '__main__':
    app.run(debug=True)