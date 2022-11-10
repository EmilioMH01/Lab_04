import data

'''2.2 Verificación de avance'''
#BITCOIN
data_binance = data.data_binance.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_binance['Midprice'] = (data.data_binance['bid'] + data.data_binance['ask'])/2
data_binance['Exchange'] = 'Binance'
data_binance = data_binance.drop(['bid', 'ask'], axis=1)
data_kraken = data.data_kraken.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_kraken['Midprice'] = (data.data_kraken['bid'] + data.data_kraken['ask'])/2
data_kraken['Exchange'] = 'Kraken'
data_kraken = data_kraken.drop(['bid', 'ask'], axis=1)
data_currencycom = data.data_currencycom.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_currencycom['Midprice'] = (data.data_currencycom['bid'] + data.data_currencycom['ask'])/2
data_currencycom['Exchange'] = 'Currencycom'
data_currencycom = data_currencycom.drop(['bid', 'ask'], axis=1)

#ETHEREUM
data_binanceeth = data.data_binanceeth.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_binanceeth['Midprice'] = (data.data_binanceeth['bid'] + data.data_binanceeth['ask'])/2
data_binanceeth['Exchange'] = 'Binance'
data_binanceeth = data_binanceeth.drop(['bid', 'ask'], axis=1)
data_krakeneteth = data.data_krakeneteth.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_krakeneteth['Midprice'] = (data.data_krakeneteth['bid'] + data.data_krakeneteth['ask'])/2
data_krakeneteth['Exchange'] = 'Kraken'
data_krakeneteth = data_krakeneteth.drop(['bid', 'ask'], axis=1)
data_currencycometh = data.data_currencycometh.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_currencycometh['Midprice'] = (data.data_currencycometh['bid'] + data.data_currencycometh['ask'])/2
data_currencycometh['Exchange'] = 'Currencycom'
data_currencycometh = data_currencycometh.drop(['bid', 'ask'], axis=1)

#XRP
data_binancexrp = data.data_binancexrp.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_binancexrp['Midprice'] = (data.data_binancexrp['bid'] + data.data_binancexrp['ask'])/2
data_binancexrp['Exchange'] = 'Binance'
data_binancexrp = data_binancexrp.drop(['bid', 'ask'], axis=1)
data_krakenetxrp = data.data_krakenetxrp.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_krakenetxrp['Midprice'] = (data.data_krakenetxrp['bid'] + data.data_krakenetxrp['ask'])/2
data_krakenetxrp['Exchange'] = 'Kraken'
data_krakenetxrp = data_krakenetxrp.drop(['bid', 'ask'], axis=1)
data_currencycomxrp = data.data_currencycomxrp.drop(['timestamp','high','low','open','last','previousClose','change','percentage','average','baseVolume','close', 'symbol'], axis=1)
data_currencycomxrp['Midprice'] = (data.data_currencycomxrp['bid'] + data.data_currencycomxrp['ask'])/2
data_currencycomxrp['Exchange'] = 'Currencycom'
data_currencycomxrp = data_currencycomxrp.drop(['bid', 'ask'], axis=1)