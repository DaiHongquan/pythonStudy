#网站的域名后加上/robots.txt查看robots协议，协议里最常出现的英文是Allow和Disallow，Allow代表可以被访问，Disallow代表禁止被访问
from matplotlib.pyplot import text
import requests
from bs4 import BeautifulSoup
import json

##设置代理
#proxies = {'http':'http://…'}
# ip地址
#response = requests.get(url,proxies=proxies)

#请求 文本并保存
# url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md'
# res = requests.get(url)#如果是图片等非文本资源使用res.content 获取二进制，res.status_code 值在200~300或304代表响应成功，res.encoding='gbk' 设置编码
# with open('httpStatus.txt','a',encoding='utf-8') as file:
#     file.write(res.text)


#BeautifulSoup解析数据，提取数据 soup.find(标签，属性)只提取首个满足要求的数据，而find_all()提取出的是所有满足要求的数据
# url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'html.parser') 
# item = soup.find('div') #使用find()方法提取首个<div>元素，并放到变量item
# items = soup.find_all(class_='books') #用find_all()把所有符合要求的数据提取出来，并放在变量items里
# #print(type(item)) #打印item的数据类型
# #Tag.find()/Tag.find_all()  Tag.text 提取Tag中的文字 Tag['属性名'] 提取属性值
# for item in items:
#     kind = item.find('h2') # 在列表中的每个元素里，匹配标签<h2>提取出数据
#     title = item.find(class_='title') #在列表中的每个元素里，匹配属性class_='title'提取出数据
#     brief = item.find(class_='info') #在列表中的每个元素里，匹配属性class_='info'提取出数据
#     print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text) # 打印书籍的类型、名字、链接和简介的文字


#每周热门菜谱  str = string.strip() # 去掉字符串string前后两端的空格

# url = 'https://www.xiachufang.com/explore/'
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'html.parser')  
# print(soup)
# items = soup.find_all('div',class_='cover pure-u') #使用find()方法提取首个<div>元素，并放到变量item 
# foods = []
# for item in items:
#     print(1)
#     title = item.find('a').text.strip()
#     link = item.find('a')['href']
#     foods.append([title,link])
#     print(title,'  ',link)

##爬歌单   
# url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6'
# res = requests.get(url)
# bs_music = BeautifulSoup(res.text,'html.parser')  
# print(bs_music)
# # 查找class属性值为“js_song”的a标签，得到一个由标签组成的列表
# list_music = bs_music.find_all('a',class_='js_song')
# # 对查找的结果执行循环
# for music in list_music:
# # 打印出我们想要的音乐名
#     print(music['title'])

# res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# # 调用get方法，下载这个字典
# json_music = res_music.json()    
# # 使用json()方法，将response对象，转为列表/字典
# list_music = json_music['data']['song']['list']
# # 一层一层地取字典，获取歌单列表
# for music in list_music:
# # list_music是一个列表，music是它里面的元素
#     print(music['name'])
#     # 以name为键，查找歌曲名

# Network能够记录浏览器的所有请求。我们最常用的是：ALL（查看全部）/XHR（仅查看XHR）/Doc（Document，第0个请求一般在这里），有时候也会看看：Img（仅查看图片）/Media（仅查看媒体文件）/Other（其他）。最后，JS和CSS，则是前端代码，负责发起请求和页面实现；Font是文字的字体；而理解WS和Manifest，需要网络编程的知识    
# XHR（或Fetch），因为有它的存在，人们不必刷新/跳转网页，即可加载新的内容  https://docs.python.org/3/library/json.html

# 创建一个列表a。
a = [1,2,3,4]
# 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b。
b = json.dumps(a)
# 打印b。
print(b)
# 打印b的数据类型
print(type(b))
# 使用loads()函数，将json格式的字符串b转为列表，赋值给c。
c = json.loads(b)
# 打印c。
print(c)
# 打印c的数据类型。
print(type(c)) 


    
