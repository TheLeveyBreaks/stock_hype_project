import pandas as pd
from wsb_mentions import *
from rapid_api_key import rapid_api_key
import requests


# Pull top mentioned stock in wsb new

wsb_new_mentions = get_wsb_mentions()

# Filter to only stocks that have been mentioned, then convert to list

wsb_new_only_mentions = wsb_new_mentions.loc[wsb_new_mentions['count']>=1]

stock_list = wsb_new_only_mentions['stock'].tolist()

symbol_list = [x.lower() for x in stock_list ]

def get_stock_info(symbol):

	url = "https://seeking-alpha.p.rapidapi.com/symbols/get-historical-prices"

	querystring = {"symbol":symbol,"start":"2022-02-01","end":"2023-03-09","show_by":"day","sort":"as_of_date"}

	headers = {
		"X-RapidAPI-Key": rapid_api_key,
		"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring).json()

	data = response.get('data', [])

	# Empty List to store DataFrame
	dfs = []

	#Make For loop to get attributes into a dictionary, then make into a df
	for item in data:
		attributes = item.get('attributes', {})
		if attributes:
			#Make new df with a single row
			df = pd.DataFrame(attributes, index=[0])
			#Add New Column 'symbol' to the df indicating the stock ticker

			df['symbol'] = symbol

			dfs.append(df)
	if not dfs:
		return None

	result_df = pd.concat(dfs, ignore_index=True)


	return result_df


symbols = symbol_list


#Error with the length of index due to adding new column, make for loop to adjust
dfs = []

for symbol in symbols:
	df_result = get_stock_info(symbol)
	if df_result is not None:
		dfs.append(df_result)

if dfs:
	result_df = pd.concat(dfs, ignore_index = True)
	result_df

else:
	print("No Data Found")

def get_stocks_mentioned_historical_data():
	return df_result
