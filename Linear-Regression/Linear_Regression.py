# The objective of a linear regression model is to find a LINEAR relationship between one or more features (independent variables) and a continuous target variable.

import sys
sys.path.append("..") 
import numpy as np
import matplotlib.pyplot as plt
from Plots import scatter_plot, plot, ploty
from Metrics import PerformanceMetrics

'''
HELPFUL LINKS:
- https://s3.amazonaws.com/assets.datacamp.com/email/other/ML+Cheat+Sheet_2.pdf
- https://towardsdatascience.com/linear-regression-using-python-b136c91bf0a2
- https://analyticsvidhya.com/blog/2021/10/everything-you-need-to-know-about-linear-regression/
'''

def generate_data():
    # Generate the random data
    np.random.seed(0)
    x = np.random.rand(1000,1)
    y = 2 + 3 * x + np.random.rand(1000, 1)
    return x, y


# Linear Regression starts with randomly selected parameters (a bias term and slope), and then moves towards minimizing a cost (error) function.
# The cost function typically used is the sum of the square of the residuals.

class LinearRegressionUsingGD:
    '''
    Params:
        - eta (float): Learning Rate
        - n_iterations (float): Number of iterations to pass over the training set
    
    Attributes:
        - w_ : Weights after fitting model
        - cost_ : total error of the model after each iteration
    '''

    def __init__(self, eta=0.05, n_iterations = 1000):
        self.eta = eta
        self.n_iterations = n_iterations

    def fit(self, x, y):
        '''
        Params: 
            -  x : array-like, shape = [n_samples, n_features] Training samples
            - y : array-like, shape = [n_samples, n_target_values] Target values
        
        Returns:
            - self: object
        '''

        self.cost_ = []
        self.w_ = np.zeros((x.shape[1], 1))
        m = x.shape[0]

        for _ in range(self.n_iterations):
            y_pred = np.dot(x, self.w_)
            residuals = y_pred - y
            gradient_vector = np.dot(x.T, residuals)
            self.w_ -= (self.eta / m) * gradient_vector
            cost = np.sum((residuals ** 2)) / (2*m)
            self.cost_.append(cost)

        return self
        
    def predict(self, x):
        '''
        Params:
            - x : array-like, shape = [n_samples, n_features] Test samples
        '''
        return np.dot(x, self.w_)


if __name__ == "__main__":
    # initializing the model
    linear_regression_model = LinearRegressionUsingGD()

    # generate the data set
    x, y = generate_data()

    # transform the feature vectors to include the bias term
    # adding 1 to all the instances of the training set.
    m = x.shape[0]
    x_train = np.c_[np.ones((m, 1)), x]

    # fit/train the model
    linear_regression_model.fit(x_train, y)

    # predict values
    predicted_values = linear_regression_model.predict(x_train)

    # model parameters
    print(linear_regression_model.w_)
    intercept, coeffs = linear_regression_model.w_

    # cost_function
    cost_function = linear_regression_model.cost_

    # plotting
    scatter_plot(x, y)
    plot(x, predicted_values)
    plt.show()
    ploty(cost_function, 'no of iterations', 'cost function')

    # computing metrics
    metrics = PerformanceMetrics(y, predicted_values)
    rmse = metrics.compute_rmse()
    r2_score = metrics.compute_r2_score()

    print('The coefficient is {}'.format(coeffs))
    print('The intercept is {}'.format(intercept))
    print('Root mean squared error of the model is {}.'.format(rmse))
    print('R-squared score is {}.'.format(r2_score))