#!/usr/bin/python3
from muti_Parser import mutiParserUrls
# from job_urls import urlsParser
from first_page_factory import pageChangerProducer
from time import sleep
'''
Prepare different results after querying on 104.
----------------
keyword,endpage
0. 資料,150
1. python,63
2. hadoop,9
3. 數據,41
----------------
'''
if __name__ == '__main__':
    first_urls = [("https://www.104.com.tw/jobs/search/?ro=1&jobcat=2007000000&kwop=7&keyword=%E8%B3%87%E6%96%99&area=6001001000&order=1&asc=0&page={}&mode=s&jobsource=n104bank1",150),
                  ("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&kwop=7&keyword=python&area=6001001000&order=1&asc=0&page=2&mode=s&jobsource=n104bank1",63),
                  ("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&kwop=7&keyword=hadoop&area=6001001000&order=1&asc=0&page=2&mode=s&jobsource=n104bank1",9),
                  ("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&kwop=7&keyword=%E6%95%B8%E6%93%9A&area=6001001000&order=1&asc=0&page=7&mode=s&jobsource=n104bank1",41)]
    # single one
    # url = first_urls[1]
    # mutiParserUrls(pageChangerProducer(url[0]), url[1])

    # iterate
    for url in first_urls:
        mutiParserUrls(pageChangerProducer(url[0]),url[1])
        print(url)
        #sleep(3)