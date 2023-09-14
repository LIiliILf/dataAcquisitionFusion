# 查找文档中所有超级链接地址
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
# 获取元素的属性值，使用tag[attrName]
soup = BeautifulSoup(doc, "lxml")
# 实例6 查找文档中的所有超链接地址
tags = soup.find_all("a")
print("实例6查找文档中的所有超链接地址")
for tag in tags:
    print(tag["href"])

# 获取元素包含的文本值，使用tag.text
# 实例7 查找所有<a>超链接包含的文本值
tags = soup.find_all("a")
print("实例7所有<a>超链接包含的文本值")
for tag in tags:
    print(tag.text)

# 实例8 查找文档中所有<p>超链接包含的文本值
# 元素a包含的是一个简单的文本字符串，元素p包含复杂的结构
# 那么此时tag.text得到的是tag节点这颗子树下面所有文本节点的联合的字符串值。
tags = soup.find_all("p")
print("实例8<p>复杂结构包含的文本值")
for tag in tags:
    print(tag.text)
