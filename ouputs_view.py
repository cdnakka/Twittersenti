import pandas as pd
from os.path import join as pjoin
Data_path='data'

df=pd.read_csv(pjoin('data','test_100jenasena.csv'))
print(df.head())
