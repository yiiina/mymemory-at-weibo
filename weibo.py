#-*-coding:utf8-*-
 
import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree
 
reload(sys) 
sys.setdefaultencoding('utf-8')

user_id = (int)(raw_input(u"请输入user_id: ")) 
cookie = {"Cookie": "SCF=AgJWFBFuib9sGbc2FlXQGoVxPfkmkp1dHwJ6g6CqgmwWRzmViS3KmGPaX_j9h92dZORr9oTIo4JIjIcZ7eZgJ8Q.; SUHB=0WGdD9fMmfsh5B; _T_WM=8064c7b9df5de10409fd2b0f82a1ad8c; SUB=_2A251wWmDDeRxGedJ7lcS9ibNyj2IHXVXSnfLrDV6PUJbkdANLXfXkW1gfK0rEq1BlnEEat9YzZO5gILraA..; gsid_CTandWM=4u3m48131eRlhgML5dhOd7mEo1N; PHPSESSID=d5f910da4b2aae3a83ca9fd6e19a3cef"}
url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id
 
html = requests.get(url, cookies = cookie).content
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
 
result = "" 
word_count = 1
 
print u'爬虫准备就绪...'
 
for page in range(1,pageNum+1):
 
  #获取lxml页面
  url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page) 
  lxml = requests.get(url, cookies = cookie).content
 
  #文字爬取
  selector = etree.HTML(lxml)
  content = selector.xpath('//span[@class="ctt"]')
  for each in content:
    text = each.xpath('string(.)')
    if word_count >= 4:
      text = "%d :"%(word_count-3) +text+"\n\n"
    else :
      text = text+"\n\n"
    result = result + text
    word_count += 1
 
fo = open("/Users/Yina/Desktop/mymemory-at-weibo/%s"%user_id, "wb")
fo.write(result)
word_path=os.getcwd()+'/%d'%user_id
print u'文字微博爬取完毕'

print u'原创微博爬取完毕，共%d条，保存路径%s'%(word_count-4,word_path)