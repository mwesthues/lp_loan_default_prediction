import pandas as pd

from loanpred.clean import add_years_months


uri = 'https://raw.githubusercontent.com/nateGeorge/manning_random_forest_classifier_liveproject/master/loan_data.csv'
df = pd.read_csv(uri, index_col=0)
df['CREDIT_HISTORY_LENGTH'] = df['CREDIT_HISTORY_LENGTH'].map(add_years_months)
df['AVERAGE_ACCT_AGE'] = df['AVERAGE_ACCT_AGE'].map(add_years_months)
df['DATE_OF_BIRTH'] = pd.to_datetime(df['DATE_OF_BIRTH'])
df['DISBURSAL_DATE'] = pd.to_datetime(df['DISBURSAL_DATE'])
