"""
Created on Sat Jul 27 15:30:53 2022

@author: Prem Atul Jethwa
UTA Id : 1001861810

"""

import numpy as np
import pandas as pd  # To read data
import matplotlib.pyplot as plt  # To visualize
from sklearn.linear_model import LinearRegression
data = pd.read_excel('Data_file.xlsx')  # load data set from excel file

# values converts it into a numpy array
X = data.iloc[:, 0].values.reshape(-1, 1)  

#-1 means that calculate the dimension of rows, but have 1 column 
Y = data.iloc[:, 1].values.reshape(-1, 1)


# create object for the class LinearRegression
linear_reg = LinearRegression()  
linear_reg.fit(X, Y)  # perform linear regression
Y_pred = linear_reg.predict(X)  # make predictions

#Title to plot and labeling both X and Y axis
plt.title('Dietary Data')
plt.xlabel('BMI')
plt.ylabel('% of Body Fat')

plt.scatter(X, Y) # scattered plot using X and Y
plt.plot(X, Y_pred, color='green') # line plot with red color
plt.show() # display plots
