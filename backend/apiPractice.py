from flask import Flask, request, jsonify
from logic import add, subtract
#Intilaizies flask application
app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    a = data.get("a")
    b = data.get("b")
    
    res = add(a,b)
    print(res)
    return jsonify({"OK": res})

@app.route("/subtract", methods=["POST"])
def subtract_numbers():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    
    a = data.get("a")
    b = data.get("b")

    result = subtract(a,b)
    print(result)
    return jsonify({"OK": result})



if __name__ == '__main__':
    app.run(debug=True)
    