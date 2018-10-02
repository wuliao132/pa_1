# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

    def _get_new_urls(self,page_url, soup):
        new_urls = set()

        links = soup.find_all("a", href=re.compile(r"/item/(.*)"))
        for link in links:
            new_url = link['href']
            #对url进行补全处理
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        #也就是说在主2函数里接受到的是一个元组
        return new_urls


    def _get_new_data(self,page_url,soup):
        #要获取两种信息
        res_data = {}

        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
#       #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

        


    #返回数据和新的url，参数是HTML页面和最近的URL，使用的方法是
    #_get_new_urls()和_get_new_data()两种
    #因为从HTNL里解析出的url是不完整的
    def parse(self, page_url, html_cont):

        if page_url is None or html_cont is None:
            return
        #煲汤，使用HTML，html.parser,编码方式 煲汤
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)

        return new_urls, new_data

        
