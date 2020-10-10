## OCTOBER 8th 2020 - DAY 8 - DAILY LOG ##

* What to do today?

How about a Data Science Hands-On Crash Course... Continued!

```python
    #import libraries we will be using
    import pandas as pd
    import numpy as np

    import matplotlib.pyplot as plt

    from sklearn.linear_model import LinearRegression

    import statsmodels.api as sm

    %matplotlib inline

    #importing data
    data = pd.read_csv('C:\\Users\\chad\\Desktop\\dswithmarco\\data\\Advertising.csv', index_col=0)
    data.head()

    ##Simple Linear Regression
    plt.figure(figsize=(16,8))
    plt.scatter(data['TV'], data['sales'], c='black')
    plt.xlabel('Money spent on TV ads ($)')
    plt.ylabel('Sales (k$)')
    plt.show()


    X = data['TV'].values.reshape(-1,1)
    y = data['sales'].values.reshape(-1,1)
    reg = LinearRegression()
    reg.fit(X, y)
    print(f"The linear model is: \n Y = {reg.intercept_[0]} + {reg.coef_[0][0]}*TV")


    predictions = reg.predict(X)
    plt.figure(figsize=(16,8))
    plt.scatter(X, y, c='Black')
    plt.plot(X, predictions, c='blue', linewidth=2)
    plt.xlabel('Money spent on TV ads ($)')
    plt.ylabel('Sales (k$)')
    plt.show()

    ##Printing Summary
    X = data['TV']
    y = data['sales']
    exog = sm.add_constant(X)
    est = sm.OLS(y, exog).fit()
    print(est.summary())

    ## Continuation Point Day 8
    ## Multiple linear regression

    Xs = data.drop(['sales'], axis=1)
    y = data['sales'].values.reshape(-1,1)

    reg = LinearRegression()
    reg.fit(Xs, y)

    print(f"The linear model is: \n Y = {reg.intercept_[0]} + {reg.coef_[0][0]}*TV + {reg.coef_[0][1]}*radio + {reg.coef_[0][2]}*newspaper")

    X = np.column_stack((data['TV'], data['radio'], data['newspaper']))
    y = data['sales'].values.reshape(-1, 1)

    exog = sm.add_constant(X)
    est = sm.OLS(y, exog).fit()

    print(est.summary())
```

Video timestamp for tonight: 00:00

* reference: 
    * [Data Science Hands-On Crash Course](https://www.youtube.com/watch?v=XU5pw3QRYjQ)
    * [Data set used from Github - marcopeix](https://github.com/marcopeix/datasciencewithmarco))


