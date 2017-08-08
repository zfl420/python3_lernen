#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request          # 获取网页内容
from bs4 import BeautifulSoup  # 解析网页内容
import re                      # 正则式模块.
import os                      # 系统路径模块: 创建文件夹用
import socket                  # 下载用到?
import time                    # 下载用到?
import requests



# 浏览器输入网址就下载网页并显示给你.
# 终端怎么下载网页呢.  用 urllib2 / urllib.request 是最方便的.
# 首先python3 的话:  import urllib.request 导入这个下载网页的库.
# 然后上面第一行只要改掉urlopen 双引号里面的网址就可以爬你想要的网址了.
# 就可以在终端显示出 某个网站的源代码了, 这样一个网页就算被你爬下来了!! 很简单吧.
# response = urllib2.urlopen("https://www.0214.live")
# 调用 urllib库 里面的 urlopen 这个方法,这个方法需要传入一个数据.一般都是网址.
# 把 整个网页数据保存到 response 这个变量中.
# 这行其实可以分成两行.
# request = urllib2.Request("https://www.0214.live")
# response = urllib2.urlopen(request)
# 推荐大家这么写. 最终会有很多代码. 这样写逻辑上更清晰.
# 先传入一个请求,  然后再打开网站
# print response.read()
# 读取变量的内容. 也就是整个网页的内容

# 上面三行是获取网页源代码的方法.
# 取消注释. 就能在终端显示妹子图第一页的源代码了.
# 接下来需要从源代码里面. 找出第一页的24个 主题地址网址!
# 这里就要用 beautifulsoup 4 模块来提取网页中指定内容了. 简称 bs4
# 下面是 bs4 的基本用法.


# 了解了bs4 的基本用法. 就可以 把网址中的特定的网址加到某个数组里了.

'''


# 下面是结果
# ✘✘∙𝒗 zz python3 mzitu00.py
# ['http://www.mzitu.com/88557', 'http://www.mzitu.com/88509', 'http://www.mzitu
# .com/88458', 'http://www.mzitu.com/88415', 'http://www.mzitu.com/88373', 'http
# ://www.mzitu.com/88317', 'http://www.mzitu.com/88250', 'http://www.mzitu.com/8
# 8209', 'http://www.mzitu.com/88162', 'http://www.mzitu.com/88116', 'http://www
# .mzitu.com/88065', 'http://www.mzitu.com/88014', 'http://www.mzitu.com/87933',
#  'http://www.mzitu.com/87973', 'http://www.mzitu.com/87825', 'http://www.mzitu
# .com/87813', 'http://www.mzitu.com/87762', 'http://www.mzitu.com/87693', 'http
# ://www.mzitu.com/87628', 'http://www.mzitu.com/87580', 'http://www.mzitu.com/8
# 7541', 'http://www.mzitu.com/87500', 'http://www.mzitu.com/87434', 'http://www
# .mzitu.com/87390']

# 看了上面的例子就会爬第一个页面上的24个主题的链接了,只要用循环就能爬所有页面了!!!
'''


# ❤️❤️ ↓↓↓ 获取整个妹子网所有的主题 ↓↓↓ ❤️❤️


def get_page1_urls():          # 定义一个函数
    page1_urls = []            # 定义一个数组,来储存所有主题的URL
    for page in range(1, 73):
        url = 'http://www.mzitu.com/page/' + str(page)
        request = requests.get(url)
        request.encoding = request.apparent_encoding
        html = request.text
        soup = BeautifulSoup(html, 'lxml')
        # 把下载的网页.结构化成DOM, 方便下面用 find 取出数据
        lis = soup.find('ul', {'id': 'pins'}).find_all('li')
        # 找到 id 为pins 这个列表下面的 每个列 就找到每个页面下的 24个主题了
        for li in lis:
            # 遍历每页下面的24个主题 (也就是24个li)
            page1_urls.append(li.find('a')['href'])
            # 把每个主题的地址. 添加到page1_urls 这个数组里面.
        # print(page1_urls)
        # # 显示网址. 测试用. 循环140次. 这样就获得了所有主题的网址了
    return page1_urls


