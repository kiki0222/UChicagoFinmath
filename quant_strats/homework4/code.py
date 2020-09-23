# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:15:01 2020

@author: Krist
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import quandl
import functools
import seaborn as sns
import random

def debtnan(m):
    return np.isnan(m).any()
def debtlarge(m):
    series = m.apply(lambda x: x>0.1)
    return series.all()
    
    
tickers = pd.read_csv(r"C:\Users\Krist\OneDrive\desktop\quant strategies\hw4\ZACKS_FC.csv")
tickers = tickers.loc[(tickers['exchange'] == "NYSE") | (tickers['exchange'] == "NSDQ")]
tickers = tickers.loc[tickers['is_active'] == "Y"]
tickers = list(tickers['ticker'])



quandl.ApiConfig.api_key = "khzKyrGRmxZen9BA5h9a"
fc = quandl.get_table('ZACKS/FC', paginate=True, ticker = tickers)
fr = quandl.get_table('ZACKS/FR', paginate=True, ticker = tickers)
#mktv = quandl.get_table('ZACKS/MKTV', paginate=True, ticker = tickers)
#shrs = quandl.get_table('ZACKS/SHRS', paginate=True, ticker = tickers)

#following is to filter at least 200 tickers for our research
#delete automotive = 5, financial = 13, insurance = 13
fc = fc.loc[(fc['zacks_sector_code'] != 5) & (fc['zacks_sector_code'] != 13)]

#for period 2012-01 to 2019-01
fc = fc.loc[fc['per_end_date'] > '2011-12-31']
fc = fc.sort_values(by = ['m_ticker','per_end_date'])
fc_last = fc.groupby(fc['m_ticker']).last()
fc_last = fc_last.loc[fc_last['per_end_date'] >= '2019-01-31']
tickers = list(fc_last.index)

#to get tickers that have debt/market cap > 0.1 and have values during the period
fr['in_tick'] = fr['m_ticker'].apply(lambda x: x in tickers)
fr = fr.loc[fr['in_tick'] == True]
fr = fr.drop(columns = ['in_tick'])
fr = fr.loc[(fr['per_end_date'] > '2011-12-31') & (fr['per_end_date'] < '2019-01-31')]
fr = fr.sort_values(by = ['m_ticker','per_end_date'])

fr_debt = fr.groupby(by = 'm_ticker').agg({'tot_debt_tot_equity': debtnan})
fr_debt = fr_debt.loc[fr_debt['tot_debt_tot_equity'] == False]
tickers = list(fr_debt.index)
fr['in_tick'] = fr['m_ticker'].apply(lambda x: x in tickers)
fr = fr.loc[fr['in_tick'] == True]
fr = fr.drop(columns = ['in_tick'])

fr_debt = fr.groupby(by = 'm_ticker').agg({'tot_debt_tot_equity': debtlarge})
fr_debt = fr_debt.loc[fr_debt['tot_debt_tot_equity'] == True]
tickers = list(fr_debt.index)

#filter by accessible closing price
eod_ticker = pd.read_csv(r'C:\Users\Krist\OneDrive\desktop\quant strategies\hw4\ticker_list.csv')
eod_ticker = list(eod_ticker['Ticker'])

ticker = [t for t in tickers if t in eod_ticker]

###get close price
eod = pd.DataFrame()
for t in ticker:
    table_name = 'EOD/'+t
    ##table_name = 'EOD/AA'
    eod_seg = quandl.get(table_name)
    if eod_seg.index[0] <= pd.Timestamp('2012-01-01'):
        eod_seg['ticker'] = t
        eod = eod.append(eod_seg)
    else:
        continue

###choose 400+ tickers finally
ticker = list(eod['ticker'].drop_duplicates())
#################################################

#update data
fc = quandl.get_table('ZACKS/FC', paginate=True, ticker = ticker)
fr = quandl.get_table('ZACKS/FR', paginate=True, ticker = ticker)
mktv = quandl.get_table('ZACKS/MKTV', paginate=True, ticker = ticker)
shrs = quandl.get_table('ZACKS/SHRS', paginate=True, ticker = ticker)

