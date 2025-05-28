from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__, template_folder="templates")

# Load model and vectorizer
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "tfidf_vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    review = request.form.get("review", "")
    prediction = None

    if review:
        transformed = vectorizer.transform([review])
        prediction = model.predict(transformed)[0]

    return render_template("index.html", review=review, prediction=prediction)

@app.route("/ping", methods=["GET"])
def ping():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
