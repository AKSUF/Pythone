import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
file_path=r'G:\File store\Book1.csv'
df=pd.read_csv(file_path)
print(df)
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')
reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
print("Coeffcient(Slopes):",reg.coef_)
print(("Interect",reg.intercept_))
plt.plot(df.area,reg.predict(df[['area']]),color='blue')

new_area=[[3300]]
predicted_price=reg.predict(new_area)
print("Predicted Price for 3300 sq.ft area",predicted_price[0])
plt.show()