#to get debt ratio quarterly
fr = fr.sort_values(by = ['m_ticker','per_end_date'])
fc = fc.sort_values(by = ['m_ticker','per_end_date'])
fr = fr.loc[(fr['per_end_date'] >= pd.Timestamp('2011-09-30')) & (fr['per_end_date'] <= pd.Timestamp('2018-12-31'))]
fc = fc.loc[(fc['per_end_date'] >= pd.Timestamp('2011-09-30')) & (fc['per_end_date'] <= pd.Timestamp('2018-12-31'))]
fcfr = fc.merge(fr, how = 'left', on = ['m_ticker','per_end_date','per_type'])
debt_to_cap = fcfr[['m_ticker', 'per_end_date', 'filing_date', 'tot_debt_tot_equity','per_type']]
debt_to_cap = debt_to_cap.loc[debt_to_cap['per_type'] == 'Q']

mktv = mktv.sort_values(by = ['m_ticker','per_end_date'])
mktv = mktv.loc[(mktv['per_end_date'] >= pd.Timestamp('2011-09-30')) & (mktv['per_end_date'] <= pd.Timestamp('2018-12-31'))]
mkv = mktv[['m_ticker','per_end_date','per_type','mkt_val']]
debt_to_cap = debt_to_cap.merge(mkv, how = 'left', on = ['m_ticker','per_end_date','per_type'])

shrs = shrs.sort_values(by = ['m_ticker','per_end_date'])
shrs = shrs.loc[(shrs['per_end_date'] >= pd.Timestamp('2011-09-30')) & (shrs['per_end_date'] <= pd.Timestamp('2018-12-31'))]
shs = shrs[['m_ticker','per_end_date','per_type','shares_out']]
debt_to_cap = debt_to_cap.merge(shs, how = 'left', on = ['m_ticker','per_end_date','per_type'])
# I found there is a mismatch of per_end_date for fc and mktv data for some specific companies.
# So I drop companies 
debt_to_cap = debt_to_cap.dropna()
ticker = [t for t in ticker if t in list(debt_to_cap['m_ticker'].drop_duplicates())]
#update data again
fr['in_tick'] = fr['m_ticker'].apply(lambda x: x in ticker)
fc['in_tick'] = fc['m_ticker'].apply(lambda x: x in ticker)
mktv['in_tick'] = mktv['m_ticker'].apply(lambda x: x in ticker)
fr = fr.loc[fr['in_tick'] == True]
fc = fc.loc[fc['in_tick'] == True]
mktv = mktv.loc[mktv['in_tick'] == True]
fr = fr.drop(columns = ['in_tick'])
fc = fc.drop(columns = ['in_tick'])
mktv = mktv.drop(columns = ['in_tick'])


# get debt per end date
debt_to_cap['tot_debt'] = debt_to_cap['tot_debt_tot_equity'] * debt_to_cap['mkt_val']
eod['in_tick'] = eod['ticker'].apply(lambda x: x in ticker)
eod = eod.reset_index()
cp = eod.loc[(eod['in_tick'] == True) & (eod['Date'] >= pd.Timestamp('2011-09-30')) & (eod['Date'] <= pd.Timestamp('2019-01-31'))]
cp = cp[['ticker','Date','Adj_Close']]

# debt ratio, can't think of any ways better than loops to adjust for lagged filing date
cp['tot_debt'] = pd.Series(np.nan)
cp['shares_out'] = pd.Series(np.nan)
for t in ticker:
    #t = 'LLY'
    d = debt_to_cap.loc[debt_to_cap['m_ticker'] == t]
    filing = list(d['filing_date'])
    for i in range(len(filing)-1):
        debt = d.loc[d['filing_date'] == filing[i],'tot_debt'].values[0]
        market_value = d.loc[d['filing_date'] == filing[i],'mkt_val'].values[0]
        fiscal_end = d.loc[d['filing_date'] == filing[i], 'per_end_date'].values[0]
        lly = cp.loc[cp['ticker'] == t]
        price = lly.loc[lly['Date'] <= pd.Timestamp(fiscal_end)][-1:]['Adj_Close'].values[0]
        ids = lly.loc[(lly['Date'] > filing[i]) & (lly['Date'] <= filing[i+1])].index
        if len(ids) != 0:
            cp.loc[list(ids)[0]:list(ids)[-1],'tot_debt'] = debt
            cp.loc[list(ids)[0]:list(ids)[-1],'shares_out'] = market_value/price
