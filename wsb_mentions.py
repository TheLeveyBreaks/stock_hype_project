import pandas as pd
from stock_ticker_web_scrapper import get_dataframe_ticker_data
from wsb_scraper import get_dataframe_wsb_new_post
from collections import Counter

#Pull data from ticker, and wsb scripts

#Ticker Data
ticker_data = get_dataframe_ticker_data()
#WSB Post Data
wsb_new_post = get_dataframe_wsb_new_post()


# flatten the list column in wsb_new_post
wsb_new_post['post_content'] = wsb_new_post['post_content'].apply(set)

# Initialize a dictionary to store counts

counts = Counter()

# Iterate over the strings in wsb_new_post and count the occurances in ticker_data

for string in ticker_data['NASDAQ_Symbol']:
    counts[string] = wsb_new_post['post_content'].apply(lambda x: string in x).sum()

# Convert the dictionary to a df

counts_df = pd.DataFrame(counts.items(), columns=['stock','count'])

print(counts_df)

#counts_df.to_csv(r'C:\Users\Ryan Levey\OneDrive\Bureaublad\DE Project\stockhype\wsb_mention_counts_2.csv')






