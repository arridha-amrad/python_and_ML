import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
# print(data)
# also known as label -> what u want to get
predict = "G3"

# X is our features/attributes or training data and based on that we gonna predict the new value
X = np.array(data.drop([predict], 1))  # return data frame without G3
# print("X label", X)

# y is all of our labels
y = np.array(data[predict])
# print("y labels", y)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

"""
best = 0
for _ in range(30):
    # x train is section for x array
    # y train for y array
    # x test & y test to test the accuracy of our model which we gonna create
    # to test our data we splitting up 10% of our data,
    # the more the test size the more sample data is used means take more time
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    # print("x_train", x_train)
    # print("y_train", y_train)
    # print("x_test", x_test)
    # print("y_test", y_test)
    # print("y_train_length", len(y_train))
    # print("x_train_length", len(x_train))
    # print("x_test_length", len(x_test))
    # print("y_test_length", len(y_test))

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print("ACCURACY", accuracy)

    if accuracy > best:
        best = accuracy
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
"""
# Best 0.9415978583021912
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# linear regression model basically finds the best value for the intercept and slope
print("Coefficient: \n", linear.coef_)  # to retrieve the slope
print("Intercept: \n", linear.intercept_) # to retrieve the intercept

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(x, predictions[x], x_test[x], y_test[x])

p = "G1"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()