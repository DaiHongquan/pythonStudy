import scrapy
import bs4
from ..items import DoubanItem

#Scrapy中，每个爬虫的代码结构基本都如下所示
#继承自scrapy.Spider类
class DoubanSpider(scrapy.Spider):
    #爬虫的唯一标识
    name = 'douban'
    #定义允许爬虫爬取的网址域名（不需要加https://）。如果网址的域名不在这个列表里，就会被过滤掉
    allowed_domains = ['book.douban.com']
    #定义起始网址,allowed_domains的设定对start_urls里的网址不会有影响
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)   
    #parse是Scrapy里默认处理response的一个方法，中文是解析
    def parse(self, response):
        #用BeautifulSoup解析response
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        #用find_all提取<tr class="item">元素，这个元素里含有书籍信息
        datas = bs.find_all('tr',class_="item")
        #遍历data。
        for data in  datas:
            #实例化DoubanItem这个类。
            item = DoubanItem()
            #提取出书名，并把这个数据放回DoubanItem类的title属性里。
            item['title'] = data.find_all('a')[1]['title']
            #提取出出版信息，并把这个数据放回DoubanItem类的publish里。
            item['publish'] = data.find('p',class_='pl').text
            #提取出评分，并把这个数据放回DoubanItem类的score属性里。
            item['score'] = data.find('span',class_='rating_nums').text
            #打印书名。
            print(item['title'])
            #yield item是把获得的item传递给引擎。
            yield item
    
     