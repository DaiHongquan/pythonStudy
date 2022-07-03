# pip3 install selenium # 电脑安装selenium  不要命名为selenium.py
# https://registry.npmmirror.com/binary.html?path=chromedriver/浏览器版本/ 浏览器驱动版本地址  版本不一致解决办法https://www.likecs.com/show-141662.html
# driver.close()是关闭浏览器驱动，每次调用了webdriver之后，都要在用完它之后加上一行driver.close()用来关闭它
# selenium所解析提取的，是Elements中的所有数据，而BeautifulSoup所解析的则只是Network中第0个请求的响应


# 本地Chrome浏览器设置方法
from selenium import webdriver # 从selenium库中调用webdriver模块
import time # 调用time模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
print(dir(driver))
driver.
# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
# time.sleep(2) # 暂停两秒，等待浏览器缓冲

# teacher = driver.find_element_by_id('teacher') # 找到【请输入你喜欢的老师】下面的输入框位置
# teacher.send_keys('必须是吴枫呀') # 输入文字
# assistant = driver.find_element_by_name('assistant') # 找到【请输入你喜欢的助教】下面的输入框位置
# assistant.send_keys('都喜欢') # 输入文字
# button = driver.find_element_by_class_name('sub') # 找到【提交】按钮
# button.click() # 点击【提交】按钮
# time.sleep(1)
# driver.close() # 关闭浏览器


# 以下方法都可以从网页中提取出'你好，蜘蛛侠！'这段文字  换成s就是复数提取  HTML源代码字符串 = driver.page_source  就可以用BeautifulSoup
#.send_keys() # 模拟按键输入，自动填写表单
#.click() # 点击元素  .clear()，用于清除元素的内容

# find_element_by_tag_name：通过元素的名称选择
# 如<h1>你好，蜘蛛侠！</h1> 
# 可以使用find_element_by_tag_name('h1')

#find_element_by_class_name：通过元素的class属性选择
# 如<h1 class="title">你好，蜘蛛侠！</h1>
# 可以使用find_element_by_class_name('title')

#find_element_by_id：通过元素的id选择
# 如<h1 id="title">你好，蜘蛛侠！</h1> 
# 可以使用find_element_by_id('title')

#find_element_by_name：通过元素的name属性选择
# 如<h1 name="hello">你好，蜘蛛侠！</h1> 
# 可以使用find_element_by_name('hello')

#以下两个方法可以提取出超链接

#find_element_by_link_text：通过链接文本获取超链接
# 如<a href="spidermen.html">你好，蜘蛛侠！</a>
# 可以使用find_element_by_link_text('你好，蜘蛛侠！')

#find_element_by_partial_link_text：通过链接的部分文本获取超链接
# 如<a href="https://localprod.pandateacher.com/python-manuscript/hello-spiderman/">你好，蜘蛛侠！</a>
# 可以使用find_element_by_partial_link_text('你好')