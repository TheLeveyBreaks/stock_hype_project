# get S&P 500 Stock Data
import datapackage
import pandas as pd

data_url = 'https://datahub.io/core/s-and-p-500-companies/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources

def get_dataframe_ticker_data():
    for resource in resources:
        if resource.tabular:
            data = pd.read_csv(resource.descriptor['path'])
            return data
            #print (data)


data = get_dataframe_ticker_data()
