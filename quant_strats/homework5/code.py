# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:08:06 2020

@author: Krist
"""

import pandas as pd
import numpy as np
import datetime
import random
import quandl
import functools
import matplotlib.pyplot as plt

@functools.lru_cache(maxsize=1600)
def fetch_quandl(my_data_items, start_date=None, returns="pandas"):
    qdata = quandl.get(list(my_data_items), returns=returns, 
                      trim_start=start_date,
                      api_key="khzKyrGRmxZen9BA5h9a")
    return qdata
def fun(x):
    if '.' in x:
        return False
    else:
        return True

# Here is how I selected the 200+ tickers. 
# =============================================================================
# eod_ticker = pd.read_csv(r'C:\Users\Krist\OneDrive\desktop\quant strategies\homework4\ticker_list.csv')
# eod_ticker = eod_ticker.loc[(eod_ticker['Last Trade Date'] == '2020-05-01') & \
#                             (eod_ticker['Ticker'].apply(lambda x: fun(x)) == True) & \
#                             (eod_ticker['Exchange'] == 'NYSE') | (eod_ticker['Exchange'] == 'NASDAQ')]
# tickers = random.sample(list(eod_ticker['Ticker']),350)
# tickers.append('SPY')
# pd.Series(tickers).to_csv(r'C:\Users\Krist\OneDrive\desktop\quant strategies\hw5\tickers.csv')
# =============================================================================

# get eod data and daily returns.
tickers = pd.read_csv(r'C:\Users\Krist\OneDrive\desktop\quant strategies\hw5\tickers.csv',header = None)
tickers = list(tickers[tickers.columns[1]])

tablenames = ['EOD/'+t for t in tickers]
tablenames = tuple(tablenames)
names = ['EOD/'+t+' - Adj_Close' for t in tickers]


data_df = fetch_quandl(tablenames, start_date = datetime.date(2016,1,4)).loc[:, names]
data_df.columns = tickers

ret_df = data_df.diff().div(data_df).iloc[1:]
ret_df = ret_df.dropna(axis = 1)
ticker = list(ret_df.columns)


# Regressions
times = [pd.Timestamp('2018-06-29'),pd.Timestamp('2018-12-31'),pd.Timestamp('2019-06-28'),pd.Timestamp('2019-11-29')]
#oos window_beta c
pd_oos_beta = pd.DataFrame()
for i in range(len(times)):
    pd_oos_covs = ret_df[times[i]:][1:21].cov()[ticker].xs('SPY')
    pd_oos_beta_seg = pd_oos_covs/pd_oos_covs.loc['SPY']
    pd_oos_beta[times[i]] = pd_oos_beta_seg[:-1]
    
#lambda = 0.05,0.1,0.2,0.4,0.5,1
lambdas = [0.05,0.1,0.2,0.4,0.5,1]
for lm in lambdas:
    alpha = 1-np.exp(-lm) 
    pd_ew_covs = ret_df.ewm(alpha, adjust=True).cov()[ticker].xs('SPY', level=1)
    
    #ewma beta for all the times and all tickers
    pd_ew_beta = pd_ew_covs[ticker[:-1]].div(pd_ew_covs.SPY, axis = 0)
    #ewma beta for the specific four times
    pd_ew_beta_4 = pd.DataFrame()
    for i in range(len(times)):
        pd_ew_beta_4[times[i]] = pd_ew_beta.loc[times[i],:]
        
    #window_beta b for the specific four times
    window = int(2/lm)
    
    pd_bc_beta = pd.DataFrame()
    for i in range(len(times)):
        pd_bc_covs = ret_df[:times[i]][-window:].cov()[ticker].xs('SPY')
        pd_bc_beta_seg = pd_bc_covs/pd_bc_covs.loc['SPY']
        pd_bc_beta[times[i]] = pd_bc_beta_seg[:-1]
    
    #plot beta and b for tickers in different times
    for i in range(len(times)):
        plt.figure()
        plt.plot(pd_ew_beta_4[times[i]])
        plt.plot(pd_bc_beta[times[i]])
        #plt.plot(pd_oos_beta[times[i]])
        plt.xticks([])
        plt.title("lambda="+str(lm)+" time="+str(times[i]))
    
    #calculate MAE and RMSE for out of sample comparison
    error = pd.DataFrame(index = times,columns = ['mae_ewm','mae_window','rmse_ewm','rmse_window'])
    for i in range(len(times)):
        error.loc[times[i],'rmse_ewm'] = np.mean((pd_oos_beta[times[i]] - pd_ew_beta_4[times[i]])**2)
        error.loc[times[i],'rmse_window'] = np.mean((pd_oos_beta[times[i]] - pd_bc_beta[times[i]])**2)
        error.loc[times[i],'mae_ewm'] = np.mean(abs(pd_oos_beta[times[i]] - pd_ew_beta_4[times[i]]))
        error.loc[times[i],'mae_window'] = np.mean(abs(pd_oos_beta[times[i]] - pd_bc_beta[times[i]]))
    
    error.to_csv(r'C:\Users\Krist\OneDrive\desktop\quant strategies\hw5\error_lm='+str(lm)+'.csv')
