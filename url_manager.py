# -*- coding: utf-8 -*-
class UrlManager(object):

    def __init__(self):
        #有新旧两种元组
        self.new_urls = set()
        self.old_urls = set()

    #添加源url,在循环外用了一次
    def add_new_url(self,url):
        if url is None:
            return

        #添加的url必须是全新的
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #判断self.new_urls中蜀否还有为爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #批量添加新的url,用到之前的add_new_url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        #可能解析出来的不止一个url
        for url in urls:
            self.add_new_url(url)

    #从new_urls中获取一个url，并把他添加到old_urls中去
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
