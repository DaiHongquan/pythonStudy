import requests,json

#创建会话。
session = requests.session()
#添加请求头，避免被反爬虫。
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
try:
    #以reader读取模式，打开名为cookies.txt的文件。
    cookies_txt = open('cookies.txt', 'r')
    #调用json模块的loads函数，把字符串转成字典。    
    cookies_dict = json.loads(cookies_txt.read())
    #把转成字典的cookies再转成cookies本来的格式。    
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    #获取会话下的cookies    
    session.cookies = cookies
    
#如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论。
except FileNotFoundError:

    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    #登录的参数。   
    data = {'log': input('请输入你的账号:'),
            'pwd': input('请输入你的密码:'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}
    #在会话下，用post发起登录请求。    
    session.post(url, headers=headers, data=data)
    #把cookies转化成字典。
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #调用json模块的dump函数，把cookies从字典再转成字符串。
    cookies_str = json.dumps(cookies_dict)
    #创建名为cookies.txt的文件，以写入模式写入内容
    f = open('cookies.txt', 'w')
    #把已经转成字符串的cookies写入文件
    f.write(cookies_str)
    #关闭文件
    f.close()
    
#文章的网址。
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
#评论的参数。
data_1 = {
'comment': input('请输入你想评论的内容：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'
}
#在会话下，用post发起评论请求
session.post(url_1, headers=headers, data=data_1)
