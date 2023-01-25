import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')  # ignore warnings

CURRENT_FILE_NAME = "real_es.csv"
FILE_SEPERATOR = ','

def file_reader(file_name, seperator):
    # reading csv file to pandas dataframe
    return pd.read_csv(file_name, seperator)

def file_information(file_data):
    # Getting information about data
    length_rows = len(file_data)
    length_columns = len(file_data.columns)
    columns_header = list(file_data.columns)
    df_data_type = file_data.dtypes
    print(f"This file has: {length_rows} rows, and {length_columns} columns.\nColumns: \n{columns_header}\nDatatypes:\n{df_data_type}")

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
    print('C=', round(covariance[1][0], 4))

def correlation_coefficient_calculator(filtered_file):
    # calculating correlation
    correlation = np.corrcoef(filtered_file['meter_price'],filtered_file['square_meter'])
    rounded_correlation = round(correlation[1][0], 4)
    # calculating coefficient
    coefficient = round((rounded_correlation ** 2 * 100), 2)
    coefficient_percent = f"{coefficient}%"
    print('r=', rounded_correlation)
    print('r^2=', coefficient_percent)


def main():
    file_data = file_reader(CURRENT_FILE_NAME, FILE_SEPERATOR)
    file_info = file_information(file_data)
    modified_file = file_modifier(file_data)
    filtered_file = file_filter(modified_file)
    covariance_calculation = covariance_calculator(filtered_file)
    correlation_coefficient_calculaton = correlation_coefficient_calculator(filtered_file)


# starting point of file
if __name__ == '__main__':
    main()