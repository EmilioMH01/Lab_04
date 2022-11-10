import main
import plotly.graph_objects as go
import plotly.express as px

#PLOT BITCOIN
Bitcoin = go.Figure()

Bitcoin.add_scatter(x= main.data_kraken['datetime'], y= main.data_kraken['Midprice'], name='Kraken')
Bitcoin.add_scatter(x= main.data_currencycom['datetime'], y= main.data_currencycom['Midprice'], name='Currencycom')
Bitcoin.add_scatter(x= main.data_binance['datetime'], y= main.data_binance['Midprice'], name='Binance')

Bitcoin.update_layout(title='Bitcoin',
                   xaxis_title='Datetime',
                   yaxis_title='Price')

#Ethereum
Ethereum = go.Figure()

Ethereum.add_scatter(x= main.data_krakeneteth['datetime'], y= main.data_krakeneteth['Midprice'], name='Kraken')
Ethereum.add_scatter(x= main.data_currencycometh['datetime'], y= main.data_currencycometh['Midprice'], name='Currencycom')
Ethereum.add_scatter(x= main.data_binanceeth['datetime'], y= main.data_binanceeth['Midprice'], name='Currencycom')

Ethereum.update_layout(title='Ethereum',
                   xaxis_title='Datetime',
                   yaxis_title='Price')
                   
#Ripple
Ripple = go.Figure()

Ripple.add_scatter(x= main.data_krakenetxrp['datetime'], y= main.data_krakenetxrp['Midprice'], name='Kraken')
Ripple.add_scatter(x= main.data_currencycomxrp['datetime'], y= main.data_currencycomxrp['Midprice'], name='Currencycom')
Ripple.add_scatter(x= main.data_binancexrp['datetime'], y= main.data_binancexrp['Midprice'], name='Kraken')

Ripple.update_layout(title='Ripple',
                   xaxis_title='Datetime',
                   yaxis_title='Price')

