from flask import Flask , jsonify
from flask import Flask, request, make_response, redirect, render_template
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
CORS(app)
@app.route('/')
@app.route("/ConsumingData",methods=['POST'])
def index():
    Data = request.data
    ByteToString = json.loads(Data)
    StringToJson = json.dumps(ByteToString,indent=4)
    with open('data.json',w) as outfile:
        outfile.write(StringToJson)
    df = pd.read_json(StringToJson)
    df.to_csv("Dhanush".csv)
    print('Successful')
    import pandas as pd
    import numpy as np
    df=pd.read_csv("cleaned_milk_data_data.csv",index_col='DATE',parse_dates=True)
    df=df.dropna()
    print('Shape of data',df.shape)
    df.head(20) 
    df['Flavoured Milk'].plot(figsize=(12,5))
    print(df.shape)
    train=df.iloc[:-30]
    test=df.iloc[-30:]
    print(train.shape,test.shape)
    from statsmodels.tsa.arima.model import ARIMA
    model=ARIMA(train['Flavoured Milk'],order=(2,0,5))
    model=model.fit()
    model.summary()
    start=len(train)
    end=len(train)+len(test)-1
    pred=model.predict(start=start,end=end,typ='levels').rename('ARIMA Predictions')
    pred.index=df.index[start:end+1]
    print(pred)
    pred.plot(legend=True)
    test['Flavoured Milk'].plot(legend=True)
    test['Raw Milk'].mean()
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    rmse=sqrt(mean_squared_error(pred,test['Flavoured Milk']))
    print(rmse)
    model2=ARIMA(df['Flavoured Milk'],order=(2,0,5))
    model2=model2.fit()
    df.tail()
    index_future_dates=pd.date_range(start='2018-12-30',end='2019-10-01')
    #print(index_future_dates)
    pred=model2.predict(start=len(df),end=len(df)+275,typ='levels').rename('ARIMA Predictions')
    #print(comp_pred)
    pred.index=index_future_dates
    print(pred)
    pred.plot(figsize=(12,5),legend=True)



app.run(debug=True)


