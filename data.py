import ccxt
import pandas as pd

binance = ccxt.binance()
kraken = ccxt.kraken()
currencycom = ccxt.currencycom()
rango = 1290

#BITCOIN
binance_btc = binance.fetch_ticker('BTC/USDT')
kraken_btc = kraken.fetch_ticker('BTC/USDT')
currencycom_btc = currencycom.fetch_ticker('BTC/USDT')
data_binance = pd.DataFrame(index = range(rango), columns = list(binance_btc.keys())[0:19])
data_kraken = pd.DataFrame(index = range(rango), columns = list(kraken_btc.keys())[0:19])
data_currencycom = pd.DataFrame(index = range(rango), columns = list(currencycom_btc.keys())[0:19])

#ETHEREUM
binance_eth = binance.fetch_ticker('ETH/USDT')
kraken_eth = kraken.fetch_ticker('ETH/USDT')
currencycom_eth = currencycom.fetch_ticker('ETH/USDT')
data_binanceeth = pd.DataFrame(index = range(rango), columns = list(binance_eth.keys())[0:19])
data_krakeneteth = pd.DataFrame(index = range(rango), columns = list(kraken_eth.keys())[0:19])
data_currencycometh = pd.DataFrame(index = range(rango), columns = list(currencycom_eth.keys())[0:19])

#XRP
binance_xrp = binance.fetch_ticker('XRP/USDT')
kraken_xrp = kraken.fetch_ticker('XRP/USDT')
currencycom_xrp = currencycom.fetch_ticker('XRP/USDT')
data_binancexrp = pd.DataFrame(index = range(rango), columns = list(binance_xrp.keys())[0:19])
data_krakenetxrp = pd.DataFrame(index = range(rango), columns = list(kraken_xrp.keys())[0:19])
data_currencycomxrp = pd.DataFrame(index = range(rango), columns = list(currencycom_xrp.keys())[0:19])

for i in range(rango):
    #CADA 100 SON 5MIN
    #BITCOIN
    binance_btc = binance.fetch_ticker('BTC/USDT')
    kraken_btc = kraken.fetch_ticker('BTC/USDT')
    currencycom_btc = currencycom.fetch_ticker('BTC/USDT')
    data_binance.iloc[i] = list(binance_btc.values())[0:19]
    data_kraken.iloc[i] = list(kraken_btc.values())[0:19]
    data_currencycom.iloc[i] = list(currencycom_btc.values())[0:19]
    
    #ETHEREUM
    binance_eth = binance.fetch_ticker('ETH/USDT')
    kraken_eth = kraken.fetch_ticker('ETH/USDT')
    currencycom_eth = currencycom.fetch_ticker('ETH/USDT')
    data_binanceeth.iloc[i] = list(binance_eth.values())[0:19]
    data_krakeneteth.iloc[i] = list(kraken_eth.values())[0:19]
    data_currencycometh.iloc[i] = list(currencycom_eth.values())[0:19]
    
    #XRP
    binance_xrp = binance.fetch_ticker('XRP/USDT')
    kraken_xrp = kraken.fetch_ticker('XRP/USDT')
    currencycom_xrp = currencycom.fetch_ticker('XRP/USDT')
    data_binancexrp.iloc[i] = list(binance_xrp.values())[0:19]
    data_krakenetxrp.iloc[i] = list(kraken_xrp.values())[0:19]
    data_currencycomxrp.iloc[i] = list(currencycom_xrp.values())[0:19]
    