# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:49:03 2020

@author: Krist
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
# =============================================================================
# data = pd.read_csv(r'C:\Users\Krist\OneDrive\desktop\CPP\final\CUR-CNY.csv')
# data = data.sort_values(by = 'DATE')
# 
# 
# data[-365:].to_csv(r'C:\Users\Krist\OneDrive\desktop\CPP\final\CUR-CNY2019.csv')
# =============================================================================

# =============================================================================
# =============================================================================
#data = pd.read_csv(r'C:\Users\Krist\OneDrive\desktop\CPP\final\CUR-CNY2019.csv')
#data['DATE'] = data['DATE'].apply(lambda x: datetime.strptime(x,'%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%fS'))
# data = data.set_index(data['DATE'])
#data.to_csv(r'C:\Users\Krist\OneDrive\desktop\CPP\final\CUR-CNY2019.csv')
# =============================================================================
# =============================================================================
#%%
data = pd.read_csv(r'C:\Users\Krist\OneDrive\desktop\CPP\final\CUR-CNY2019.csv')
data['rsi'] = np.nan
for i in range(len(data)):
    if len(data[:(i+1)]) >= 15:
        prices = data[i-14:i+1]['RATE']
        pc = list((prices.diff()/prices)[1:])
        gain = np.mean([p for p in pc if p>=0])
        loss = np.mean([p for p in pc if p<0])
        rsi = 100-(100/(1+gain/abs(loss)))
        data.loc[i,'rsi'] = rsi
print(np.nanpercentile(data['rsi'],30))
print(np.nanpercentile(data['rsi'],70))

idx1 = data.loc[data['rsi']<30].index
idx2 = data.loc[data['rsi']>50].index
data['signal'] = 0
data.loc[idx1,'signal'] = 1
data.loc[idx2,'signal'] = -1
data['position_change'] = data['signal'] * 100
data['position'] = data['position_change'].cumsum()
data['cash'] = 10000-(data['position_change'] * data['RATE']).cumsum()
data['holdings'] = data['position'] * data['RATE']
data['total'] = data['holdings'] + data['cash']
plt.plot(data['total'])

#To convert date to epoch time
utc_time = data['DATE'].apply(lambda x:datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
data['epoch_time'] = utc_time.apply(lambda x: (x- datetime(1970,1,1)).total_seconds())