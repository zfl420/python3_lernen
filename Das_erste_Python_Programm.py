import requests
from bs4 import BeautifulSoup
import urllib.request          # 获取网页内容
import re                      # 正则式模块.
import os                      # 系统路径模块: 创建文件夹用
import socket                  # 下载用到?
import time                    # 下载用到?


#结构化网页数据前提，必须先写这个才能开始输出结构化数据 ！！！非常重要！！！ —— 后面的 'lxml' 一定要写，这是定义解析器。

# print(soup.prettify())
#  结构化网页数据2

#print(soup.title.string)
#  打印title标签以及里面的内容, 如果后面不加 .string 就会把<title></title>一起打印出来。

# print(soup.title.name)
#  打印title 标签的名字

# print(soup.title.string)
#  打印 title 标签里面的内容

#print(soup.title.parent.name)
# 打印title父标签的名字,名字是 head

# print(soup.p)
# print(soup.a)
#  打印soup里面第一个p标签， 如果是soup.a 就是打印soup内的第一个a 标签

#print(soup.find_all('a')) # 找到soup 里面所有的a标签
# find_all() 搜索元素,
# find_all('a')  → 搜索所有的a  链接
# find_all('p')  → 搜索所有的p  段落
# find_all('li') → 搜索所有的li 列表项目
# find_all() 也能用正则式来匹配搜索

# print(soup.find(id="sidebar"))
# 找到id 为 sidebar 的 id

#for link in soup.find_all('a'):
#    print(link.get('href'))
# 从文档中找到所有<a>标签的链接
# 这是找出网页内所有的链接.
# link是个变量. 名字任取. 只要上下两行对应就可.
# for xxx in soup.find_all('a'):
#     print(xxx.get('href'))
# for link in soup.find_all('ul', id="pins"):
#     print(link)
# 搜索网页中所有的 id 是pins 的ul元素
# 搜索网页中所有的 class 是 的img元素
# for link2 in soup.find_all('img', "lazy"):
#     print(link2)
# ID 和 Class 稍微有点区别. 多参数情况下默认是搜索class的

#print(soup.get_text())
#从文档中找到所有<a>标签的链接

'''
page1_urls = []
lis = soup.find('ul', {'id': 'pins'}).find_all('li')
print(lis)
for li in lis:
    page1_urls.append(li.find('a')['href'])
print(page1_urls)
# 功能: 把 id 是 pins 的ul元素 下面的所有li里的链接 加到一个数组里面
# 每页的24个妹子主题. 都是在 <ul id="pins"> 下面的24个li中.
# li里包含很多无用的信息:比如标题,时间. 我们只要里面的网址.
# 用循环把每个主题的地址. 添加到page1_urls 这个数组里面.
'''
# ❤️❤️一、 ↓↓↓ 获取所有主题的链接地址 ↓↓↓ ❤️❤️

def get_page1_urls():          # 定义一个函数
    page1_urls = []            # 定义一个数组,来储存所有主题的URL
    for page in range(1, 73):
        url = 'http://www.mmjpg.com/home/' + str(page)
        request = requests.get(url)
        request.encoding = request.apparent_encoding
        html = request.text
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.find('div', {'class': 'pic'}).find('ul').find_all('li')
        #找到 class=pic的DIV里面的UL标签里面的LI，注意，这里的.find('ul')是可以省略的。<li>里面有很多内容 <li><a href="http://www.mmjpg.com/mm/980" target="_blank"><img src="http://img.mmjpg.com/small/2017/980.jpg" width="220" height="330" alt="漂亮嫩妹夏笑笑美腿丰臀诱惑尽显眼前"></a><span class="title"><a href="http://www.mmjpg.com/mm/980" target="_blank">漂亮嫩妹夏笑笑美腿丰臀诱惑尽显眼前</a></span><span>05-10 发布</span><span class="view">浏览(2100271)</span></li>
        for li in lis: #循环，也就是列出lis里面的所有<li>
            page1_urls.append(li.find('a')['href'])
            # 然后再从li面找到 找到<a>标签里面的href。
        #print(page1_urls)
    return page1_urls
# get_page1_urls() 这个函数可以返回所有的链接地址




# ❤️❤️二、 ↓↓↓ 自动获取某主题的照片数量 ↓↓↓ ❤️❤️

# 进入某个主题, 然后分析底部的 导航条.
# 导航条格式: 上一组 1 2 3 4 ... 64 下一组
# 很多按钮.每个按钮都是一个<a>元素.
# 倒数第二个<a>元素 这里也就是64 就是照片数量!


def get_page_num(page1_url):        # 参数 page1_url 不一定要外界传入的. 可以给函数里面用的.
    request = requests.get(page1_url)
    try:
        html = request.text
    except:
        try:
            html = requests.text
        except:
            return None
            # 这个函数会重复请求两次. 如果两次都超时就放弃.
    soup = BeautifulSoup(html, 'lxml')  # html是上
    try:
        page_num = soup.find('div', {'id': 'page'}).find_all('a')[-2].get_text()
        # 这里找到ID为PAGE的DIV里面的A标签的文字。[-2]表示倒数第二个A标签。
    except:
        return None
    return int(page_num) #这里要注意INT，是把返回的页码数字以整数的形式打印出来。
# print(get_page_num('http://www.mmjpg.com/mm/970'))  # 测试 get_page_num(page1_url) 的语句，这里面传入了一个上面一个函数获得的网页地址。








# ❤️❤️ 三: 获取某主题下第一张照片的URL. ❤️❤️

# 结合上面的照片数量. 就能获取到某主题下的所有照片链接了.


