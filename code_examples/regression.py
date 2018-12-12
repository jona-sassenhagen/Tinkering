import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

pd.options.display.html.table_schema = True
pd.options.display.max_rows = None

tips = sns.load_dataset("tips")
y = tips['tip']
X = tips.drop('tip', axis=1)


def mse(X, y, coefs):
    '''
    Compute the mean squared error of a linear regression,
    given an X matrix, y vector, and vector of coefficients.
    '''
    n = X.shape[0]

    # Predicted value is X matrix times coefs vector
    preds = X @ coefs
    resid = preds - y
    sse = np.square(resid).sum()
    mse = sse/n

    return mse


def log_loss(X, y, coefs):
    '''
    Compute the log loss function for logisttic regression,
    given an X matrix, y vector, and vector of coefficients.
    '''
    def sigmoid(x):
        1/(1 + np.exp(-x))

    n = X.shape[0]
    logits = X @ coefs
    preds = sigmoid(logits)
    loss_sum = -1*(y.T*np.log(preds) + (1-y).T*np.log(1-preds))

    return loss_sum/n