cp['tot_debt_tot_cap'] = cp['tot_debt']/(cp['shares_out']*cp['Adj_Close'])


# get return per end date
roi = fc.merge(fr, how = 'left', on = ['m_ticker','per_end_date','per_type'])\
    [['m_ticker', 'per_end_date', 'filing_date', 'per_type', 'ret_invst', 'net_lterm_debt', 'tot_lterm_debt']]
roi = roi.loc[roi['per_type'] == 'Q']
mkv = mktv[['m_ticker','per_end_date','per_type','mkt_val']]
roi = roi.merge(mkv, how = 'left', on = ['m_ticker','per_end_date','per_type'])
for i in range(len(roi)):
    if np.isnan(roi.loc[i,'net_lterm_debt']):
        roi.loc[i,'net_lterm_debt'] = roi.loc[i,'tot_lterm_debt']
roi['ret'] = roi['ret_invst']*(roi['net_lterm_debt']+roi['mkt_val'])
# roi
cp['net_lterm_debt'] = pd.Series(np.nan)
cp['ret'] = pd.Series(np.nan)

for t in ticker:
    #t = 'LLY'
    r = roi.loc[roi['m_ticker'] == t]
    filing = list(r['filing_date'].dropna())
    for i in range(len(filing)-1):
        nltd = r.loc[r['filing_date'] == filing[i], 'net_lterm_debt'].values[0]
        ret = r.loc[r['filing_date'] == filing[i], 'ret'].values[0]
        lly = cp.loc[cp['ticker'] == t]
        ids = lly.loc[(lly['Date'] > filing[i]) & (lly['Date'] <= filing[i+1])].index
        if len(ids) != 0:
            cp.loc[list(ids)[0]:list(ids)[-1],'net_lterm_debt'] = nltd
            cp.loc[list(ids)[0]:list(ids)[-1],'ret'] = ret
cp['roi'] = cp['ret']/(cp['net_lterm_debt'] + cp['shares_out']*cp['Adj_Close'])


# eps
eps = fc[['m_ticker','per_end_date', 'filing_date', 'per_type','eps_diluted_net','basic_net_eps']]
eps = eps.loc[eps['per_type'] == 'Q']
eps = eps.reset_index(drop = True)
for i in range(len(eps)):
    if np.isnan(eps.loc[i,'eps_diluted_net']):
        eps.loc[i,'eps_diluted_net'] = eps.loc[i,'basic_net_eps']
cp['eps'] = pd.Series(np.nan)
for t in ticker:
    e = eps.loc[eps['m_ticker'] == t]
    filing = list(e['filing_date'].dropna())
    for i in range(len(filing)-1):
        earning = e.loc[e['filing_date'] == filing[i], 'eps_diluted_net'].values[0]
        lly = cp.loc[cp['ticker'] == t]
        ids = lly.loc[(lly['Date'] > filing[i]) & (lly['Date'] <= filing[i+1])].index
        if len(ids) != 0:
            cp.loc[list(ids)[0]:list(ids)[-1],'eps'] = earning
cp['pe'] = cp['Adj_Close']/cp['eps']

# Since we already calculated all the ratios, we'll use data to construct our trading strategy.
data = cp[['ticker','Date','Adj_Close','tot_debt_tot_cap','roi','pe','shares_out']]
data = data.loc[(data['Date'] >= pd.Timestamp('2012-01-01')) & (data['Date'] <= pd.Timestamp('2019-01-31'))]

# to construct indicator for ranking, I use monthly average 
data['year'] = data['Date'].apply(lambda x: x.year)
data['month'] = data['Date'].apply(lambda x: x.month)
ratios = data.groupby(by = ['ticker','year','month']).agg\
    ({'tot_debt_tot_cap':np.mean, 'roi':np.mean, 'pe':np.mean})
ratios['d_dtc'] = data.groupby(by = ['ticker','year','month']).last()['tot_debt_tot_cap']\
    /data.groupby(by = ['ticker','year','month']).first()['tot_debt_tot_cap'] - 1
ratios['d_roi'] = data.groupby(by = ['ticker','year','month']).last()['roi']\
    /data.groupby(by = ['ticker','year','month']).first()['roi'] - 1
