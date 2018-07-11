#!/usr/bin/python3
from pageDetailParserClass import pageParserCreator
from datetime import datetime
import csv
import concurrent.futures
import sys

if __name__ == '__main__':
    #df = pd.DataFrame(columns=['name','com','addr','loc','cnt','tl','othr'])
    fus = []
    i = 1
    j = 1
    a = 'urls_2018-07-09.csv'
    fileIn = sys.argv[1]
    fileOut = sys.argv[2]
    fileWriter = csv.writer(open(fileOut,'a'), delimiter=',')
    with open(fileIn) as f:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            while True:
                url = f.readline().strip()
                if url == '':break
                print(url)
                fus.append(executor.submit(pageParserCreator,url))
                if i == 10:break
                i += 1
                print(i)

            for future in concurrent.futures.as_completed(fus):
                row = future.result()
                print(row)
                if row != None:
                    fileWriter.writerow(row)
                print(j)
                j += 1

    #format(str(datetime.datetime.now().date()))


    #             s = pageParserCreator(url)
    #             print('-' * 20)
    #             df = df.append(s,ignore_index=True)
    #             if i == 20:
    #                 break
    # print(df)