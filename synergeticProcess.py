## 多协程 
#http://www.boohee.com/food/

#从gevent库里导入monkey模块
from gevent import monkey
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。必须在导入ssl库之前打猴子补丁，否则可能报错
monkey.patch_all() 
import gevent,time,requests
from gevent.queue import Queue


start = time.time()

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

#创建队列对象，并赋值给work
work = Queue()
#遍历url_list
for url in url_list:
    #用put_nowait()函数可以把网址都放进队列里
    work.put_nowait(url)
    

def crawler():
    #当队列不是空的时候，就执行下面的程序
    while not work.empty():
        #用get_nowait()函数可以把队列里的网址都取出
        url = work.get_nowait()
        #用requests.get()函数抓取网址
        r = requests.get(url)
        #打印网址、队列长度、抓取请求的状态码。
        print(url,work.qsize(),r.status_code)
        
#创建空的任务列表
tasks_list  = [ ]
#相当于创建了2个爬虫
for x in range(2):
    #用gevent.spawn()函数创建执行crawler()函数的任务
    task = gevent.spawn(crawler)
    #往任务列表添加任务
    tasks_list.append(task)
#用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站 
gevent.joinall(tasks_list)

end = time.time()
print(end-start)

