## OCTOBER 11th 2020 - DAY 11 - DAILY LOG ##

* What to do today?


```python

    import pandas as pd
    import numpy as np

    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.metrics import roc_curve, auc, confusion_matrix

    %matplotlib inline

    DATAPATH = 'C:\\Users\\chad\\Desktop\\dswithmarco\\data\\mushrooms.csv'

    data = pd.read_csv(DATAPATH)
    data.head()

    x = data['class']
    ax = sns.countplot(x=x, data=data)

    def plot_data(hue, data):
        for i, col in enumerate(data.columns):
            plt.figure(i)
            ax = sns.countplot(x=data[col], hue=hue, data=data)

    hue = data['class']
    data_to_plot = data.drop('class', axis=1)

    plot_data(hue, data_to_plot)

    for col in data.columns:
        print(f"{col}: {data[col].isnull().sum()}")

```

breakpoint for tonight 35:02

* reference: 
    * [Data Science Hands-On Crash Course](https://www.youtube.com/watch?v=XU5pw3QRYjQ)