# ❤️❤️ ↓↓↓ 自动获取某主题的照片数量 ↓↓↓ ❤️❤️
# 进入某个主题, 然后分析底部的 导航条.
# 导航条格式: 上一组 1 2 3 4 ... 64 下一组
# 很多按钮.每个按钮都是一个<a>元素.
# 倒数第二个<a>元素 这里也就是64 就是照片数量!


def get_page_num(page1_url):        # 参数 page1_url 不一定要外界传入的. 可以给函数里面用的.
    request = urllib.request.Request(page1_url)
    try:
        html = urllib.request.urlopen(request, timeout=20).read()
    except:
        try:
            html = urllib.request.urlopen(request, timeout=20).read()
        except:
            return None
            # 这个函数会重复请求两次. 如果两次都超时就放弃.
    soup = BeautifulSoup(html, 'lxml')
    try:
        page_num = soup.find('div', {'class': 'pagenavi'}).find_all('a')[-2].find('span').get_text()
    except:
        return None
    return int(page_num)
# aa = get_page_num("http://www.mzitu.com/858")
# print(aa)
# 这两行是测试 某主题下的图片数量的. 你随便填个妹子图的主题地址进去.看看对不对.


# ❤️❤️ 三: 获取某主题下第一张照片的URL. ❤️❤️
# 结合上面的照片数量. 就能获取到某主题下的所有照片链接了.


def get_img_url(url):
    request = urllib.request.Request(url)
    try:
        html = urllib.request.urlopen(request, timeout=20).read()
    except:
        try:
            html = urllib.request.urlopen(request, timeout=20).read()
        except:
            return None
    soup = BeautifulSoup(html, 'lxml')
    try:
        img_url = soup.find(
            'div', {'class':
                    'main-image'}).find('p').find('a').find('img')['src']
    except:
        return None
    return img_url
# bb = get_img_url("http://www.mzitu.com/858")
# print(bb)
# 这两行是测试 某主题下第一张图片的真实url的.  亲测通过.


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

# cc = get_img_urls("http://www.mzitu.com/858")
# print(cc)
# 这两行是测试 某主题下所有图片的真实url的.  亲测通过.


# ❤️❤️ 五: 获取某主题名称,创建本地文件夹用 ❤️❤️


def get_img_title(page1_url):
    request = urllib.request.Request(page1_url)
    try:
        html = urllib.request.urlopen(request, timeout=20).read()
    except:
        try:
            html = urllib.request.urlopen(request, timeout=20).read()
        except:
            return None
    soup = BeautifulSoup(html, 'lxml')
    # <h2 class="main-title">古典气质型美女施诗 顶级美腿加酥胸圆臀火辣身材性感十足</h2>
    title = soup.find('h2', {'class': 'main-title'}).get_text()
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
# dd = get_img_title("http://www.mzitu.com/858")
# print(dd)
# 这两行是测试 某主题的主题名.  亲测通过.


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
    if not os.path.exists('./妹子图'):
        os.mkdir('./妹子图')
    title = get_img_title(page1_url)
    if title is None:
        return
    local_path = './妹子图/' + title
    if not os.path.exists(local_path):
        try:
            os.mkdir(local_path)
        except:
            pass
    if img_urls is None or len(img_urls) == 0:
        return
    else:
        print('--开始下载' + title + '--')
        for img_url in img_urls:
            img_name = os.path.basename(img_url)
            print('正在下载 ' + img_name)
            print('from ' + img_url)
            socket.setdefaulttimeout(10)
            try:
                urllib.request.urlretrieve(img_url, local_path + '/' + img_name)
            except:
                print('下载' + img_name + '失败')
        print('--' + title + '下载完成--')


# ee = download_imgs("http://www.mzitu.com/858")
# print(ee)
# 成功下载一套主题!!!!
# ❤️❤️ 七: 下载所有主题的图片 ❤️❤️


def craw_meizitu():
    page1_urls = get_page1_urls()
    # 这里用到了 第一个函数. 也就是获取所有主题的 URL.
    if page1_urls is None or len(page1_urls) == 0:
        return
    else:
        for page1_url in page1_urls:
            # 循环第六步 来下载所有主题的URL
            download_imgs(page1_url)


def main():
    craw_meizitu()
if __name__ == '__main__':
    main()
