#!/usr/bin/python3
import requests
import json
# from bs4 import BeautifulSoup
import re
import concurrent.futures
import datetime
from time import sleep

def urlsParser(url):
    headers = json.loads(r'''{
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.3.315699719.1530244249; __auc=a8cc166516449aa3656fd01f442; luauid=192379996; CS=fddbaa306d8c4c57879a7141c6149bcd; LS=6b3b318f-d5bb-4758-987c-312dc5a3a9b1; EPK=1ba150dfbc9dc68cf752b8002fead6b90; PERSONAL_SORT=B; SYS_SETAB=20140613; JBCLOGIN=1; _gid=GA1.3.631718459.1531021816; JBCSID=ml5fvrju2ekhqninvqclqh1fh7; _gaexp=GAX1.3.wOIKurhAT7W2a_9l9WMmMw.17810.0; aidma_b_622_255=2; lup=192379996.4621384808344.4623532291991.1.4640712161167; lunp=4623532291991; __asc=5f2a62b21647ad78f1d7d618ba9; bubble=318_40_174_233_0_0_0_0",
        "Host": "www.104.com.tw",
        "Referer": "https://www.104.com.tw/jobs/search/?ro=0&keyword=%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B&area=6001001000&order=1&asc=0&page=1&mode=s&jobsource=n104bank1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }''')

    resp = requests.get(url, headers=headers)
    sleep(5)
    html = resp.text
    urls = ['http:' + url for url in re.findall('<a href="(.+?)" class="js-job-link " target="_blank">', html)]
    return urls


if __name__ == '__main__':
    first_url = ["https://www.104.com.tw/jobs/search/?ro=1&jobcat=2007000000&kwop=7&keyword=%E8%B3%87%E6%96%99&area=6001001000&order=1&asc=0&page={}&mode=s&jobsource=n104bank1",
                 "2"]

    fus = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for page_num in range(1, 150):
            url = first_url[0].format(page_num)
            fus.append(executor.submit(urlsParser, url))

        for future in concurrent.futures.as_completed(fus):
            print(future.result())
            with open('./data/urls_'+str(datetime.datetime.now().date()),'a',encoding='utf8') as f:
                for url in future.result():
                    f.write(url+'\n')

'''
https://www.104.com.tw/jobs/search/?ro=1&jobcat=2007000000&keyword=%E8%B3%87%E6%96%99&area=6001001000&order=1&asc=0&page=1&mode=l&jobsource=n104bank1
<a href="//www.104.com.tw/job/?jobno=3tpkt&amp;jobsource=hotjob_chr" class="js-job-link " target="_blank">【Head Office】IT助理/專員</a>
'''
