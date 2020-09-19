import pandas as pd
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from PIL import Image
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
data=pd.read_csv("apy.csv", header=0)
data=data.dropna()
print("States\n",data["State_Name"].unique())
state=input("Enter the State Name: ")
print("District\n",data[data["State_Name"]==state]["District_Name"].unique())
dis=input("Enter the District Name: ")
print("Season\n",data["Season"].unique())
season=input("Enter the Season: ")
s=list(data["Season"].unique())
for x in s:
    if season.title() in x:
        sin=s.index(x)
d = data[data["District_Name"]==dis.upper()][data["Season"]==s[sin]]["Crop"].unique()
c=[]
p=[]
for crop in d:
    c.append(crop)
    a = data[data["Crop"]==crop][data["District_Name"]==dis.upper()][data["Season"]==s[sin]]["Area"]
    y = data[data["Crop"]==crop][data["District_Name"]==dis.upper()][data["Season"]==s[sin]]["Production"]
    reg=LinearRegression()
    reg.fit(a.values.reshape(-1,1),y.values.reshape(-1,1))
    coeff=(reg.coef_)
    p.append(coeff[0][0])
fig=plt.figure()
ax = fig.add_axes([0,0,1,1])
crname=[]
pr=p.copy()
pr.sort(reverse=True)
for x in pr:
    crname.append(c[p.index(x)])
# for i in range(len(crname)):
#     crname[i]=crname[i][:3]
tstr='Approx Prodction in        District: '+dis.title()+'      Season: '+season.title()
ax.set_title(tstr,fontsize=15)
ax.set_ylabel('Production', fontsize=14)
ax.set_xlabel('Crop', fontsize=13)
ax.bar(crname[:5],pr[:5 ])
plt.savefig('plot.png', dpi=400, bbox_inches='tight')
#plt.show()
im = Image.open('plot.png').show()
    




