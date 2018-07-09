#!/usr/bin/python3
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'../urls_parser/data/urls_2018-07-09.csv')
    df_gb = df.groupby('url').size()
    print(df_gb.to_string())