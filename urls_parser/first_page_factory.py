#!/usr/bin/python3
from pprint import pprint

def pageChangerProducer(url):
    pageLoc = url.find('page=') + 5
    modeLoc = url.find('&mode')
    url[pageLoc:modeLoc]
    first_url = url[:pageLoc]+'{}'+url[modeLoc:]
    return first_url

if __name__ == '__main__':
    # test

    '''
    fist_urls = [
        "https://www.104.com.tw/jobs/search/?ro=1&jobcat=2007000000&kwop=7&keyword=%E8%B3%87%E6%96%99&area=6001001000&order=1&asc=0&page={}&mode=s&jobsource=n104bank1",
        "https://www.104.com.tw/page=jobs/search/?keyword=python&area=6001001000&cat=2007000000&jobsource=n104bank1&ro=0&utm_expid=.wOIKurhAT7W2a_9l9WMmMw.0&utm_referrer=https%3A%2F%2Fwww.104.com.tw%2Fjobbank%2Fcustjob%2Findex.php%3Fr%3Dcust%26j%3D3c3a426b386c492134683a63303e365f2383a426b34363e673c423a1d1d1d1d1a745603e6b88j99%26jobsource%3Dn104bank1",
        "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&keyword=hadoop&area=6001001000&order=1&asc=0&page=1&mode=s&jobsource=n104bank1",
        "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&keyword=%E6%95%B8%E6%93%9A&area=6001001000&order=1&asc=0&page=1&mode=s&jobsource=n104bank1"]
    '''
    pprint([pageChangerProducer(url) for url in first_urls])
