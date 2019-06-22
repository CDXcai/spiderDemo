# coding:utf8

import urllib2
import random

# 将要爬取的网址
url = 'http://www.baidu.com'

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



# 构造一个请求
request = urllib2.Request(url)
# add_header 用于添加HTTP报头
request.add_header('User-Agent',user_agent)
# get_header 获取已有的HTTP报头值，只能第一个字母为大写，后面的必须为小写
print request.get_header('User-agent')