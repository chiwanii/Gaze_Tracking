import pandas as pd
import numpy as np
import pyproj
import folium


df = pd.read_csv("./Gazetracking/t1.csv",
                 encoding='cp949',
                 usecols=['x','y'])


df['ÁÂÇ¥Á¤º¸(x)'] = pd.to_numeric(df['ÁÂÇ¥Á¤º¸(x)'], errors="coerce")
df['ÁÂÇ¥Á¤º¸(y)'] = pd.to_numeric(df['ÁÂÇ¥Á¤º¸(y)'], errors="coerce")

df = df.dropna()
df.index=range(len(df))
df.tail()
