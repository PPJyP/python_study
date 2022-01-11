#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

dic ={'a':1,'b':2,'c':3}
list_a=[1,2,3]

srd=pd.Series(dic)
srl=pd.Series(list_a)

print(type(dic),dic)
print(type(srd),srd)

print(type(list_a),list_a)
print(type(srl),srl)


# In[ ]:





# In[17]:


sr_data=pd.Series(list(range(10)))
sr_data[1:4]

sr_key={'a':1,'b':2,'c':3,'d':4}
sr=pd.Series(sr_key)


# In[18]:


print(sr_data[:3])

print(sr['a' : 'c']) # 문자는 c까지 출력
print(sr[0:3]) # 숫자는 2까지 출력


# In[20]:


#데이타프레임
dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9]}

df=pd.DataFrame(dict_data)
print(df)


# In[22]:


df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
               index=['준서','예은'],
               columns=['나이','성별','학교'])

print(df)


# In[25]:


# 인덱스명 변경
df.index=['a','b','c']
print(df)
df.columns=['연령','남녀','소속'] # 원데이터를 바꿈
print(df)


# In[30]:


# 일부 인덱스만 변경
# df.rename(index={'a':'준서'},columns={'소속':'학교'}) #바뀜(원데이터를 바꾸진 않음)
# df # 안바뀜


df.rename(index={'a':'준서'},columns={'소속':'학교'},inplace=True) #바뀜(실제 매핑하려면 inplace 사용)
df # 바뀜


# In[33]:


#행과 열을 삭제

df.drop('준서',axis=0) # 원데이터를 삭제하진 않음
df.drop('학교',axis=1) # 데이터를 삭제하려면 inplace=True 적용할 것


# In[38]:


students=[]
def creat_stu():
    value=[]
    while True:
        name=input("이름 입력 :")
        if name=='q':
            break
        value.append(name)
        score=list(map(int, input("점수 입력 :").split()))
        students.append(value.extend(score))


# In[39]:


creat_stu()


# In[43]:


df=pd.DataFrame(students,columns=['이름','국어','영어','수학'])


# In[23]:


df.loc['철수']=[17,'남','삼중']
print(df)


# In[50]:


# 행선택

exam_data={'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}

df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df)

labell=df.loc['서준']
position1=df.iloc[0]
print(labell)
print(position1)


# In[54]:


#행선택
#리스트로 여러개 출력
label2=df.loc[['서준','우현']]
position2=df.iloc[[0,1]]

print(label2)
print(position2)


#범위 선택
label3=df.loc['서준':'우현']
position3=df.iloc[0:1]

print(label3)
print(position3)


# In[59]:


#열선택
df.수학
print(df['수학':'음악'])
print(df[['수학','음악']])


# In[63]:


#범위 슬라이싱 df.iloc[start:end:step]
df.iloc[::-1]
df.iloc[::2]
df.iloc[0:3:1]


# In[80]:


print(df.loc['우현','음악'], df.iloc[0,1])
#서준과 인아의 수학 영어 점수
print(df.loc[['서준','인아'],['수학','영어']])
print(df.loc['서준':'인아','수학':'음악'])

#서준의 수학과 체육 점수만 출력
print(df.loc['서준',['수학','영어']])

# 새로운 행 추가(철수 추가)
df.loc['철수']=[80,90,50,100]
df

# 새로운 열 추가
df['국어']=[100,55,80,20]
df


# In[82]:


# 기존 행을 복사해서 추가
df.loc['추가']=df.loc['서준']
df


# In[89]:



score_df=pd.DataFrame(columns=['kor','eng','math'])


# In[ ]:


def create_score():
    while True:
        name=input("이름 입력 :")
        if name=='q':
            break
        
        score=list(map(int, input("점수 입력 :").split()))
        score_df.loc[name]=score


# In[127]:


# def serch_score():
#     s_name=input("검색할 이름:")
#     return score_df.loc[s_name]
# def serch_title():
#     s_title=input("검색할 과목:")
#     return score_df[s_title]
def serch_score():
    s_name=input("검색할 이름:")
    if not s_name in score_df.index:
        print("존재하지 않는 이름")
        return 
    s_title=input("검색할 과목:")
    print("{}의 {}과목 점수는 : {}".format(s_name,s_title,score_df.loc[s_name,s_title]))
    return 

def add_score():
    name=input("이름 입력 :")
    score=list(map(int, input("점수 입력 :").split()))
    score_df.loc[name]=score
    return score_df


# In[91]:


#연습문제
create_score()
score_df


# In[129]:


serch_score()


# In[116]:


# serch_title()


# In[ ]:





# In[95]:


add_score()


# In[ ]:


#점수 수정
score_df.loc['c','eng']=99


# In[131]:


score_df

