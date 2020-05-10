#爬取数据集对象对新浪收藏-艺术品数据库http://data.collection.sina.com.cn/index.php?p=data&s=default&a=view
#瓷器 http://data.collection.sina.com.cn/default/items/?category=6.1&page=1
#玉石 http://data.collection.sina.com.cn/default/items/?org_id=0&category=6.2&keyword=&search_in=&priceIndex=0&order_by=sale_date+DESC&layout=0&cpp=0&page=%s
#诸如此类，仅需改变指定URL和最后的PAGE数字即可爬取

import bs4
import requests
import os
for i in range(1,40):
    url = ("http://data.collection.sina.com.cn/default/items/?category=6.1&page=%s" % i) #正则表达式
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    #加入headers,模拟访问，否则会被反爬措施强制停止连接、拒绝访问
    req = requests.get(url,headers=headers)
    req.encoding="utf-8"

    bs = bs4.BeautifulSoup(req.text)
    obj = bs.find_all("div",{"class":{"pro_pic"}})
    objHtml=[]
    objImg=[]
    for s in obj:
        objHtml.append(s.find("img"))
    for o in objHtml:
        objImg.append(o.get("src"))
    for img in objImg:
        with open("D:\\BSdata\\Picture\\1\\"+os.path.basename(img),'wb') as f:
            f.write(requests.get(img).content)
        print(os.path.basename(img)+"保存成功");