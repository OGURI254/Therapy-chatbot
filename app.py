from flask import Flask, render_template, request, jsonify
from chat import get_response
import openai

openai.api_key = "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"
app = Flask(__name__)


def index_get():
    return render_template()
# @app.route("/",methods = ["GET"]) // old method

@app.route("/", methods=["GET"])
def index_get():
    return render_template("base.html")


@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message") #in Js i also used message as my key
    # im supposed to check if the message is valid
    res = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0, max_tokens=100)
    # response = get_response(text)
    message = {"answer": res['choices'][0]['text']} #used answer as key object for my json file.
    return jsonify( message)


if __name__ == "__main__":
    app.run(debug=True)
