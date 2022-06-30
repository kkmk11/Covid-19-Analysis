import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
import datetime
data=pd.read_csv(r"D:\IFS\Corona Virus\country_wise_latest.csv")  #paste the path of the country_wise_latest.csv file dataset for further accessing
name=input("Enter the Country Name : ")
x=data[data.Region==name]["Confirmed"].values[0]
y=data[data.Region==name]["Recovered"].values[0]
z=data[data.Region==name]["Deaths"].values[0]
print("\nConfirmed : ",x)
print("Recovered : ",y)
print("Deaths : ",z)
represent=input("\na)Bar Graph\nb)Pie Chart\n(a) or (b) : ")
if(represent=='a'):
    plt.bar(["Confirmed"],x,color="g",label="Confirmed")
    plt.bar(["Recovered"],y,color="yellow",label="Recovered")
    plt.bar(["Deaths"],z,color="r",label="Deaths")
    plt.title(name)
    d=datetime.datetime.now()
    plt.ylabel("Population effected with Covid-19")
    plt.xlabel(d.strftime("%x"))
    plt.legend()
if(represent=='b'):
    col=["g","yellow","r"]
    lab=["Confirmed","Recovered","Deaths"]
    plt.pie([x,y,z],colors=col,labels=lab,explode=(0,0,0.5),startangle=180,autopct="%1.1f%%",shadow="True")
    plt.title(name)
plt.show()