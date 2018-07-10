import tushare as ts
import os
from tools import mkdir

mkdir.mkdirA("d:/day")

filename = 'd:/day/bigfile.csv'
for code in ['000875', '600848', '000981']:
    df = ts.get_hist_data(code)
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=None)
    else:
        df.to_csv(filename)