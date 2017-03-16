# 项目思路 

### 处理微博的反爬虫技术

新浪微博的页面都是通过加密处理的吧,无法通过bs等来直接获取，尝试一下手机端的页面http://weibo.cn   

https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F

### 网上找到一个已有的轮子，功能符合我的需求,先尝试一下

#### 安装之前没有，这个程序中需要用到的模块和`lxml`和`beautifulsoup4`
```
jiangyinadeMacBook-Pro:mymemory-at-weibo Yina$ pip install lxml
Collecting lxml
  Downloading lxml-3.7.3.tar.gz (3.8MB)
    100% |████████████████████████████████| 3.8MB 30kB/s 
Installing collected packages: lxml
  Running setup.py install for lxml ... done
Successfully installed lxml-3.7.3
```

```
jiangyinadeMacBook-Pro:mymemory-at-weibo Yina$ pip install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.5.3-py2-none-any.whl (85kB)
    100% |████████████████████████████████| 92kB 50kB/s 
Installing collected packages: beautifulsoup4
Successfully installed beautifulsoup4-4.5.3
```



#### 先尝试运行，根据报错，更换文件路径
`/Users/Personals/`换成`/Users/Yina/Desktop/mymemory-at-weibo`

```
jiangyinadeMacBook-Pro:mymemory-at-weibo Yina$ python weibo2.py
请输入user_id: 1755368111
爬虫准备就绪...
Traceback (most recent call last):
  File "weibo2.py", line 60, in <module>
    fo = open("/Users/Personals/%s"%user_id, "wb")
IOError: [Errno 2] No such file or directory: '/Users/Personals/1755368111'
jiangyinadeMacBook-Pro:mymemory-at-weibo Yina$ 
jiangyinadeMacBook-Pro:mymemory-at-weibo Yina$ pwd
/Users/Yina/Desktop/mymemory-at-weibo

```

#### 虽然可以运行，没有报错，但是运行的时间也太长，可能是图片太多跑不通，先简化项目，删除图片相关的之后，形成了一个最小的可执行流程
```
jiangyinadeMacBook-Pro:mymemory-at-weibo Yina$ python weibo3.py
请输入user_id: 1755368111
# 爬虫准备就绪...
文字微博爬取完毕
原创微博爬取完毕，共497条，保存路径/Users/Yina/Desktop/mymemory-at-weibo/1755368111
```
#### 虽然可以运行，但是有问题。首先，爬取的内容是错误的，不是我自己的内容，好像是timeline上的内容；其次，不可重复，重新再来，换一个id会报错
```
jiangyinadeMacBook-Pro:mymemory-at-weibo Yina$ python weibo3.py
请输入user_id: 3168835504      
Traceback (most recent call last):
  File "weibo3.py", line 22, in <module>
    pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
IndexError: list index out of range
``` 

上面这行是：`etree.HTML`这个函数
	selector = etree.HTML(html)
	


#### 这个问题触发了一些认知盲区,顺藤摸瓜，一一梳理:HTML,XML,Xpath,lxml,Bs4,BeautifulSoup

```
 pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
IndexError: list index out of range
```

### HTML,XML,Xpath,语言家族

#### HTML
HTML也是一种语言，和markdown比较像,只用来描述，没有方法和流程，HTML文档页也就是网页。

* 包含标签和纯文本。
* 形式：<标签>元素<标签/>
* 加入属性和值：<标签 属性><标签／>
* 缩写的形式：<标签 属性／>
    
属性包含一个名称和值的键：name="value"

#### XML
* XML是可扩展标记语言，用来传输和储存数据
* 没有预定义标签
* XML和HTML为不同的目的设计
* 应用于web开发，用于简化数据的存储和共享
*  通过JS，可以读取外部XML文件，然后更新HTML中的数据内容
*  在 XML 中，XML 的属性值须加引号`<note date="08/08/2008">...</note> `
*  一些字符有特殊意义，用实体引用代替

一个误会，其实微博打开源代码，是XML，不过之前提HMTL也不浪费，语法是类似的

```
<?xml version="1.0" encoding="UTF-8"?>
```

#### xpath语法 

Xpath是在XML文档中查找信息的语言，可用来在XML文档中对元素和属性进行遍历。
效率比较高的解析方法，这种语法在lxml的解析库中。
XPath使用路径表达式，在XML文档中选取节点，节点通过沿着路径或者step来选取.
谓语（predicates)用来查找某个特定的节点或者包含某个特定值的节点。 谓语放在[ ]中。

#### 用xpath查找我需要的信息

我在过去几年中写了一千多条微博，总共有107页，如果把所有内容都弄出来，需要一页一页去复制，非常非常低效。那么，我希望这个程序是：

* 爬取第1页的内容
* 爬取第2页的内容
* 爬取第3页的内容
 ……
* 爬去第107页的内容

这里有2个对象需要处理，页面和当页的文本内容。在html中，他们的元素分别是：
    
* 文本内容：`<span class="ctt"> 哈哈，明天和小青去逛园咯。。</span>`
    
    * 标签：span 
    * 属性：1个
        * 名称-值  chass="ctt"

* 页码：`<input name="mp" type="hidden" value="107" />`

    * 在html中，这个标签是输入，有3个属性，名称-值对应包括：
        * name-mp,
        * type-hidden
        * value-1-107

`<input>`这个标签用于搜集用户信息

* 这里的input type: “hidden” 表示，在 HTML 表单中 <input type="hidden"> 标签每出现一次，一个 Hidden 对象就会被创建
* 可通过遍历表单的 elements[ ] 数组来访问某个隐藏输入域，或者通过使用document.getElementById( )

再回头看出错的地方，是在页码这里：

```
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
```
xpath的路径表达式和对应的结果是`//input[@name="mp"][0]
`

意思是：不考虑位置，选取所有input元素，且这些元素有属性name为mp的属性，第0个


selector.xpath()[0].attrib['value']


attrib.['value']不知道是啥

看看selector是啥

selector = etree.HTML(html)
html = requests.get(url, cookies = cookie).content

这里触及的概念是:  ` etree from lxml`

### lxml,Bs4,BeautifulSoup 是导入的python库


#### lxml

lxml.etree它是用来处理XML流程的。

解析字符的方法：
etree.fromastring()
etree.XML()
etree.HTML()

那么，这里有一个地方需要改，就是把HTML()改成XML()吧

http://lxml.de/tutorial.html#the-xml-function


#### BeautifulSoup的bs4




#### requests这个模块之前接触过了，它就是很简单的和网页交互的模块。通过`renquests`获取网页信息

```
>>> import urllib
>>> import urllib2
>>> from bs4 import BeautifulSoup
>>> import requests
>>> from lxml import etree
>>> user_id = 1755368111
>>> int(user_id)
1755368111
>>> url='http://weibo.cn/u/%d'%user_id
>>> url
'http://weibo.cn/u/1755368111'
>>> requests.get(url)
<Response [200]>
>>> requests.get(url).content
'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD 
……
></div></form></div></body></html>'# 返回一堆html格式信息
```

这些html的格式需要整理，提取出我需要的内容。

#### 这里的页面是第一页,所有的页面的页面数目是一个range

默认第一页：http://weibo.cn/1755368111/profile
第一页
第二页：http://weibo.cn/1755368111/profile?page=2
第三页：http://weibo.cn/1755368111/profile?page=3
……
一共有107页
最后一页：http://weibo.cn/1755368111/profile?page=107

url='http://weibo.cn/u/%d/profile?page=%d'%(user_id,range(1,pageNum+1)):


