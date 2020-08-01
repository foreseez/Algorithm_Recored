"""
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
    import requests

    for url in urls:
        print(url)

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.teI have the undergraduate and master's study experience in engineering majors, and I am familiar with computer programming, data visualization, and proficient use of MS, big data processing capabilities, and fast learning capabilities. I will use my professional expertise to help Deloitte come up with better solutions, automation and artificial intelligence (AI) functions to discover hidden relationships in the large amounts of data in the organization. Implementing the right strategy and technology will balance speed, cost, and quality to provide measurable business value.xt, 'lxml')
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
"""
# n = int(input().strip())
# res = []
# for _ in range(n):
#     res.append(list(map(int,input().strip().split())))
#
# print(res)

#
# N = int(input().strip())
# data = []
# for _ in range(N):
#     data.append(list(map(int, input().strip().split())))
#     print(data
#           )

"""
20200801 猿辅导笔试题
思路是先把区间排序，再把区间的开始和结束分别用不同的数字标记，比如0代表开始，1代表结束。
一个count初始化为0，每遇到0(也就是区间开始)时+1，同时计算最大的count(即是结果)，遇到1（也就是区间结束）时-1。
现在细想思路并不难，主要是这个排序的Comparator花了点时间，不熟练。

"""
data = [[1,4],[1,2],[2,3],[3,4]]
times = set()
change = {}
for course in data:
    times.add(course[0])
    times.add(course[1])
    # print(times)
    # 1:2,4:-1 ,2:0,3:-1
    # 1:2,4:-2 2:0,3:0

    change[course[0]] = change.get(course[0], 0) + 1
    change[course[1]] = change.get(course[1], 0) - 1
print(change)
print(times)
res = 0
cur = 0
# times = {1,2,3,4}
# change = {1:2,4:-2 2:0,3:0}
for time in times:
    cur += change[time] # cur = 2,res=2,cur = 2,res=2,cur = 2,res=2,cur = 0,res = 2
    res = max(cur, res)
print(res)

# array.get(arr[0],0)+1