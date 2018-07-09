#!/usr/bin/python3
import requests
import re
from bs4 import BeautifulSoup as bs

class pagePaser:
    url = None
    resp = None
    soup = None
    def __init__(self,url):
        self.url = url
        self.resp = requests.get(url)
        self.soup = bs(self.resp.text.replace('"',''))

    def get_name(self):
        name = self.soup.select('h1')[1].text.split('\n')[1].strip()
        print(name,type(name))

    def get_company(self):
        company = self.soup.select('h1')[1].text.split('\n')[2]
        print(company,type(company))

    def get_address(self):
        addr = self.soup.select('.addr')[0].text.split('\n')[1].strip()
        print(addr,type(addr))

    def get_location(self):
        loc = re.findall('var\ jlocation=\[(.+?),(.+?),',self.resp.text)[0]
        print(loc,type(loc))

    def get_content(self):
        cnt = self.soup.select_one("#job").find("div", {"class": 'content'}).p.text.strip().replace('\r','')
        print(cnt)

    def get_tool(self):
        tl = self.soup.select('.tool')
        all_tl = ''
        for i in tl:
            all_tl += i.text + ' '
            print(all_tl,type(i))

    def get_others(self):
        #othr = self.soup.findAll("dd")[5]
        # othr = othrs[5]
        othr = self.soup.select('.content')[1].select('dd')[7].text
        # othr = re.findall('<dt>其他條件：</dt><dd>.</dd>',self.resp.text.replace('\n',''))
        print(othr,type(othr),len(othr))
        print('-'*20)
        #print(self.resp.text)

if __name__ == '__main__':
    urls = ['https://www.104.com.tw/job/?jobno=695ve&jobsource=pda',
            'http://www.104.com.tw/job/?jobno=547dz&amp;jobsource=n104bank1',
            'http://www.104.com.tw/job/?jobno=5snph&amp;jobsource=n104bank1',
            'https://www.104.com.tw/job/?jobno=5v3r1&amp;jobsource=n104bank1']
    for url in urls:
        Page = pagePaser(url)
        Page.get_name()
        Page.get_company()
        Page.get_address()
        Page.get_location()
        Page.get_content()
        Page.get_tool()
        Page.get_others()