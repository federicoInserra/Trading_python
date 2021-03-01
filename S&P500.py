import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secrets import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')


symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'

data = requests.get(api_url).json()

price = data['latestPrice']
market_cap = data['marketCap']/1000000000000



my_columns = ['Ticker', 'Stock Price', 'Market Cap', 'Number of shares to buy']
final_dataframe = pd.DataFrame(columns=my_columns)

for stock in stocks['Ticker'][:5]:

    api_url = f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(pd.Series([stock,data['latestPrice'],data['marketCap'], 'NA'],
                                    index = my_columns),
                            ignore_index=True)

print(final_dataframe)


# sono arrivato alle batch call minuto 57