# -*- coding: utf-8 -*-
class HtmlOutputer(object):

    def __init__(self):
        #以一个列表存数据,并且解析出来的数据也是列表,且会在程序周期里保存，一个比较大的数据
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html><meta charset=\"utf-8\" />")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))

            
            fout.write("</tr>")

        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        print "写入成功"

        fout.close()
