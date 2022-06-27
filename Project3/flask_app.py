from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('./model/model.pkl', 'rb'))

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/predict')
def main():
    return render_template('predict.html')

@app.route('/result', methods=['Get','POST'])
def home():
    data1 = request.form.get('hp')
    data2 = request.form.get('attack')
    data3 = request.form.get('defence')
    data4 = request.form.get('sa')
    data5 = request.form.get('sd')
    data6 = request.form.get('speed')
    data7 = request.form.get('sum')
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)