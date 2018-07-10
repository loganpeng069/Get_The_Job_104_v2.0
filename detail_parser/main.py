#!/usr/bin/python3
from pageDetailParserClass import pageParserCreator
from datetime import datetime
import pandas as pd
import concurrent.futures

if __name__ == '__main__':
    df = pd.DataFrame(columns=['name','com','addr','loc','cnt','tl','othr'])
    fus = []
    i = 1
    with open(r'../urls_parser/data/urls_2018-07-09.csv') as f:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            while f.readline != '':
                url = f.readline()
                fus.append(executor.submit(pageParserCreator,url))
                if i == 10:break

            for future in concurrent.futures.as_completed(fus):
                s = future.result()
                df = df.append(s, ignore_index=True)
            df.to_csv('./data/detail_().csv'.format(str(datetime.datetime.now().date())))

    #format(str(datetime.datetime.now().date()))


    #             s = pageParserCreator(url)
    #             print('-' * 20)
    #             df = df.append(s,ignore_index=True)
    #             if i == 20:
    #                 break
    # print(df)