import pandas as pd
import numpy as np
import argparse

def variance_threshold(X_train,minimum_value=0.1,sample_percentage=50):
    """
    Returns all columns in X_train with a value less than minimum_value for at least sample_percentage% of samples
    The parameters are:
    **X_train**: the train set
    **minimum_value**: the threshold value to look for in each column of the train set
    **sample_percentage**: the percentage of samples to look for

    it will return:
    **columns_less_than_threshold**: a list with the names of columns of the train set with a value less than minimum_value

    """

    columns_less_than_threshold = []
    for c in X_train.columns:
        if sum(X_train[c] < minimum_value) > len(X_train)*(sample_percentage/100):
            columns_less_than_threshold.append(c)
    return columns_less_than_threshold


def bin_spectra_features(X,window_width=3):
    """
    This function will bin the data by a user-defined window_width
    :param X: the spectra columns of the set to bin
    :param window_width: the window width to bin by
    :return: the new binned train or test set
    """
    new_X=pd.DataFrame()

    cols_to_bin=[c for c in X.columns if 'fuel' not in c and 'flash point' not in c]
    for i in np.arange(0,len(cols_to_bin),window_width):
        new_col_name=np.mean([pd.to_numeric(j) for j in (cols_to_bin[i:i+3])])
        new_X[new_col_name]=X[(cols_to_bin[i:i+3])].mean(axis=1)

    return new_X