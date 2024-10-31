import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

s = df['Species'].value_counts()
plt.figure(figsize=(9, 7))
plt.pie(s, labels=s.index, autopct='', startangle=140)
plt.title('Доля разных видов ирисов')
plt.axis('equal')  

p = [0, 1.2, 1.5, float('inf')]  
pl = ['меньше 1.2', '1.2-1.5', 'больше 1.5 см']
df['PetalLengthCategory'] = pd.cut(df['PetalLengthCm'], bins=p, labels=pl, right=False)
pc = df['PetalLengthCategory'].value_counts()

plt.figure(figsize=(9, 7))
plt.pie(pc, labels=pc.index, autopct='', startangle=140)
plt.title('Доля ирисов по длине лепестка')
plt.axis('equal') 

plt.show()

