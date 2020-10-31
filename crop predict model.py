import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
df = pd.read_csv("apy.csv")
data = df.dropna()
sum_maxp = data["Production"].sum()
data["percent_of_production"] = data["Production"].map(lambda x:(x/sum_maxp)*100)
print(data.shape)
data1 = data.drop(["District_Name","Crop_Year"],axis=1)
data_dum = pd.get_dummies(data1)
x = data_dum.drop("Production",axis=1)
y = data_dum[["Production"]]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25, random_state=42)
print("x_train :",x_train.shape)
print("x_test :",x_test.shape)
print("y_train :",y_train.shape)
print("y_test :",y_test.shape)

model = RandomForestRegressor()
model.fit(x_train,y_train.values.ravel())
print("Training Done...")

filename = 'rf_model.sav'
joblib.dump(model, filename)

predict = model.predict(x_test)
r = r2_score(y_test,predict)
print("R2score",r)
