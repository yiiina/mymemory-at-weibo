#-*-coding:utf8-*-

import re

import os

from bs4 import BeautifulSoup
from lxml import etree
import requests
import json
import base64



def cn_get_login_cookie(username, password):
    username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    result_login=0
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    session = requests.Session()
    res = session.post(loginURL, data = postData)
    jsonStr = res.content.decode('gbk')
    info = json.loads(jsonStr)
    if info["retcode"] == "0":
        result_login=1
        #print('succeed')
        cookies = session.cookies.get_dict()
        cookies = [key + "=" + value for key, value in cookies.items()]
        cookies = "; ".join(cookies)
    else:
        result_login=0
        cookies=0
        #print('fail: %s' % info["reason"])
    cookie = {"Cookie": cookies}
    #url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id
    return cookie,result_login

def cn_get_SelfId(cookie):#通过cookies访问，获取自己的id号
    url = 'http://weibo.cn/'
    html = requests.get(url, cookies = cookie).content
    Self_User_id=re.findall('a href="/(\d*)/follow"' , html.decode())[0]
    #print(Self_User_id)
    return Self_User_id

def com_get_ELseId(url,cookie):#通过cookies和url访问要保存的微博网址，获取自己的id号
    html = requests.get(url, cookies = cookie).content
    #print(html.decode())
    Else_User_id=re.findall('CONFIG\[\'oid\'\]=\'(\d*)\'', html.decode())[0]
    #print(Else_User_id)
    return Else_User_id



def get_page(cookie,user_id):

    url = 'http://weibo.cn/%d/profile?page=2'% user_id
    html = requests.get(url,cookies=cookie).content

    selector = etree.HTML(html)
    pagenum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
    #print(pagenum)
    #pagenum=5
    #获取lxml页面
    for page in range(1,pagenum+1):
        url = 'http://weibo.cn/%d/profile?page=%d'%(user_id,page)
        lxml = requests.get(url,cookies=cookie).content.decode('utf-8')
        soup = BeautifulSoup(lxml, "lxml")
        #print(soup.prettify())
        targetDir='/Users/Yina/Desktop/mymemory-at-weibo/weibo_to_doc/weibo_to_doc/'
        if not os.path.isdir(targetDir):
            os.mkdir(targetDir)
        fp = open(targetDir+'%d.txt'%page , 'w' , encoding = 'utf-8')
        fp.write(soup.prettify())
        #lxml.writexml(fp,encoding = 'utf-8')
        fp.close()

    return(pagenum)