ratios['d_pe'] = data.groupby(by = ['ticker','year','month']).last()['pe']\
    /data.groupby(by = ['ticker','year','month']).first()['pe'] - 1  
ratios['return'] = data.groupby(by = ['ticker','year','month']).last()['Adj_Close']\
    /data.groupby(by = ['ticker','year','month']).first()['Adj_Close'] - 1
ratios['return'] = ratios.groupby('ticker')['return'].shift(-1)
ratios = ratios.reset_index()
ratios['ym'] = ratios['year'].apply(lambda x: str(x))+'-'+ratios['month'].apply(lambda x: str(x))
yearmonth = list(ratios['ym'].drop_duplicates())

# rank by every single indicator
ranks = {1:'tot_debt_tot_cap',2:'roi',3:'pe',4:'d_dtc',5:'d_roi',6:'d_pe'}
for x in ranks:
    ratios['rank'+str(x)] = pd.Series(np.nan)

for i in range(len(yearmonth)-1):
    seg = ratios.loc[ratios['ym'] == yearmonth[i]]
    for x in ranks:
        values = seg[ranks[x]].values
        value90 = np.nanpercentile(values,90)
        value10 = np.nanpercentile(values,10)
        ids1 = seg.loc[seg[ranks[x]] >= value90].index
        ids2 = seg.loc[seg[ranks[x]] <= value10].index
        ratios.loc[ids1,'rank'+str(x)] = 1
        ratios.loc[ids2,'rank'+str(x)] = -1

for x in ranks:
    ratios['return'+str(x)] = ratios['return'] * ratios['rank'+str(x)]

# rank by combination of indicators
ratios['rank7'] = pd.Series(np.nan)
ratios['rank8'] = pd.Series(np.nan)
for i in range(len(yearmonth)-1):
    seg = ratios.loc[ratios['ym'] == yearmonth[i]]
    values1 = seg['tot_debt_tot_cap'].values
    value190 = np.nanpercentile(values1,90)
    value110 = np.nanpercentile(values1,10)
    values2 = seg['roi'].values
    value290 = np.nanpercentile(values2,90)
    value210 = np.nanpercentile(values2,10)
    values3 = seg['pe'].values
    value390 = np.nanpercentile(values3,90)
    value310 = np.nanpercentile(values3,10)
    ids1 = seg.loc[(seg['tot_debt_tot_cap'] >= value190) & (seg['roi'] <= value210) &\
                   (seg['pe'] <= value310)].index
    ids2 = seg.loc[(seg['tot_debt_tot_cap'] <= value110) & (seg['roi'] >= value290) &\
                   (seg['pe'] >= value390)].index
    ratios.loc[ids1,'rank7'] = 1
    ratios.loc[ids2,'rank7'] = -1
    
    values1 = seg['d_dtc'].values
    value190 = np.nanpercentile(values1,90)
    value110 = np.nanpercentile(values1,10)
    values2 = seg['d_roi'].values
    value290 = np.nanpercentile(values2,90)
    value210 = np.nanpercentile(values2,10)
    values3 = seg['d_pe'].values
    value390 = np.nanpercentile(values3,90)
    value310 = np.nanpercentile(values3,10)
    ids1 = seg.loc[(seg['d_dtc'] >= value190) & (seg['d_roi'] >= value290) &\
                   (seg['d_pe'] <= value310)].index
    ids2 = seg.loc[(seg['d_dtc'] <= value110) & (seg['d_roi'] <= value210) &\
                   (seg['d_pe'] >= value390)].index
    ratios.loc[ids1,'rank8'] = 1
    ratios.loc[ids2,'rank8'] = -1

    
ratios['return7'] = ratios['return'] * ratios['rank7']
ratios['return8'] = ratios['return'] * ratios['rank8']

portfolio = ratios.groupby(by = 'ym').agg({'return1':np.nanmean,'return2':np.nanmean,\
        'return3':np.nanmean,'return4':np.nanmean,'return5':np.nanmean,'return6':np.nanmean,\
        'return7':np.nanmean, 'return8':np.nanmean})
for x in ranks:
    print(portfolio['return'+str(x)].describe())
portfolio['return7'].describe()
portfolio['return8'].describe()

portfolio = portfolio.reset_index()
for i in range(1,9):
    plt.figure()
    plt.plot((portfolio['return'+str(i)]+1).cumprod())
    