def get_img_url(url):
    request = requests.get(url)
    try:
        html = request.text
    except:
        try:
            html = request.text
        except:
            return None
    soup = BeautifulSoup(html, 'lxml')
    try:
        img_url = soup.find('div', {'id':'content'}).find('a').find('img')['src']
        # 找到 单个主题里面的 id 是content 的DIV 里面的<a> 里面的 <img>的SRC，也就是照片链接。
    except:
        return None
    return img_url

# print(get_img_url('http://www.mmjpg.com/mm/970'))  测试 def get_img_url(url)







# ❤️❤️ 四: 获取某主题下所有照片的URL. ❤️❤️

# 然后就要获取某主题下所有照片的URL的函数
# 这时候就用到了 上面两个函数了.
# 这个函数 要传入一个参数.也就是主题的URL地址.
# 每个主题都循环一遍 就能获取所有主题的所有照片了.
# 任务也就只差下载了.


def get_img_urls(page1_url):
    page_num = get_page_num(page1_url)
    # 这里就用到了 上面的 get_page_num 这个函数了.
    if page_num is None:
        return None
    img_urls = []
    # 定义一个数组 来储存该主题下的 所有照片的 URL
    for page in range(1, page_num + 1):
        url = page1_url + '/' + str(page)
        # 实际照片的链接地址 就是主题的链接 + / + 数量
        img_url = get_img_url(url)
        # 这里用到了 get_img_url 这个函数. 可以获取该主题下的第一张照片.
        # 现在是在循环里面. 循环次数就是 该主题的照片数量+1
        if img_url is None:
            return None
        else:
            img_urls.append(img_url)
        # 把获取到的 url 添加到 img_urls 这个数组里.
        # 这样循环下来 img_urls 数组里面就有该主题下的所有照片地址了
    return img_urls

# print(get_img_urls('http://www.mmjpg.com/mm/1069'))  测试四











# ❤️❤️ 五: 获取某主题名称,创建本地文件夹用 ❤️❤️


def get_img_title(page1_url):
    request = requests.get(page1_url)
    request.encoding = request.apparent_encoding  #转换一下字符编码。要不然乱码
    try:
        html = request.text
    except:
        try:
            html = request.text
        except:
            return None
    soup = BeautifulSoup(html, 'lxml')
    # <h2 class="main-title">古典气质型美女施诗 顶级美腿加酥胸圆臀火辣身材性感十足</h2>
    title = soup.find('div', {'class': 'article'}).find('h2').get_text()
    # 下面两行是异常分析..
    removeSign = re.compile(r'[\/:*?"<>|]')
    # re 就是正则表达式模块
    # re.compile 把正则表达式封装起来. 可以给别的函数用. ()里面的才是真的 表达式.
    # r'[\/:*?"<>|]'
    # [] 表示一个字符集;  \对后面的进行转义 英文/是特殊符号; 其他的是正常符号.
    title = re.sub(removeSign, '', title)
    # re.sub 在字符串中 找到匹配表达式的所有子串. 用另一个进行替换.这里用'' 就是删除的意思.
    # 就是说 删除标题里面的 /:*?"<>| 这些符号.
    # 英文创建文件夹时候 不能有特殊符号的!!!
    return title

# print(get_img_title('http://www.mmjpg.com/mm/979'))  测试











# ❤️❤️ 六: 定义下载某主题所有图片的函数 ❤️❤️
# 下载肯定要创建文件夹.要用到路径.这就需要 os 模块了.
# 我们把照片 建立个文件夹 下载到 脚本运行的目录下
# os.path模块主要用于文件的属性获取，经常用到，以下是该模块的几种常用方法
# print(os.getcwd())                 # 获取并输出当前脚本所在的目录.
# os.mkdir('./妹子图')               # 在当前文件夹下 建立 妹子图 文件夹.
# os.rmdir('./妹子图')               # 在当前文件夹下 删除 妹子图 文件夹.
# if os.path.exists('./妹子图'):     # 判断当前文件夹 是否存在   妹子图这个文件夹
# if not os.path.exists('./妹子图'): # 判断当前文件夹 是否不存在 妹子图这个文件夹
# 本项目我们先判断当前脚本文件夹 是否已经有妹子图这个文件夹存在.
# 如果不存在那就新建一个妹子图文件夹.
# 再判断妹子图文件夹下 有没有对应的子文件夹存在.


def download_imgs(page1_url):
    img_urls = get_img_urls(page1_url)
    if img_urls is None:
        return None
    if not os.path.exists('./mmjpg'):
        os.mkdir('./mmjpg')
    title = get_img_title(page1_url)
    if title is None:
        return None
    local_path = './mmjpg/' + title    #一会确认下
    if not os.path.exists(local_path):
        try:
            os.mkdir(local_path)
        except:
            pass
    if img_urls is None or len(img_urls) == 0:
        return None
    else:
        print('--开始下载' + title + '--')
        for img_url in img_urls:
            img_name = os.path.basename(img_url)
            print('正在下载 ' + img_name)
            print('来自这个链接 ' + img_url)
            socket.setdefaulttimeout(10)
            try:
                urllib.request.urlretrieve(img_url, local_path + '/' + img_name)
            except:
                print('下载' + img_name + '失败')
        print('--' + title + '下载完成--')


#print(download_imgs('http://www.mmjpg.com/mm/979'))   测试


# ee = download_imgs("http://www.mzitu.com/858")
# print(ee)
# 成功下载一套主题!!!!

def craw_mmjpg():
    page1_urls = get_page1_urls()
    # 这里用到了 第一个函数. 也就是获取所有主题的 URL.
    if page1_urls is None or len(page1_urls) == 0:
        return
    else:
        for page1_url in page1_urls:
            # 循环第六步 来下载所有主题的URL
            download_imgs(page1_url)


def main():
    craw_mmjpg()
if __name__ == '__main__':
    main()



