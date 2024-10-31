import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = pd.read_csv('BTC_data.csv')
f['time'] = pd.to_datetime(f['time'])

plt.plot(f['time'], f['close'], 'r')

plt.xticks(rotation=90)

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: pd.to_datetime(x).strftime('%d-%m-%y')))
plt.tight_layout()
plt.show()