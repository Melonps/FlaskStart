from flask import Flask, request, send_file
from flask_cors import CORS
from lib.drawsingraph import drawsingraph
from lib.drawnameimage import drawnameimage
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # CORSを有効にする


@app.route("/", methods=["GET"])
def hello():
    return "hello"


@app.route("/<name>", methods=["GET"])
def hello_name(name):
    return "hello " + name


@app.route("/getsinimage", methods=["POST"])
def gensinimage():
    angle = request.json.get("angle")  # POSTリクエストからangleパラメータを取得
    print(angle)
    print(type(angle))
    drawsingraph(int(angle))  # angleを整数に変換してdrawsingraph関数を呼び出す
    return send_file("./GeneratedData/sin.png", mimetype="image/png")  # 生成された画像ファイルを送信


@app.route("/getnameimage/<name>", methods=["POST"])
def gennameimage(name):
    drawnameimage(name)  # drawnameimage関数を呼び出す
    return send_file("./GeneratedData/name.png", mimetype="image/png")  # 生成された画像ファイルを送信


@app.route("/convertToMonochrome", methods=["POST"])
def convert_to_monochrome():
    if "image" not in request.files:
        return "No image file provided", 400
    image_file = request.files["image"]
    image = Image.open(image_file)

    # 画像をモノクロに変換する処理
    monochrome_image = image.convert("L")

    # モノクロ画像をバイナリデータに変換する
    output = io.BytesIO()
    monochrome_image.save(output, format="PNG")
    output.seek(0)

    return send_file(output, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
