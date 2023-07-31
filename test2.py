import pandas as pd
import numpy as np
import pyproj
import folium


df = pd.read_csv("./Gazetracking/t1.csv",
                 encoding='cp949',
                 usecols=['x','y'])


df['��ǥ����(x)'] = pd.to_numeric(df['��ǥ����(x)'], errors="coerce")
df['��ǥ����(y)'] = pd.to_numeric(df['��ǥ����(y)'], errors="coerce")

df = df.dropna()
df.index=range(len(df))
df.tail()
