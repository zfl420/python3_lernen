import requests
from bs4 import BeautifulSoup
# 引入库
base_url = 'http://www.jianshu.com/p/f001e63fed4e' # page=0 和 page=1的效果相同
add_url = 1 # page数
num = 0 # 文章标题计数

while(True):
    try:
        page = requests.request('get', base_url% add_url).content
        # 将基础网址和页数拼接得到实际网址，使用request的get方法获取响应，再用content方法得到内容
        soup = BeautifulSoup(page) 
        # 使用BeautifulSoup分析页面，这里并没有指定解析器，会自动选取可获得的最优解析器
        # BeautifulSoup会报一个warning要你选择解析器，可以忽略

        article_list = [i.get_text() for i in soup.select(".title a")]
        # 这里使用了BeautifulSoup的选择器soup.select，它会返回一个被选取的对象列表，我们使用列表推导，对每个对象获取其中的文字再组成列表。
        # 选择器使用见下文
        for i in article_list:
        # 将文章列表打印出来
            num+=1
            print(num, '  ', i)
        add_url += 1
    except Exception as e:
    # 异常分析，打印出异常信息
        print(e)
        break # 这里使用break退出循环，也可注释掉该句，不断循环

作者：treelake
链接：http://www.jianshu.com/p/be891e7e96e2
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。