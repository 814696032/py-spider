#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import re
import os
import urllib
import lxml
from urllib import request,parse
from bs4 import BeautifulSoup

class Baidu_spider():
    def __init__(self):
        folders = os.path.exists('./image')
        if not folders:
            os.makedirs("image")

        keyword = input('输入关键字：')
        INIT = eval(input("从第几页开始爬取："))
        N = eval(input("爬取的页数(每页20张图)："))
        self.crawler_img(keyword,INIT,N)

    def crawler_img(self,keyword,INIT,N):
        son_folders = os.path.exists('/image/%s' %keyword)
        if not son_folders:
            os.makedirs('./image/%s' %keyword)
        keyword_encode = parse.quote(keyword)  # 可以把字符串编码为url的格式
        for page in range(INIT-1,N):
            pn = page*20
            url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword_encode + '&pn=%s' %pn
            url_request = request.Request(url)
            url_response = request.urlopen(url_request)  # 请求数据，可以和上一句合并
            html = url_response.read().decode('utf-8')  # 加编码，重要！转换为字符串编码，read()得到的是byte格式的。
            jpgList = re.findall('"objURL":"(.*?)",',html,re.S)  #re.S将字符串作为整体，在整体中进行匹配
            n = 1
            for each in jpgList:
                # print(each)  # 每个图片的下载地址
                try:
                    # print(n+pn)  # 图片编号
                    request.urlretrieve(each,'image/%s/%s.jpg' %(keyword,n+pn))
                    print("正在下载 %s / %s ..." %(n+pn,20*N))
                except Exception as e:
                    # print(e)
                    print("正在下载 %s / %s ..." % (n + pn, 20 * N))
                    print("第%s张图片下载失败" %(n+pn))
                n = n+1
                if n>20:
                    break
        print("下载完成！")


s = Baidu_spider()

