# import urllib.request
# from bs4 import BeautifulSoup
#
# # 定义目标URL
# url = "http://www.shanghairanking.cn/rankings/bcur/2020"
#
# # 发起HTTP请求并获取页面内容
# response = urllib.request.urlopen(url)
# html = response.read()
#
# # 使用BeautifulSoup解析页面
# soup = BeautifulSoup(html, "html.parser")
#
# # 查找包含大学排名信息的表格
# table = soup.find("table", class_="rk-table")
#
# # 打印表头
# print("排名\t学校名称\t省市\t学校类型\t总分")
#
# # 获取自己学号尾数的最后两位
# N = 10  # N为学号的最后两位
#
# # 遍历表格行数据
# for row in table.find_all("tr")[1:]:
#     cols = row.find_all("td")
#     if len(cols) == 0:
#         continue
#
#     # 解析每一列数据
#     rank = cols[0].text.strip()
#     university_name = cols[1].text.strip()
#     province = cols[2].text.strip()
#     university_type = cols[3].text.strip()
#     total_score = cols[4].text.strip()
#
#     # 将排名信息打印出来
#     print(f"{rank}\t{university_name}\t{province}\t{university_type}\t{total_score}")
#
#     # 判断是否达到了自己学号尾数的最后两位
#     if int(rank) >= N:
#         break

# 只打印学校中文名称，在解析HTML时只获取中文名字对应的元素，并在打印时输出这些元素的文本。


# import urllib.request
# from bs4 import BeautifulSoup
#
# url = "http://www.shanghairanking.cn/rankings/bcur/2020"
#
# # 发起HTTP请求并获取页面内容
# response = urllib.request.urlopen(url)
# html = response.read()
#
# # 使用BeautifulSoup解析页面
# soup = BeautifulSoup(html, "html.parser")
#
# # 查找包含大学排名信息的表格
# table = soup.find("table", class_="rk-table")
#
# # 打印表头
# print("排名\t学校名称\t省市\t学校类型\t总分")
#
# # 获取自己学号尾数的最后两位
# student_id = 10  # 请将这里的值更改为自己学号的最后两位
#
# # 遍历表格行数据
# for row in table.find_all("tr")[1:]:
#     cols = row.find_all("td")
#     if len(cols) == 0:
#         continue
#
#     # 解析每一列数据
#     rank = cols[0].text.strip()
#     university_name = cols[1].find("a").text.strip()  # 获取中文名字
#     province = cols[2].text.strip()
#     university_type = cols[3].text.strip()
#     total_score = cols[4].text.strip()
#
#     # 将排名信息打印出来
#     print(f"{rank}\t{university_name}\t{province}\t{university_type}\t{total_score}")
#
#     # 判断是否达到了自己学号尾数的最后两位
#     if int(rank) >= student_id:
#         break


# #导入urllib和BeautifulSoup库
# import urllib.request
# from bs4 import BeautifulSoup
#
# #获取指定网址页面数据
# url = "http://www.shanghairanking.cn/rankings/bcur/2020"
# response = urllib.request.urlopen(url)
# html = response.read().decode()
#
# #使用BeautifulSoup解析页面数据
# soup = BeautifulSoup(html, 'html.parser')
#
# #找到想要的表格
# table = soup.find('table', class_='_ranking-table _ranking-table-hover')
#
# #遍历表格前10行,提取对应的标题和内容
#     for tr in table.find_all('tr')[0:10]:
#
#     #找到每行的各个td
#         tds = tr.find_all('td')
#
#     #打印排名、学校名称、省市、学校类型、总分
#         print(tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text)

#
# import urllib.request
# from bs4 import BeautifulSoup
#
# # 定义要爬取的网址
# url = "http://www.shanghairanking.cn/rankings/bcur/2020"
#
# # 发起HTTP请求并获取页面内容
# response = urllib.request.urlopen(url)
# html = response.read()
#
# # 使用BeautifulSoup解析页面内容
# soup = BeautifulSoup(html, 'html.parser')
#
# # 找到包含大学排名信息的表格
# table = soup.find('table', {'id': 'worldUniversityRanking'})
#
# # 打印表头
# print("排名 学校名称 省市 学校类型 总分")
#
# # 找到表格中的所有行
# rows = table.find_all('tr')
#
# # 遍历每一行并打印排名信息，从第二行开始（第一行是表头）
# for row in rows[1:11]:  # 只打印前10名
#     # 找到每一行的所有列
#     columns = row.find_all('td')
#
#     # 提取排名、学校名称、省市、学校类型和总分信息
#     rank = columns[0].text.strip()
#     school_name = columns[1].text.strip()
#     location = columns[2].text.strip()
#     school_type = columns[3].text.strip()
#     total_score = columns[4].text.strip()
#
#     # 打印排名信息
#     print(f"{rank} {school_name} {location} {school_type} {total_score}")


# import urllib.request
# from bs4 import BeautifulSoup
#
# url = "http://www.shanghairanking.cn/rankings/bcur/2020"
#
# # 发起HTTP请求并获取页面内容
# response = urllib.request.urlopen(url)
# html = response.read()
#
# # 使用BeautifulSoup解析页面
# soup = BeautifulSoup(html, "html.parser")
#
# # 查找包含大学排名信息的表格
# table = soup.find("table", class_="rk-table")
#
# # 打印表头
# print("排名\t学校名称\t省市\t学校类型\t总分")
#
# # 设置一个计数器，用于控制打印前10名的信息
# count = 0
#
# # 遍历表格行数据
# for row in table.find_all("tr")[1:]:
#     cols = row.find_all("td")
#     if len(cols) == 0:
#         continue
#
#     # 解析每一列数据
#     rank = cols[0].text.strip()
#     university_name = cols[1].find("a").text.strip()  # 获取中文名字
#     province = cols[2].text.strip()
#     university_type = cols[3].text.strip()
#     total_score = cols[4].text.strip()
#
#     # 将排名信息打印出来
#     print(f"{rank}\t{university_name}\t{province}\t{university_type}\t{total_score}")
#
#     # 增加计数器
#     count += 1
#
#     # 判断是否已经打印了前10名的信息，如果是则退出循环
#     if count >= 10:
#         break


import urllib.request
from bs4 import BeautifulSoup

url = "http://www.shanghairanking.cn/rankings/bcur/2020"

# 发起HTTP请求并获取页面内容
response = urllib.request.urlopen(url)
html = response.read()

# 使用BeautifulSoup解析页面
soup = BeautifulSoup(html, "html.parser")

# 查找包含大学排名信息的表格
table = soup.find("table", class_="rk-table")

# 打印表头
print("排名\t学校名称\t省市\t学校类型\t总分")

# 遍历表格前十次
for row in table.find_all("tr")[1:11]:
    cols = row.find_all("td")
    if len(cols) == 0:
        continue

    # 解析每一列数据
    rank = cols[0].text.strip()
    university_name = cols[1].find("a").text.strip()  # 获取中文名字
    province = cols[2].text.strip()
    university_type = cols[3].text.strip()
    total_score = cols[4].text.strip()

    # 将排名信息打印出来
    print(f"{rank}\t{university_name}\t{province}\t{university_type}\t{total_score}")
