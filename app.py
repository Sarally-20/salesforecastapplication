from flask import Flask , jsonify
from flask import Flask, request, make_response, redirect, render_template
from flask_cors import CORS
from flask import send_file
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
app = Flask(__name__)
CORS(app)
@app.route("/upload",methods=['GET','POST'])
def upload():
        file = request.files['file'].read()
        n=request.form['count']
        per=request.form['period']
        print(file)
        f=open("milk.csv",'wb')
        f.write(file)
        f.close()
        df=pd.read_csv("milk.csv",index_col='DATE',parse_dates=True)
        from statsmodels.tsa.arima.model import ARIMA
        model=ARIMA(df['Flavoured Milk'],order=(2,0,5))
        model=model.fit()
        index_future_dates=pd.date_range(start='2018-12-30',end='2019-10-01')
        pred=model.predict(start=len(df),end=len(df)+275,typ='levels').rename('ARIMA Predictions')
        pred.index=index_future_dates
        plt.figure(figsize=(12,7))
        plt.plot(pred)
        plt.savefig('temp.png')
        return '{"status":"success"}'
@app.route('/image',methods=['GET','POST'])
def image():
        return send_file('temp.png',mimetype='image/png')
app.run(debug=True)