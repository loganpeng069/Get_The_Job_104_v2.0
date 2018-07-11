#!/usr/bin/python3
import requests
import re
from bs4 import BeautifulSoup as bs
# import pandas as pd
from time import sleep
from random import randint
from celery import Celery

app = Celery('main',)

class pageParser:
    def __init__(self,url):
        self.url = url
        self.resp = requests.get(url)
        sleep(randint(1,10))
        self.soup = bs(self.resp.text.replace('"',''))

    def get_name(self):
        name = self.soup.select('h1')[1].text.split('\n')[1].strip()
        #print(name, type(name))
        return name

    def get_company(self):
        company = self.soup.select('h1')[1].text.split('\n')[2]
        #print(company, type(company))
        return company

    def get_address(self):
        addr = self.soup.select('.addr')[0].text.split('\n')[1].strip()
        #print(addr, type(addr))
        return addr

    def get_location(self):
        loc = re.findall('var\ jlocation=\[(.+?),(.+?),',self.resp.text)[0]
        #print(loc, type(loc))
        return loc

    def get_content(self):
        cnt = self.soup.select_one("#job").find("div", {"class": 'content'}).p.text.strip().replace('\r','')
        #print(cnt, type(cnt))
        return cnt

    def get_tool(self):
        tl = self.soup.select('.tool')
        all_tl = ''
        for i in tl:
            all_tl += i.text + ' '
        #print(all_tl, type(all_tl))
        return all_tl

    def get_others(self):
        othr = self.soup.select('.content')[1].select('dd')[7].text.replace('\r',' ')
        #print(othr, type(othr), len(othr))
        return othr

    def printResult(self):
        self.get_name()
        self.get_company()
        self.get_address()
        self.get_location()
        self.get_content()
        self.get_tool()
        self.get_others()

def pageParserCreator(url):
    Page = pageParser(url) # init Page

    try:
        name = Page.get_name()
        com = Page.get_company()
        addr = Page.get_address()
        loc = Page.get_location()
        lat = loc[0]
        lon = loc[1]
        cnt = Page.get_content().replace(',',' ')
        tl = Page.get_tool().replace(',',' ')
        othr = Page.get_others().replace(',',' ')
        s = [name, com, addr, lat, lon, cnt, tl, othr]
        return s
    except:
        with open('data/error_1.txt','a',encoding='utf8') as f:
            f.write(url+'\n')
        return None
    finally:
        Page = None

if __name__ == '__main__':
    urls = ['https://www.104.com.tw/job/?jobno=695ve&jobsource=pda',
            'http://www.104.com.tw/job/?jobno=547dz&amp;jobsource=n104bank1',
            'http://www.104.com.tw/job/?jobno=5snph&amp;jobsource=n104bank1',
            'https://www.104.com.tw/job/?jobno=5v3r1&amp;jobsource=n104bank1',
            'http://www.104.com.tw/job/?jobno=6543k&amp;jobsource=n104bank1']

    df = pd.DataFrame(columns=['name','com','addr','loc','cnt','tl','othr'])
    for url in urls:
        print('-' * 20)
        s = pageParserCreator(url)
        print('-' * 20)
        print(s)
        df = df.append(s,ignore_index=True)
    print(df.head())
