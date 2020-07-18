# 爬取瞬眼天下网页多页的小标题
import requests
from bs4 import BeautifulSoup
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

baseurl = 'http://www.luxian.gov.cn/zwgk/zwdt/jcdt_'
urls = []

filename = './yunji888n.txt'  # 需要保存的位置
with open(filename, 'w', encoding='utf-8') as f:
    for page in range(1, 10):
        allurl = baseurl + str(page)
        urls.append(allurl)
    print(urls)

    for url in urls:
        print(url)

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        # html = response.read()
        # selector = etree.HTML(resp)
        # 核心部分
        # bloger = selector.xpath("//div[@class=mBd']/ul/li/a")[0].text.encode('utf-8').strip()
        # print(bloger)
        alla = soup.find_all('ul', class_='newsList')
        # print(alla)
        # print(len(alla))
        for a in alla:
            t = a.find_all('a')
            # print(len(t))
            # print(type(t))
            # print(t)
            for title in t:
                # print(title)
                print(title.get_text().strip())
                f.writelines(title.get_text().strip()+"\n")
            # f.writelines(t.get_text().strip() + '\n')

    print('success')