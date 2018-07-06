__author__ = 'Administrator'

from sqlalchemy import create_engine

#engine = create_engine('mysql://root:root@127.0.0.1/stockdata0?charset=utf8')

import pandas as pd
from pandas import Series, DataFrame

data = {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]}
f1 = DataFrame(data)

print(f1)
f1["price"]=[ 'dd % i' % i for i in f1["price"]]
print(f1)
print(f1["price"])



#df.to_sql('tick_data',engine,if_exists='append')