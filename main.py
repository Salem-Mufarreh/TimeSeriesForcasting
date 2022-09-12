import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
plt.style.use('fivethirtyeight')
df = pd.read_csv('Data/PJME_hourly.csv')
df = df.set_index('Datetime')
df.index = pd.to_datetime(df.index)
color_pal = sns.color_palette()
df.plot(style='.', figsize=(15, 5), color=color_pal[0], title='PJME Energy used in MW')
# Test Date
train = df.loc[df.index < '01-01-2015']
test = df.loc[df.index >= '01-01-2015']
fig, ax = plt.subplots(figsize=(15, 5))
train.plot(ax=ax, label="Training Set")
test.plot(ax=ax, label="Test Set")
ax.axvline('01-01-2015', color='black', ls="--")
ax.legend(['Training Set', 'Test Set'])
week = df.loc[(df.index > '01-01-2015') & (df.index < '01-08-2015')].plot()
plt.show()
