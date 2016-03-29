#/usr/bin/env python
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):  #处理开始标签，比如<xx>
        print('<%s>' % tag)

    def handle_endtag(self, tag):  #处理结束标签，比如</xx>
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs): #处理开始标签和结束标签
        print('<%s/>' % tag)

    def handle_data(self, data):  #处理数据，就是<xx>data</xx>中间的那些数据
        print(data)

    def handle_comment(self, data):  #处理注释
        print('<!--', data, '-->')

    def handle_entityref(self, name): #处理特殊字符以&开头的，比如 &nbsp;
        print('&%s;' % name)

    def handle_charref(self, name): #处理特殊字符串，就是以&#开头的，一般是内码表示的字符
        print('&#%s;' % name)

    def handle_decl(self, decl):  #处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        print('<!%s;' % decl)

    def handle_pi(self, data):  #处理形如<?instruction>的东西

        print('<?instruction>%s' %data)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

