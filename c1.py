import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.qiushibaike.com/article/123370822')
content =url.content
soup = BeautifulSoup(content, 'html.parser')
for div in soup.find_all('div', {'class': 'content'}):
     print (div.text.strip())

# comments = soup.find(attrs={'class': 'comments'})
comments = soup.find(class_= 'comments')
print(comments.text)

""""
    class是python的保留关键字，若要匹配标签内class的属性，需要特殊的方法，有以下两种：
    在attrs属性用字典的方式进行参数传递
    BeautifulSoup自带的特别关键字class_
"""


