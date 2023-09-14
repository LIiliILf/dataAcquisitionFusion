from bs4 import BeautifulSoup

doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<a href="http://example.com/elsie" >Elsie</a>
<a href="http://example.com/lacie" >Lacie</a>
<a href="http://example.com/tillie" >Tillie</a>
</body>
</html>
'''

# 高级查找
# 查找文档中的href="http://example.com/lacie"的节点元素<a>
def myFilter(tag):
    print(tag.name)
    return (tag.name == "a" and tag.has_attr("href") and tag["href"] == "http://example.com/lacie")


soup = BeautifulSoup(doc, "lxml")
# 将myFilter函数的地址给find_all()函数。每个tag传入myFilter参数，判定是否符合过滤器，符合就被保留。
tags = soup.find_all(myFilter)
for tag in tags:
    print(tag)




