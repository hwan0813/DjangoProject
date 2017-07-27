import pymysql
import requests
from bs4 import BeautifulSoup
# 아래 4줄을 추가해 줍니다. 이 네줄을 추가하면 이 파일을 단독으로 실행해도 manage.py를 통해 django를 구동한 것과같이 사용할 수 있음. 
import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askdjango.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

# BlogData를 import해옵니다
from crawl.models import Lotte



def parse_lotte():
    req = requests.get('http://www.lottemart.com/category/categoryList.do?CategoryID=C00100140004')
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    
    # 상품명 리스트에 담기
    a = []
    for product in soup.select('#contents .prod-name a'):
        a.append(product.text.strip())
    
    # 가격 리스트에 담기
    b = []
    for price in soup.select('#contents .price-max em'):
        b.append(price.text)
    
    # 가격 긁어온것중에 쓸모없는 데이터 확인해서 제거
    for i in range(b.count('~')):
        b.remove('~')
    
    # 두개의 리스트를 dictionary 형으로 삽입. 
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = b[i]
    
    return dict


if __name__=='__main__':
    # 데이터베이스 연결
    conn = pymysql.connect(db='crawl', user='root', password='ghks5466', host='localhost', charset='utf8')
    # cursor 객체를 가져온다.
    curs = conn.cursor()
    
    data_dict = parse_lotte()
    
    sql = "INSERT into crawl_lotte (pro_name,price) values (%s,%s);"
    
    
    try:
        for t, l in data_dict.items():
            
            print(t,l)
            # t, l을 파라미터로 sql문 전달 
            curs.execute(sql, (t, l))
            
    finally:
        # 데이터베이스에 반영 commit
        conn.commit()
        # 데이터 베이스 연결 끊기 
        conn.close()
    





'''
# 데이터 베이스에 넣기 save를 통해서도 가능하다. 
if __name__=='__main__':
    blog_data_dict = parse_lotte()
    for t, l in blog_data_dict.items():
        Lotte(pro_name=t, price=l).save()
        #print(t,l)
'''