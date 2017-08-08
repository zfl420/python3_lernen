import requests
url = "https://www.amazon.cn/gp/product/B01E8BTCK0/"

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers= kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
