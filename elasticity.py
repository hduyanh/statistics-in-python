import linear_regression as lr
import covariance as c
import warnings

warnings.filterwarnings('ignore')  # ignore warnings

FILE_NAME = c.CURRENT_FILE_NAME
FILE_SEPERATOR = c.FILE_SEPERATOR
BASE_AREA_IN_SQUARE_METER = 103 # =x0


def getting_data(file_name, seperator):
    required_data = lr.required_data(file_name, seperator)
    estimated_coef = lr.estimate_coef(required_data[0], required_data[1])
    b0 = estimated_coef[0]
    b1 = estimated_coef[1]
    return(b0, b1)

def elasticity_calculator(b0, b1, x0):
    E = b1 * (x0 / (b0 + b1 * x0))
    E_in_percent  = f"{round(E, 2)}%"
    print(E_in_percent)

def main():
    data = getting_data(FILE_NAME, FILE_SEPERATOR)
    elasticity_calculation  = elasticity_calculator(data[0], data[1], BASE_AREA_IN_SQUARE_METER)
  
if __name__ == '__main__':
    main()
