from flask import Flask, request, render_template
import pickle

# Buat aplikasi Flask
app = Flask(__name__)

# Muat model yang telah dilatih dari file .pkl
with open('model.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        prediction = clf.predict(data)
        result = "not spam" if prediction[0] == 0 else "spam"
        return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
