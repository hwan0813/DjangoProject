import requests
from bs4 import BeautifulSoup

url = "http://www.hanyang.ac.kr/web/www/main-notices"
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

notice = []
date =[]
for a_tag in soup.select('.title a'):
    notice.append(a_tag.text)
for a_tag in soup.select('.date'):
    date.append(a_tag.text)

dict ={}
for i in range(len(notice)):
    dict[notice[i]] = date[i]

print("                    << 현재 한양대 최신 공지사항 긁어오기 >>")
for i in dict.items():
    print(i)

