# coding:utf8

import urllib
import urllib2
import random
# 比如搜索耳机，百度的url会有 wd=%e8%80%b3%e6%9c%ba ,wd为get请求的键,%e8%80%b3%e6%9c%ba是耳机编码后的结果


# 构造链接地址
url = "http://www.baidu.com/s?"

# 构造查询关键字
keyword = '耳机'
# 转化为编码  将字典转化为  wd=%e8%80%b3%e6%9c%ba
wd = {'wd':keyword}
# 通过urlencode编码,参数是字典类型的，
wd = urllib.urlencode(wd)


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

# 组合url链接和GET参数
url = url+wd

# 编辑User-Agent请求头参数
headers = {'User-Agent':random.choice(ua_list)}
request = urllib2.Request(url,headers=headers)
print url
# 发送请求

lib = urllib2.urlopen(request).read()

f = open('测试.txt','w')
f.write('hello')
f.close()