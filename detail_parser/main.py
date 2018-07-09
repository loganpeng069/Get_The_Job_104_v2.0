#!/usr/bin/python3
import pandas as pd

if __name__ == '__main__':
    with open(r'../urls_parser/data/urls_2018-07-09.csv') as f:
        line = f.readline()
        print(line)