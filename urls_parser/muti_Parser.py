#!/usr/bin/python3
import concurrent.futures
import datetime
from job_urls import urlsParser
import os


def mutiParserUrls(first_url,end_page):
    fus = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for page_num in range(1, end_page):
            url = first_url.format(page_num)
            fus.append(executor.submit(urlsParser, url))

        for future in concurrent.futures.as_completed(fus):
            print(future.result())
            with open('data/urls_{}.csv'.format(str(datetime.datetime.now().date())),'a', encoding='utf8') as f:
                for url in future.result():
                    if 'hunter' in url:continue
                    if 'tutor' in url:continue
                    f.write(url + '\n')

if __name__ == '__main__':
    # test
    first_urls = \
        [
            "https://www.104.com.tw/jobs/search/?ro=1&jobcat=2007000000&kwop=7&keyword=%E8%B3%87%E6%96%99&area=6001001000&order=1&asc=0&page={}&mode=s&jobsource=n104bank1",
            "2"]
    first_url = first_urls[0]
    end_page = 150
    mutiParserUrls(first_url,end_page)