from bs4 import BeautifulSoup

# HTML文档
html = """
<html>
<head>
    <title>This is a python demo page</title>
</head>
<body>
    <p class="title">
        <b>The demo python introduces several python courses.</b>
    </p>
    <p class="course">Python is a wonderful general‐purpose programming language.
        You can learn Python from novice to professional by tracking the following courses:
        <a href="http://www.icourse163.org/course/BIT‐268001" class="py1" id="link1">Basic Python</a> and
        <a href="http://www.icourse163.org/course/BIT‐1001870001" class="py2" id="link2">Advanced Python</a>.
    </p>
</body>
</html>
"""

# 使用Beautiful Soup解析HTML文档


# # 上行遍历示例：从<b>标签到<p>标签
# b_tag = soup.find('b')
# p_tag = b_tag.find_parent('p')
# print(f'上行遍历：{b_tag} -> {p_tag}')
#
# # 下行遍历示例：从<p>标签到<a>标签
# p_tag = soup.find('p', class_='course')
# a_tags = p_tag.find_all('a')
# for a_tag in a_tags:
#     print(f'下行遍历：{p_tag} -> {a_tag}')
#
# # 平行遍历示例：从第一个<a>标签到第二个<a>标签
# first_a_tag = soup.find('a', class_='py1')
# second_a_tag = first_a_tag.find_next_sibling('a', class_='py2')
# print(f'平行遍历：{first_a_tag} -> {second_a_tag}')
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.head)
#
# soup.head.contents
# soup.body.contents
# len(soup.body.contents)
# soup.body.contents[1]

import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

print("soup.head:",soup.head)
print("soup.head.contents:",soup.head.contents)
print("soup.body.contents:\n",soup.body.contents)
print("soup.body.contents个数:",len(soup.body.contents))
print("soup.body.contents[1]:",soup.body.contents[1])

#遍历儿子节点
for child in soup.body.children:
    print(child)

#遍历子孙节点
for child in soup.body.descendants:
    print(child)
