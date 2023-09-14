import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

print("soup.a.next_sibling:\n",soup.a.next_sibling)
print("soup.a.next_sibling.next_sibling:\n",soup.a.next_sibling.next_sibling)
print("soup.a.previous_sibling:\n",soup.a.previous_sibling)
print("soup.a.previous_sibling.previous_sibling:\n",soup.a.previous_sibling.previous_sibling)
print("soup.a.parent:\n",soup.a.parent)

print("遍历后续节点:")
for sibling in soup.a.next_siblings: print(sibling)

print("遍历前续节点:")
for sibling in soup.a.previous_siblings: print(sibling)
