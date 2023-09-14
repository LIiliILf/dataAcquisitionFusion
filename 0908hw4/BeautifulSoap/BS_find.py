from bs4 import BeautifulSoup

doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
</body>
</html>
'''
# 实例1查找文档中的<title>元素,元素类型是一个bs4.element.Tag对象。
soup = BeautifulSoup(doc, "lxml")
tag = soup.find("title")
print("实例1用find()查找title元素结果：", end="")
print(type(tag), tag)
#实例1查找元素find()结果：<class 'bs4.element.Tag'> <title>The Dormouse's story</title>

# 实例2查找文档中的所有<a>元素,元素类型是一个bs4.element.ResultSet对象。
tags = soup.find_all("a")
# tags = soup.find_all("a",attrs = {"class":"sister"})
print("实例2用find_all()查找所有a元素：\n", end="")
for tag in tags:
    print(tag)
#实例2查找元素find_all()结果：<class 'bs4.element.ResultSet'> <title>The Dormouse's story</title>


# 实例3查找文档中的第一个<a>元素,元素类型是一个bs4.element.Tag对象。
tag = soup.find("a")
print("实例3find()查找a元素，只会找到第一个：",tag)

# 实例4查找class = "title"的<p>元素,元素类型是一个bs4.element.Tag对象。
tag = soup.find("p", attrs={"class": "title"})
print("实例4查找class = title的<p>元素",tag)

# 实例5 查找class = "sister"的元素
tags = soup.find_all(name=None, attrs={"class": "sister"})
print("实例5查找class为sister的元素//带特定属性及属性值元素")
for tag in tags:
    print(tag)


