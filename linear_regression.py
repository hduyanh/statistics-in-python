import matplotlib.pyplot as plt
import covariance as c
import warnings
import numpy as np

warnings.filterwarnings('ignore')  # ignore warnings

FILE_NAME = c.CURRENT_FILE_NAME
FILE_SEPERATOR = c.FILE_SEPERATOR

def required_data(file_name, seperator):
    # getting required data 
    read_file = c.file_reader(file_name, seperator)
    modify_file = c.file_modifier(read_file)
    filter_file = c.file_filter(modify_file)
    x = filter_file['square_meter'] # steepness
    y = filter_file['meter_price'] # y_axis_section
    return(x, y)

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    # calculating regression coefficients
    b_1 = round((SS_xy / SS_xx), 4)
    b_0 = round((m_y - b_1*m_x), 4)
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
    # predicted response vector
    y_pred = b[0] + b[1]*x
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
    # putting labels
    plt.title('Linear regression function')
    plt.xlabel('area(m2)')
    plt.ylabel('price/area(dollar/m2)')
    # function to show plot
    plt.show()

def main():
    data = required_data(FILE_NAME, FILE_SEPERATOR)
    coefficients = estimate_coef(data[0], data[1])
    plot_regression_line(data[0], data[1], coefficients)
 
  
if __name__ == '__main__':
    main()

