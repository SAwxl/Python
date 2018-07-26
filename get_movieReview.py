# -*- coding: utf-8 -*-
'''
Created on 2018-07-20

@author: Xiale Wu
'''

import urllib
import re
import HTMLParser
import json
import excel
import os
from bs4 import BeautifulSoup

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

path = "./"
excel_name = "douban_hot_review.xls"
mkdir(path)
url = 'http://movie.douban.com/review/best/?start='
sheet_name = '豆瓣最新影评'
column = ['影片', '作者', '标题', '影评']

douban_excel = excel.Excel(excel_name, sheet_name)


# 将HTML中的转义字符转换成普通字符
def html_parser(s):
    html_parser = HTMLParser.HTMLParser()
    return str(html_parser.unescape(s))


# 获取URL的源代码
def get_url(url, Page, step):
    url2 = url + str(x * 20)
    return url2


def get_movie_review(x):
    url2 = get_url(url, x, 20)   #我们要取start=0、20、40
    html = urllib.urlopen(url2)
    soup = BeautifulSoup(html, "lxml")
    #data = soup.prettify()
    location = soup.body.find('div', id = 'wrapper')
    location = location.find('div', id = 'content')
    location = location.find('div', class_ = 'grid-16-8 clearfix')
    location = location.find('div', class_ = 'article')
    location = location.find('div', class_ = 'review-list chart ')
    location = location.find_all('div', typeof = 'v:Review')
    for element in location:
        element = element.find('div', class_ = 'main review-item')

    pattern_subject = re.compile(r'<img alt="(.+)" rel=')
    pattern_people = re.compile(r'<a class="name" href=".+people.+">(.+)</a>')
    pattern_title = re.compile(r'<a.+review.+/">(.+)</a>')
    pattern_description = re.compile(r'<div class="short-content">[<p class="spoiler-tip">这篇影评可能有剧透</p>]?(.+)\(<a', re.DOTALL)



    for element in location:
        s_1 = re.search(pattern_subject, str(element))
        list_subject.append(s_1.group(1))

        s_2 = re.search(pattern_people, str(element))
        list_people.append(s_2.group(1))

        s_3 = re.search(pattern_title, str(element))
        list_title.append(s_3.group(1))

        s_4 = re.search(pattern_description, str(element))
        s_4 = s_4.group(1)
        s_4 = s_4.replace('<p class="spoiler-tip">这篇影评可能有剧透</p>', '')
        s_4 = s_4.replace(' ', '')
        s_4 = s_4.replace('\n', '')
        list_description.append(s_4)



    print '----------写excel开始----------'
    for row in range(0, len(list_title)):
        if row == 0:
            print '----------获取第' + str(row + 1) + '个影评开始----------'
            douban_excel.write(row, 0, column[0])
            douban_excel.write(row, 1, column[1])
            douban_excel.write(row, 2, column[2])
            douban_excel.write(row, 3, column[3])
            douban_excel.write(row + 1, 0, html_parser(list_subject[row]))
            douban_excel.write(row + 1, 1, html_parser(list_people[row]))
            douban_excel.write(row + 1, 2, html_parser(list_title[row]))
            douban_excel.write(row + 1, 3, html_parser(list_description[row]))
            print '影片：', html_parser(list_subject[row])
            print '作者：', html_parser(list_people[row])
            print '标题：', html_parser(list_title[row])
            print '影评：', html_parser(list_description[row])
            print '----------获取第' + str(row + 1) + '个影评结束----------\n'
        else:
            print '----------获取第' + str(row + 1) + '个影评开始----------'
            douban_excel.write(row + 1, 0, html_parser(list_subject[row]))
            douban_excel.write(row + 1, 1, html_parser(list_people[row]))
            douban_excel.write(row + 1, 2, html_parser(list_title[row]))
            douban_excel.write(row + 1, 3, html_parser(list_description[row]))
            print '影片:', html_parser(list_subject[row])
            print '作者:', html_parser(list_people[row])
            print '标题:', html_parser(list_title[row])
            print '影评:', html_parser(list_description[row])
            print '----------获取第' + str(row + 1) + '个影评结束----------\n'

    print '----------写excel结束,路径：' + path + excel_name + '----------'

    douban_excel.save()

list_subject = []#影片
list_people = []#作者
list_title = []#标题
list_description = []#影评
for x in range(0, 3):   #每次只考虑一个页面，这样在进行正则表达式匹配，将结果存入建立列表时，就无需考虑“列表中的列表”
    get_movie_review(x)