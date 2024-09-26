import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from sklearn.linear_model import LinearRegression
import tglearn #custom libray

lifesat = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

print(lifesat.head(27))

lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23500, 63000, 3, 10])
plt.show()


#model = NNeinearRegression(n_neighbors=3) #선형 회귀 모델 적용
model=tglearn.LinearRegression() #apply custom

model.fit(X, y)

X_new = [[32142.0]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # output: [[6.30165767]]