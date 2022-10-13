
import numpy as np
from fastapi import FastAPI
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pydantic import BaseModel


app=FastAPI()
@app.get('/')
def index():
    return{'message':'Hello World'}
class request_body(BaseModel):
    Weight: float
    Length3: float
    Height: float
    Width: float


dataset=pd.read_csv("Fish.csv")
dataset.head()
dataset=dataset.drop(['Length1','Length2'],axis=1)
dataset.head(3)
X=dataset.iloc[:,0:5].values
X=X[:,1:]
Y=dataset.iloc[:,0].values
X_train,X_test, Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=0)
regression=LogisticRegression()
regression.fit(X_train,Y_train)

@app.post('/predict')
def predict(data: request_body):
    test_data=[[
        data.Weight,
        data.Length3,
        data.Height,
        data.Width
    ]]
    Y_pred= regression.predict(test_data)[0]
    return Y_pred
