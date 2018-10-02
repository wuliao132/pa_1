# -*- coding: utf-8 -*-
import urllib2
class HtmlDownloader(object):
    #这个函数只有一个功能，就是下载HTML页面
    def download(self,url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
