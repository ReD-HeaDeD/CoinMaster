import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as lite
import pandas as pd
import numpy as np
import seaborn as sb


con = lite.connect('coin.db')

sql_cmd = "SELECT dollar FROM coins WHERE data LIKE '%2022%'"

df = pd.read_sql(sql_cmd, con)
df = df.replace(to_replace='[$]', value='', regex=True)
df = df.replace(to_replace='[,]', value='', regex=True)
df = df.astype({"dollar": "float64"})
df.head()
print(df)
y_simple = np.array(df)
my_rho = np.corrcoef(y_simple)
print(my_rho)

