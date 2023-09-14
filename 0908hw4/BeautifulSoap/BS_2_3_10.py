# 通过函数查找可以查找到一些复杂的节点元素，查找文本值以"cie"结尾所有<a>节点
from bs4 import BeautifulSoup

doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<a href="http://example.com/elsie" >Elsie</a>
<a href="http://example.com/lacie" >Lacie</a>
<a href="http://example.com/tillie" >Tillie</a>
<a href="http://example.com/tilcie" >Tilcie</a>
</body>
</html>
'''

# 实例10 通过函数查找可以查找到一些复杂的节点元素，查找文本值以"cie"结尾所有<a>节点
# endsWith(s,t)函数判断s字符串是否以字符串t结尾，是就返回True，不然返回False，在myFilter中调用这个函数判断tag.text是否以"cie"结尾，最后找出所有文本值以"cie"结尾的<a>节点。
def endsWith(s, t):
    if len(s) >= len(t):
        return s[len(s) - len(t):] == t
    return False


def myFilter(tag):
    return (tag.name == "a" and endsWith(tag.text, "cie"))


soup = BeautifulSoup(doc, "lxml")
tags = soup.find_all(myFilter)
for tag in tags:
    print(tag)
