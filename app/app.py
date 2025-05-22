from flask import Flask, request, render_template
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
model = joblib.load('../model/model.pkl')
vectorizer = joblib.load('../model/tfidf_vectorizer.pkl')

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
    app.run(debug=True)
