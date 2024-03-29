from flask import Flask, request, jsonify
import util

app = Flask(__name__)


# @app.route('/')
# def usr():
#     return "Hello"


@app.route('/', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form.get('image_data')

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Footballer Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000, debug=True)
