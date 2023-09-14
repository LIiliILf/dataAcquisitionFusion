import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

print("soup.title.parent:\n",soup.title.parent)
print("soup.html.parent:\n",soup.html.parent)
print("soup.parent:\n",soup.parent)

# 上行遍历，遍历所有先辈结点，包括suop本身
soup = BeautifulSoup(demo, "html.parser")
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)