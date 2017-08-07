# coding=utf-8
import requests
from bs4 import BeautifulSoup

url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'

demo = requests.get(url)
demo.encoding = demo.apparent_encoding

soup = BeautifulSoup(demo, "html.parser")

print(soup[:500])