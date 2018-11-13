import pandas as pd
import numpy as np
import seaborn as sns

pd.options.display.html.table_schema = True
pd.options.display.max_rows = None

tips = sns.load_dataset("tips")
y = tips['tip']
X = tips.drop('tip', axis=1)

null_mse = sum(y**2)/(2*X.shape[1])
null_mse

def mse(X, y, coefs):
    '''
    Compute the mean squared error of a linear regression,
    given an X matrix, y vector, and vector of coefficients.
    '''
    n = X.shape[0]

    # Predicted value is X matrix times coefs vector
    preds = X @ coefs
    sum_sqr_resid = np.sum(np.square(np.subtract(preds, y)))
    mse = sum_sqr_resid/(2*n)

    return mse

def log_loss(X, y, coefs):
    '''
    Compute the log loss function for logisttic regression,
    given an X matrix, y vector, and vector of coefficients.
    '''
