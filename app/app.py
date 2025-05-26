from flask import Flask, request, jsonify
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# SageMaker expects this endpoint for inference
@app.route("/invocations", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        review = data.get("review", "")

        if not review:
            return jsonify({"error": "Missing 'review' field"}), 400

        transformed = vectorizer.transform([review])
        prediction = model.predict(transformed)[0]

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional: Health check route
@app.route("/ping", methods=["GET"])
def ping():
    return "OK", 200

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
