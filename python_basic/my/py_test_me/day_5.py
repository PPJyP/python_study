#!/usr/bin/env python
# coding: utf-8

# In[3]:


#표준모듈
import math


# In[5]:


math.cos(10)
math.ceil(5.6) # 올림
math.floor(5.6) # 버림


# In[6]:


from math import ceil, cos, floor #모듈명이 길면 이처럼 일부만 가져와서 사용가능

print(cos(10))
print(ceil(5.6))
print(floor(5.6))


# In[7]:


# as를 사용하여 별명(alias)으로 사용

import math as m

m.cos(10)


# In[15]:



import random as r

print("random 모듈 :")
print("random() : ", r.random())

# float 리턴은 random.uniform(x,y)
# int 리턴은 random.randrange(x,y) or random.randrange(x)


# 1~10중 선택 // 아래와 같이 리스트를 작성할 수 있음
a_list=list(range(10))
print("random() : ", r.choice(a_list))

#셔플
b=r.shuffle(a_list)
print("random() : ", a_list)

#샘플
print("random() : ", r.sample(a_list,k=2))


# In[17]:


# sys 모듈
import sys

print(sys.copyright)
print("--구분--")
print(sys.version)


# In[22]:


# os 모듈
import os

print("현재 os 정보 :", os.name)
print("현재 경로 :", os.getcwd())
print("현재 경로 파일 :", os.listdir())


# In[26]:


#디렉토리 생성
os.mkdir("mktest")
os.listdir()


# In[27]:


# 파일명 이름 변경
os.rename('mkdir','nemkdir')
os.listdir()


# In[39]:


# 파일 삭제
#os.remove('nemkdir.txt')
# 폴더 삭제
#os.removedirs('nemkdir')
os.listdir()


# In[40]:


# cmd 명령어도 사용가능
get_ipython().system('dir')


# In[ ]:


# datetime 모듈

#datetime.datetime.now()와 .today()는 동일하다


# In[41]:


import time
print("time start")
time.sleep(3)
print("time end")


# In[80]:


#url 모듈
# 1. open 2. read
from urllib import request

target=request.urlopen("https://www.google.com")
output=target.read()

print(output)


# In[81]:


# <html> ~ </html> 로 변환해주는 모듈 : beautifulsoup

# beatifulsoup4 설치하는 방법
# anaconda cmd 콘솔에서 "pip install beautifulsoup4"

from bs4 import BeautifulSoup

target=request.urlopen("https://www.google.com")
soup=BeautifulSoup(target)


# In[82]:


soup


# In[61]:


# soup.title
# <title>The Dormouse's story</title>

# soup.title.name
# # u'title'

# soup.title.string
# # u'The Dormouse's story'

# soup.title.parent.name
# # u'head'

# soup.p
# # <p class="title"><b>The Dormouse's story</b></p>

# #soup.p['class']
# # u'title'

# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>


# In[85]:



from urllib import request
from bs4 import BeautifulSoup

target=request.urlopen("https://www.weather.go.kr/w/weather/forecast/mid-term.do")
soup=BeautifulSoup(target)


# In[88]:


# for location in soup.select("table.table-col"):
#     for td in location.select("td.midterm-province"):
#         print("도시:",td.select_one("서울"))
#     print("!! : ",location.select('서울'))

# #             for span in city.select("span.tmx"):
# for city in soup.select("td.midterm-city"):
for tr in soup.select("tr"):
    print("도시 : ",tr.select_one("td.midterm-city"))
    print("최고기온 : ",tr.select_one("span.tmx"))
    print("최저기온 : ",tr.select_one("span.tmn"))


# In[12]:


for location in soup.find_all('tr'): 
    if location.find('td', class_='midterm-city'):
        print("도시명 : {}, 최저기온 :{}, 최대기온 :{}".              format(location.find('td', class_='midterm-city').text,
                location.find('span', class_='tmn').text,
                 location.find('span', class_='tmx').text))


# In[32]:


# flask
get_ipython().system('pip install flask')


# In[35]:


from flask import Flask
app=Flask(__name__)

@app.route("/")

def hello():
    return "<h1> Hello World!</h1>"


# In[38]:


#함수 데코레이터

def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")
    
hello()


# In[40]:


# 모듈 만들기
import os
os.mkdir("modul_basic")


# In[42]:


import test_m as test

radius=test.number_input()


# In[44]:


# 제작 모듈 불러오기
import test_p.module_a as a
import test_p.module_b as b

print(a.variable_a)
print(b.variable_b)


# In[49]:


from test_p import * #__init__.py 파일을 꼭 생성해야함

print(module_a.variable_a)
print(module_b.variable_b)

