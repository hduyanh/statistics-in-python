from scipy import stats
import matplotlib.pyplot as plt
import covariance as c
import warnings



warnings.filterwarnings('ignore')  # ignore warnings

CURRENT_FILE_NAME = "real_es.csv"
FILE_SEPERATOR = ','

read = c.file_reader(CURRENT_FILE_NAME, FILE_SEPERATOR)
modify = c.file_modifier(read)
filtered_file = c.file_filter(modify)


m, b, r, p, std_err = stats.linregress(filtered_file['meter_price'], filtered_file['square_meter'])
print(m, b, r, p, std_err )

def pred(x, m, b):
    return x*m+b

x = pred(4,m,b)
print(x)
#filtered_file.plot(kind = 'scatter', x = 'square_meter', y = 'meter_price')
#plt.show()

