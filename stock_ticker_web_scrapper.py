import pandas as pd

data_url_other = 'https://datahub.io/core/nyse-other-listings/r/other-listed.csv'

stock_ticker = pd.read_csv(data_url_other)

def get_dataframe_ticker_data():
    data_url_other = 'https://datahub.io/core/nyse-other-listings/r/other-listed.csv'
    stock_ticker = pd.read_csv(data_url_other)
    stock_ticker.columns = stock_ticker.columns.str.replace(' ', '_')
    return stock_ticker

