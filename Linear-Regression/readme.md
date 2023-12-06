# Linear Regression

Linear regression predicts the relationship between two variables by assuming a linear connection between the independent and dependent variables. It seeks the optimal line that minimizes the sum of squared differences between predicted and actual values.

To calculate best-fit line linear regression uses a traditional slope-intercept form which is given below,

Yi = β0 + β1Xi 

where Yi = Dependent variable,  β0 = constant/Intercept, β1 = Slope/Intercept, Xi = Independent variable.

## Evaluation Metrics
### Coefficient of Determination or R-Squared (R2)
The R-squared (R2) value is a statistical measure that represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s) in a regression model. In other words, it assesses the goodness of fit of the model.

The R2 value ranges from 0 to 1, where:
    - 0 indicates that the model does not explain any of the variability in the dependent variable.
    - 1 indicates that the model perfectly explains the variability in the dependent variable.

The formula for R2 is:

\[ R^2 = 1 - \frac{\text{SSR}}{\text{SST}} \]
