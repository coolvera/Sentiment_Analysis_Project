from flask import Flask, request, render_template
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        review_transformed = vectorizer.transform([review])
        prediction = model.predict(review_transformed)[0]
        return render_template('index.html', review=review, prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))  
    app.run(debug=True, host='0.0.0.0', port=port)

