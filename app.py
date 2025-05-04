from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
classifier = joblib.load("static\model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        headline = request.form['headline']
        category = predict_category(headline)  # Call predict_category with the headline
        return render_template('index.html', headline=headline, category=category)
    return render_template('index.html', headline=None, category=None)
loaded_classifier = joblib.load("static\model.pkl")

def predict_category(headline):
    #y_pred1 = cv.transform([headline])
    yy = loaded_classifier.predict(y_pred1)  # Load the classifier first
    result = ""
    if yy == [0]:
        result = "Business News"
    elif yy == [1]:
        result = "Tech News"
    elif yy == [2]:
        result = "Politics News"
    elif yy == [3]:
        result = "Sports News"
    elif yy == [4]:
        result = "Entertainment News"

    return result

# Return the predicted category as a string
if __name__ == '__main__':
    app.run(debug=True)
