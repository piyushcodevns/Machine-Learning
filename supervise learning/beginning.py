import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([35,50,65,80,95])

model=LinearRegression()

model.fit(x,y)

prediction=model.predict(x)
mse=mean_squared_error(y,prediction)