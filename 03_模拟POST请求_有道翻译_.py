#coding:utf8
import urllib
import urllib2



key = raw_input("请输入要翻译的汉字")


# url请求的实际地址，需要用抓包工具获取,http://fanyi.youdao.com/只是接口地址
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

# 需要发送的POST数据
data = {
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_CLICKBUTTION"
}

data = urllib.urlencode(data)

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
# 请求头参数
headers = {
    "Host": " fanyi.youdao.com",
    "Connection": " keep-alive",
    "Content-Length": "100",
    "Accept": " application/json, text/javascript, */*; q=0.01",
    "Origin": "http：//fanyi.youdao.com",
    "X-Requested-With": " XMLHttpRequest",
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http：//fanyi.youdao.com/",
    "Accept-Language": " zh-CN,zh;q=0.9"

}
print data
# 构造Response对象，三个参数url data headers 有data参数就表示发送POST请求
response = urllib2.Request(url,data = data,headers = headers)

print urllib2.urlopen(response).read()