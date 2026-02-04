

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

if __name__ == "__main__":
    df = pd.read_excel('project_1/data/data.xls')

    print("sneak peak of the data: \n", df.head())
    print("columns of the data: \n", df.columns)
    print("shape of the data: \n", df.shape)
    print("data types of the data: \n", df.dtypes)
    print("missing values of the data: \n", df.isnull().sum())
    print("unique values of the data: \n", df.nunique())
    print("correlation of the data: \n", df.corr())
    print("variance of the data: \n", df.var())
    print("standard deviation of the data: \n", df.std())

    # x is our treatment group and purchase is our outcome variable
    x = df['test']
    purchase = df['purchase']

    n_control = df[df['test'] == 0].shape[0]
    n_treatment = df[df['test'] == 1].shape[0]
    n_control_purchase = df[(df['test'] == 0) & (df['purchase'] == 1)].shape[0]
    n_treatment_purchase = df[(df['test'] == 1) & (df['purchase'] == 1)].shape[0]

    print("number of control rows:", n_control)
    print("number of treatment rows:", n_treatment)
    print("control purchases:", n_control_purchase)
    print("treatment purchases:", n_treatment_purchase)

    print("control conversion rate:", n_control_purchase / n_control)
    print("treatment conversion rate:", n_treatment_purchase / n_treatment)

    # hypothesis test that the conversion rate of treatment group is equal to the conversion rate of control group
    # because of the large sample size, we will use a z-test for this
    z_score = (n_treatment_purchase / n_treatment - n_control_purchase / n_control) / np.sqrt((n_treatment_purchase / n_treatment) * (1 - n_treatment_purchase / n_treatment) / n_treatment + (n_control_purchase / n_control) * (1 - n_control_purchase / n_control) / n_control)
    print("z-score:", z_score)

    # we will use a p-value to test the hypothesis
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    print("p-value:", p_value)

    confidence_interval = stats.norm.interval(0.95, 0, 1)


    is_causal = True
    # for causalility we need 

    # 1) X must be associated with Y
    is_test_associated_with_purchase = df['test'].corr(df['purchase'])
    print("test associated with purchase:", is_test_associated_with_purchase)
    if not is_test_associated_with_purchase:
        is_causal = False
        print("test is not associated with purchase, so it is not causal")
        exit()

    # 2) Temporal precedence: 
    # this is more of a qualitative question with how the experiment was conducted

    # 3) No Endogeneity:
    # this is more of a qualitative question with how the experiment was conducted

