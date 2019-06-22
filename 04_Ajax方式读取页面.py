# coding:utf8

import urllib
import urllib2
import random

# User_Agent列表，用于反爬虫,也可以是代理列表
ua_list=[
    # safari 5.1 – MAC
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    # safari 5.1 – Windows
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    # Firefox 4.0.1 – MAC
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    # IE 9.0
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    # Opera 11.11 – Windows
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    # Chrome 17.0 – MAC
    ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    # 傲游（Maxthon）
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'
]

# 随机选择一个User_Agent,(choice随机选择列表的一个元素)
user_agent = random.choice(ua_list)
headers = {"headers":user_agent}

# 通过抓取网页信息得到的url信息
"""https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="""
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="


# 模拟网页发送的表单数据
formdate = {
        "type":"11",
        "interval_id":"100:90",
        "action":"",
        "start":"20",
        "limit":"20"
    }
# 编码表单数据
data = urllib.urlencode(formdate)

# 构造请求
request = urllib2.Request(url,data = data,headers=headers)
# 发送请求
with open("Ajax爬取页面.txt", 'w') as f:
    f.write(urllib2.urlopen(request).read())