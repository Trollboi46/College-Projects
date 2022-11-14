import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import csv
from datetime  import datetime
import numpy as np
header=['Time']
df=pd.read_csv('time.csv')

df["DateTime"] = df["Time"]
df["DateTime"]=pd.to_datetime(df["DateTime"])
df["DateTime"]=df["DateTime"].diff()

df['DateTime'] = df['DateTime'].shift(-1)
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
df['Time'] = df['Time'].dt.strftime('%Y-%m-%d %H-%M')
df['DateTime']=df.DateTime.astype('timedelta64[s]')

print(df['DateTime'].mean())
y=df.DateTime
x=df.Time
plt.ylabel("Time in seconds")
plt.xlabel("Date")
plt.plot(x,y,marker='o')
plt.show()
