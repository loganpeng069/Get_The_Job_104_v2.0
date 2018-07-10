#!/usr/bin/python3
from pageDetailPaserClass import pagePaser

if __name__ == '__main__':
    with open(r'../urls_parser/data/urls_2018-07-09.csv') as f:
        for i in range(10):
            line = f.readline()
            pagePaser(line).printResult()
    print(line)