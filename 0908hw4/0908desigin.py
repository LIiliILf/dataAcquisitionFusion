import urllib.request
from bs4 import BeautifulSoup

url = "http://www.shanghairanking.cn/rankings/bcur/2020"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# 找到包含大学排名信息的表格
table = soup.find("table", class_="rk-table")

print("排名 学校名称 省市 学校类型 总分")

# 遍历表格前十次
for row in table.find_all("tr")[1:11]:
    cols = row.find_all("td")
    if len(cols) == 0:
        continue

    rank = cols[0].text.strip()
    university_name = cols[1].find("a").text.strip()  # 获取中文名字
    province = cols[2].text.strip()
    university_type = cols[3].text.strip()
    total_score = cols[4].text.strip()

    print(f"{rank}\t{university_name}\t{province}\t{university_type}\t{total_score}")
