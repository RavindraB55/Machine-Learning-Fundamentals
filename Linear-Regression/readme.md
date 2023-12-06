# Linear Regression

Linear regression predicts the relationship between two variables by assuming a linear connection between the independent and dependent variables. It seeks the optimal line that minimizes the sum of squared differences between predicted and actual values.

To calculate best-fit line linear regression uses a traditional slope-intercept form which is given below,

Yi = β0 + β1Xi 

where Yi = Dependent variable,  β0 = constant/Intercept, β1 = Slope/Intercept, Xi = Independent variable.


## Assumptions of Linear Regression
1). **Linearity:** The relationship between the independent variable(s) and the dependent variable is linear. The model assumes that a change in the independent variable(s) leads to a proportional change in the dependent variable.

2). **Independence of Residuals:** The residuals (the differences between the observed and predicted values) are independent. In other words, the value of the dependent variable for one observation is not affected by the values of other observations.

3). **Normality of Residuals:** The residuals are normally distributed. This assumption is important for statistical inference, particularly hypothesis testing and confidence interval estimation.

4). **Homoscedasticity:** The variance of the residuals is constant across all levels of the independent variable(s). This implies that the spread of residuals should be roughly constant as you move along the predicted values.


## Evaluation Metrics
### Coefficient of Determination or R-Squared (R2)
The R-squared (R2) value is a statistical measure that represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s) in a regression model. In other words, it assesses the goodness of fit of the model.

The R2 value ranges from 0 to 1, where:
    - 0 indicates that the model does not explain any of the variability in the dependent variable.
    - 1 indicates that the model perfectly explains the variability in the dependent variable.

The formula for R2 is:

```math
R^2 = 1 - \frac{\text{RSS}}{\text{TSS}}
```

where: 
- Residual sum of Squares (RSS) represents the unexplained or residual variation in the dependent variable by the model. It's calculated by taking the sum of the squared differences between each actual value and the predicted value from the model.
```math
RSS = \sum{(y_{i} - \hat{y}_{i})}^2
```
- Total Sum of Squares (TSS) represents the total variation in the dependent variable. It's calculated by taking the sum of the squared differences between each actual value and the mean of all actual values.
```math
RSS = \sum{(y_{i} - \bar{y}_{i})}^2
```

### Root Mean Squared Error 
The Root Mean Squared Error is the square root of the variance of the residuals. It specifies the absolute fit of the model to the data i.e. how close the observed data points are to the predicted values. 

```math
RMSE = \sqrt{\frac{RSS}{n}}
```

R-squared is a better measure than RSME. Because the value of Root Mean Squared Error depends on the units of the variables (i.e. it is not a normalized measure), it can change with the change in the unit of the variables.