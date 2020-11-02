import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestRegressor
plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
df = pd.read_csv("Crop Production With Rainfall.csv")
rain = pd.read_csv("Rainfall Predicted.csv")
data = df.dropna()
print(data.shape)
dis=input("Enter the District Name: ")
state=list(data[data["District_Name"]==dis.upper()]["State_Name"][:1])[0]
season=input("Enter the Season: ")
area_in=input("Enter Area in hectares: ")
s=list(data["Season"].unique())
for x in s:
    if season.title() in x:
        sin=s.index(x)
data_cu=data[data["District_Name"]==dis.upper()][data["Season"]==s[sin]]
data1 = data_cu.drop(["State_Name","Crop_Year"],axis=1)
data_dum = pd.get_dummies(data1)
x = data_dum.drop("Production",axis=1)
y = data_dum[["Production"]]

model = RandomForestRegressor()
model.fit(x,y.values.ravel())

ch=pd.DataFrame()
for crop in list(data_cu["Crop"].unique()):
    t=(x[x["Crop_{}".format(crop)]==1])[:1]
    ch=pd.concat([ch,t])
ch["Area"]=area_in
ch["Rainfall"]=list(rain[rain["State_Name"]==state]["Rainfall"])[0]
predict=model.predict(ch)
crname=data.loc[ch.index]["Crop"]
crdata= {'Crop': list(crname), 
        'Production': list(predict)}
crpro = pd.DataFrame(crdata) 
crpro=crpro.sort_values(by=['Production'], ascending=False)
print(crpro)
fig=plt.figure()
ax = fig.add_axes([0,0,1,1])
tstr='Predicted Production in        District: '+dis.title()+'      Season: '+season.title()
ax.set_title(tstr,fontsize=15)
ax.set_ylabel('Production in Tones', fontsize=14)
ax.set_xlabel('Crop', fontsize=13)
ax.bar(list(crpro["Crop"])[:5], list(crpro["Production"])[:5])
plt.savefig('plot.png', dpi=400, bbox_inches='tight')
im = Image.open('plot.png').show()
