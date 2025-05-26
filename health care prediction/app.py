# flask app
from flask import Flask, request, jsonify
import pickle
from flask import render_template

app = Flask(__name__)
# load the model, scaler, and encoder
with open("result/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("result/label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")


# post request to predict
@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    age = int(data.get("age"))
    sex = data.get("sex")
    bmi = float(data.get("bmi"))
    children = int(data.get("children"))
    smoker = data.get("smoker")
    region = data.get("region")

    # convert categorical variables to numerical
    smoker = encoder.transform([smoker])[0]

    # make prediction
    prediction = model.predict([[age, smoker]])
    return render_template(
        "index.html",
        prediction=round(prediction[0], 2),
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
