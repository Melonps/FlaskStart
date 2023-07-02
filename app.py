from flask import Flask, request, send_file
from flask_cors import CORS
from drawsingraph import drawsingraph


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello():
    return "hello"


@app.route("/<name>", methods=["GET"])
def hello_name(name):
    return "hello " + name


@app.route("/getsinimage", methods=["POST"])
def gensinimage():
    angle = request.json.get("angle")
    print(angle)
    print(type(angle))
    drawsingraph(int(angle))
    return send_file("./GeneratedData/sin.png", mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
