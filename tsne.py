import  pandas as pd
import tushare as ts
df = ts.get_hist_data(code="600848",start='2020-01-01',end='2020-12-10')
print(df)
df = pd.DataFrame(df)
df.to_csv("股票数据.csv")