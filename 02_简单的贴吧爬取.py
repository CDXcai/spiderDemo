# coding:utf8

import urllib
import urllib2
import random



def tieba_spider(kw, start_page, end_page):
    """
        作用:组建爬取贴吧网页函数
        参数:
            kw:贴吧名称
            start_page:开始页
            end_page:结束页
        :return:
    """
    # 要爬取的贴吧网址
    url = "http://tieba.baidu.com/f?"
    # 对贴吧名称编码
    kw = urllib.urlencode({'kw':kw})
    # 遍历页码，逐页爬取
    for index in range(start_page,end_page+1):
        # 当前页面的pn值
        pn  ='&pn=' + str((index-1) * 50)
        # 调用爬取函数
        tieba_load(url, kw, pn, index)

def tieba_load(url, kw, pn, index):
    """
        作用:爬取页面内容
        参数:
            url:链接地址
            kw:编码后的贴吧名称
            pn:页码参数
            index:第几页
        :return:
    """
    # User_Agent列表，用于反爬虫,也可以是代理列表
    ua_list = [
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
    # 构造页面URL
    fullurl = url + kw + pn
    # 随机选择User_Agent
    headers = {'User_Agent':random.choice(ua_list)}
    # 发送请求，读取页面
    request = urllib2.Request(fullurl,headers = headers)
    read = urllib2.urlopen(request).read()
    # 组建文件名
    filename = '02/第' + str(index) + '页.html'
    # 调用写文件函数
    tieba_file(read, filename)
def tieba_file(content, filename):
    """
        作用:用于保存爬取的网页到文件
        content:爬取的内容
        filename:文件名
        :return:
    """
    with open(filename,'w') as f:
        f.write(content)

if __name__ == "__main__":

    kw = raw_input("请输入你要爬取的贴吧")
    start_page = input("请输入要爬取的开始页")
    end_page = input("请输入爬取的结束页")

    # 调取处理函数，传递参数
    tieba_spider(kw, start_page, end_page)