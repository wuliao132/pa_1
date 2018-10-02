# -*- coding: utf-8 -*-
#引入四个模块,分别是管理，下载，解析，输出
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    #初始化变量
    def __init__(self):
        self.urls = url_manager.UrlManager()#url管理器
        self.downloader = html_downloader.HtmlDownloader()#html下载器
        self.parser = html_parser.HtmlParser()#html解析器
        self.outputer = html_outputer.HtmlOutputer()#最终结果的输出器

    #执行主函数,有一个参数
    def craw(self, root_url):
        #计数器设置
        count = 1
        #先给主体一个启动条件,使用url管理器的url添加函数add_new_url()
        self.urls.add_new_url(root_url)
        #使用url管理器的判断有无新url方法has_new_url()
        while self.urls.has_new_url():
            try:
                #使用url管理器的从新urls set()获取一个还未下载和解析的url
                new_url = self.urls.get_new_url()
                #输出该url
                print "craw %d : %s" % (count, new_url)
                #然后使用url下载器，对url进行下载,返回一个html页面
                html_cont = self.downloader.download(new_url)
                #使用html解析器，对html进行解析，查找出要找的new_url和new_data
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                #使用url管理器处理新url，使用add_new_urls()方法
                self.urls.add_new_urls(new_urls)
                #使用输出器对new_data进行处理
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count += 1
                
            except Exception as e:
                print "craw failed--", e

        #输出搜集好的数据
        self.outputer.output_html()

if __name__ == "__main__":

    #这个貌似有变化，现在可行
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
