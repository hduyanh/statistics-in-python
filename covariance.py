import pandas as pd
import numpy as np

CURRENT_FILE_NAME = "Real_es.csv"

def file_reader(file_name):
    # reading csv file to pandas dataframe
    return pd.read_csv(file_name)

def file_modifier(file_data):
    # replace string in 'Price' with float
    file_data['Price'] = file_data['Price'].str.replace('$','').str.replace(',','').astype(float)
    # add 2 column to dataframe: square_meter and meter_price
    modified_data = file_data.assign(square_meter=lambda x: x['Area (ft.)'] * 0.09290304, \
    meter_price=lambda x: file_data['Price'] / x['square_meter'])
    return modified_data

def file_filter(complete_data):
    # filter Californian flat
    filter_california = complete_data[complete_data['State'].isin(['California'])]
    # return required y:meter_price and x:square_meter
    californian_flat = filter_california[['meter_price', 'square_meter']]
    return(californian_flat)

def covariance_calculator(filtered_file):
    # calculating covariance
    covariance = np.cov(filtered_file['meter_price'],filtered_file['square_meter'])
    print(covariance[1][0])


def main():
    file_data = file_reader(CURRENT_FILE_NAME)
    modified_file = file_modifier(file_data)
    filtred_file = file_filter(modified_file)
    covariance = covariance_calculator(filtred_file)


# starting point of file
if __name__ == '__main__':
    main()