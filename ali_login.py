#coding=utf-8

import urllib2
import time
import json
from lxml import etree

from selenium import webdriver
import requests
import random

# print(random.randint(0,10))


# heards = {
#     'Referer': 'https://login.aliexpress.com/',
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
#
# htmlll = requests.get(loginurl,headers=heards)
# print htmlll.text


# try:
#     sel.find_element_by_id("fm-login-id").send_keys('184845217@qq.com')
#     # print sel.find_element_by_id("fm-login-id")
#     # sel.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("184845217@qq.com")
#     print 'user success!'
# except Exception, e:
#     print str(e)
#     print 'user error!'
# time.sleep(1)
#
# try:
#     # sel.find_element_by_id("fm-login-password").send_keys('141242545')
#     sel.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("141242545")
#     print 'pw success!'
# except:
#     print 'pw error!'
# time.sleep(1)
#
# # 登录
# try:
#     # sel.find_element_by_id("fm-login-submit").click()
#     sel.find_element_by_xpath("//*[@id='fm-login-submit']").click()
#     print 'click success!'
# except:
#     print 'click error!'
# time.sleep(1)
# div_list = sel.find_elements_by_xpath("//div[@class='cg-main']/div")
# print(div_list)


# print("111")
# # 跳转到产品目录
# html2 = 'https://www.aliexpress.com/all-wholesale-products.html'
# sel.get(html2)
#
# # tree = etree.HTML(html2)
# # title = tree.xpath('//ul[@class="sub-item-cont util-clearfix"]/li/a/text()')
#
#
# title = sel.find_element_by_xpath("//span[@class='desc']//text()")
# print(type(title))
# print(title)


def handleLogin():

    sel = webdriver.Firefox()
    loginurl = 'https://login.aliexpress.com/'
    # loginurl = 'https://www.aliexpress.com/all-wholesale-products.html'
    sel.get(loginurl)
    sel.switch_to.frame('alibaba-login-box')
    time.sleep(1)

    # 模拟登录
    sel.find_element_by_id("fm-login-id").send_keys('')
    sel.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("")
    sel.find_element_by_xpath("//*[@id='fm-login-submit']").click()
    # print("登录成功")

    # print type(sel.get_cookies()) # list
    print(sel.get_cookies())
    print type(sel.get_cookies()) #list


    # # 添加cookie
    # sel.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbb'})

    # key-value打印 查看
    for cookie in sel.get_cookies():
        print "%s : %s" % (cookie['name'], cookie['value'])

    # file_handle = open('/home/lj/file/sumaitong/cookies.txt', mode='w')
    # file_handle.write(sel.get_cookies())

    # cookies处理
    f = open(r'/home/lj/file/sumaitong/cookies.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(':'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    print('cookie划分成功')

    # return sel,sel.get_cookies()[0]
    return sel,cookies





if __name__ == '__main__':
    category_all = 'https://www.aliexpress.com/all-wholesale-products.html'
    sel,cookie = handleLogin()
    print('打印cookie')

    html = requests.get(category_all, cookies=cookie)  #字典
    print(cookie)
    print('123456')

    # html = requests.get(category_all)

    if "alibaba-login-box" in html.text:
        cookie = handleLogin()
    else:
        # html.caegory,url
        # html = requests.get(category_all, cookie=cookie)
        title = sel.find_element_by_xpath("//h3[@class='big-title anchor1 anchor-agricuture']/a").text
        title_links = sel.find_element_by_xpath("//h3[@class='big-title anchor1 anchor-agricuture']/a").get_attribute(href)
    print(title)
    print(title_links)

    #     f1 = open("/home/lj/file/sumaitong/ss.csv","w")
    #     f1.write({"Women's Clothing & Accessories":'www.aliexpress.com/category/100003109/women-clothing-accessories.html?spm=2114.search0101.1.1.20b248b6VDRihf&g=y'})
    # requests.get('www.aliexpress.com/category/100003109/women-clothing-accessories.html?spm=2114.search0101.1.1.20b248b6VDRihf&g=y')


    print("执行成功")
