import pandas as pd
import numpy as np

df=pd.read_csv(filepath_or_buffer='tmp/TG_STAID000100.txt',skiprows=20,parse_dates='    DATE')
df.columns
df['TG']=df['   TG'].mask(df['   TG']==-9999,np.nan)
df['TG'].hist()
df['TG'].plot(x='    DATE',y='TG',figsize=(15,3))
df.loc[df['   TG']==-9999]['    DATE']