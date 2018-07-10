#!/usr/bin/python3
from pageDetailPaserClass import pageParser

if __name__ == '__main__':
    urls = ['https://www.104.com.tw/job/?jobno=601rg&jobsource=pda',
            'https://www.104.com.tw/job/?jobno=61i80&jobsource=pda',
            'https://www.104.com.tw/job/?jobno=69ypa&jobsource=vip',
	    'https://www.104.com.tw/job/?jobno=3bw8l&jobsource=pda_i']

    for url in urls:
        Page = pageParser(url)
        Page.printResult()
