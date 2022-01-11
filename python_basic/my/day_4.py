#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factorial(n):
    output=1
    
    for i in range(1,n+1):
        output*=i
    
    return output


# In[6]:


def factorial1(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
#재귀함수는 속도가 느리기 때문에 메모화를 사용함(계산이 완료된 값을 가져옴) = 딕셔너리를 이용하면 메모화 가능


# In[ ]:


factorial1(5)


# In[8]:


def fibo(n):
    global count=0
    count+=1
    if n== 1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


# In[ ]:


fibo(5)


# In[21]:


dic={1:1,2:1}
def fibo_m(n):
    
    if n in dic:
        return dic[n]
    else:
        output =fibo_m(n-1)+fibo_m(n-2)
        dic[n]=output
        return output
    


# In[23]:


fibo_m(100)
print(dic)


# In[29]:


#tuple:수정할 수 없는 자료(),
tuple_test=(10,20,30,40)
for value in tuple_test:
    print(value)
print(tuple_test[0])
#튜플은 수정 불가

a,b,c=10,20,30
print(a)

a,b=10,20
print("before a:{}, b:{}".format(a,b))

a,b=b,a #교환 가능
print("after a:{}, b:{}".format(a,b))


# In[30]:


for idx, value in enumerate([1,2,3,4,5]):
    print("{}번째 값 : {}".format(idx,value))
    
a,b=divmod(88,3)
print("88/3= {}, {}".format(a,b))


# In[34]:


#map과 filter 함수 => map(함수, 리스트), filter(함수, 리스트)
# def power(n):
#     return n*n
# def under_3(n):
#     return n<3

#lambda 매개변수 : 리턴값
power=lambda x:x*x
under_3=lambda x:x<3

a_list=[1,2,3,4,5]
b_list=list(map(power,a_list))
print(b_list)

c_list=list(filter(under_3,a_list))
print("\n",c_list)


# In[36]:


#간단한 작성법

b_list=list(map(lambda x:x*x,a_list))
b_list


# In[ ]:





# In[35]:


c_list=list(filter(lambda x:x<3,a_list))
c_list


# In[41]:


#file 처리 : open, close, write, read...
file=open("a.txt","w")
file.write("Hello Python file write !!")
file.close()


# In[44]:


#file 처리 : open, close, write, read...
file=open("a.txt","r")
print(file.read())
file.close()


# In[47]:


#파일을 자동으로 close() 시킴
with open("a.txt","w") as file:
    file.write("with python file open!!\n")
    file.write("with python file open!!\n")
    file.write("with python file open!!\n")
#with 구문이 끝나게 되면 파일은 자동으로 close 되기 때문에 불러오면 에러 발생
# file_data=file.read()


# In[48]:


#저장된 파일의 내용을 라인 단위로 읽어옴
with open("a.txt", "r") as file:
    for line in file:
        print(line)


# In[ ]:


#키보드에서 이름 성적을 입력받아 파일에 저장
with open("score.txt", "w") as file:
    name, score = input("이름 성정 입력 : ").split() #튜플로 받기
    file.write(name+','+score)
#저장 경로 C:\Users\JYP\Documents\python_basic


# In[92]:


#키보드에서 이름 성적을 입력받아 파일에 저장
with open("test.txt", "w") as file:
    name = input("이름 성정 입력 : ")
    file.write(name)


# In[54]:


with open("score.txt","r") as file:
    for line in file:
        name, score = line.split(',')
        print(name,':',score)


# In[55]:


file=open("score.txt","a+") #a+를 입력해야 파일이 추가됨
name,score=input("이름 성적 입력 : ").split()
file.write(name+','+score+'\n')

file.seek(0,0) #파일의 처음 위치로 이동
for line in file:
    name, score=line.split(',')
    print(name,':',score)
file.close()


# In[117]:


#이름, 국어, 영어, 수학 성적을 입력받아 파일 저장한 후 (file_write())
#검색할 이름을 입력받아 파일에서 데이터 검색 (file_search())
#검색한 이름과 성적 출력
#전체 학생의 인원수와 총점 평균을ㄹ 구함 (file_total())

def file_write(file):
    while True:
        name=input("이름 : ")
        if name=='q':
            print("입력 종료")
            break

            
        score=','.join(input("국어 영어 수학 점수 : ").split())
        #score=list(map(int,score))
        file.write(name+','+score+"\n")
               

def file_search(file):
    search=input("검색할 이름 : ")
    file.seek(0,0)
    for i in file:
        f_data=i.split(',')
        if f_data[0]==search:
            return f_data
    return None

def file_total(file):
    total=0
    count=0
    file.seek(0,0)
    for line in file:
        count+=1
        f_data=line.split(',')
        f_score=list(map(int,[x for x in f_data[1:]])) # 이 형태로만 리스트로 뽑아낼 수 있다
        total+=sum(f_score)
    return total, count


# In[101]:


file =open("score.txt","a+")
file_write(file)


# In[115]:


name_search=file_search(file)
if name:
    print("{}의 성적은 {}, {}, {}".format(name_search[0],name_search[1],name_search[2],name_search[3]))
else:
    print('검색된 자료 없음')

total, count = file_total(file)
print("총 인원수 : {}\t 총점 : {:5.2f}, 평균 :{:5.2f}".format(count,total,total/3/count))


# In[124]:


# 제너레이터 함수 실행 : next(함수명), 함수 내부에 return 대신 yield 사용
def test():
    print("함수 호출 !!")
    yield "test"
    
    print("함수 호출 22")
    yield "222"
    
#함수호출
print("first call function")
test()

print("second call function")
test()

#제너레이터는 디버깅용으로 사용
a=test()
c=next(a)
print(c)

print("next")

d=next(a)
print(d)


# In[126]:


#269p 연습문제2
numbers=list(range(1,10+1))
print("홀수만 출력")
print(list(filter(lambda x:x%2,numbers)))

print("3이상 7미만 자료만 출력")
print(list(filter(lambda x:3<=x<7,numbers)))

print("제곱해서 50미만 자료만 출력")
print(list(filter(lambda x:x*x<50,numbers)))


# In[129]:


#예외상황 발생시 처리
try:
    input_number=int(input("정수 입력 :"))
    print("원의 반지름 : ",input_number)
    print("원의 둘레 : ",input_number*3.14*2)
    print("원의 넒이 : ",input_number*input_number*3.14)
# except:
#     print("입력 오류")
except:
    pass


# In[133]:


#try except:pass
list_data=['52','2','test','123','44']
#숫자만 리스트에 추가
list_number=[]
for item in list_data:
    try:
        int(item) #float or int
        list_number.append(item)
    except:
        pass
    
#     try: #에러 발생 가능 코드구현
#         int(item) #float or int
        
#     except:#에러 발생시 실행하는 코드
#         pass #그냥 넘어감
#         Exception as e: print(e) #에러를 보여줘라
    
#     else: #에러가 발생하지 않으면 실행하는 코드
#         list_number.append(item)

#     finally: #무조건 실행하는 구간이라 에러가 발생하더라도 파일을 닫고 끝내려면 여기에 작성
#         print("무조건 실행!!")

print(list_number)


# In[150]:


#try~except~finally
try:
    file=open("info.txt","w")
    file.read()
    file.close()
except Exception as e:
    print(e)
finally:
    file.close()

print(file.closed)


# In[141]:


def test():
    print("test 함수 시작 !!")
    try:
        print("test try start")
        return
        print("try 구문 return 다음 문장")
    except:
        print("except 구문")
    finally:
        print("finally 구문") #위에서 return 되더라도 finally 구문은 무조건 실행
    print("test 함수 end")
    
test()


# In[142]:


while True:
    print("test 함수 시작 !!")
    try:
        print("test try start")
        break #break 구문을 만나도 finally는 실행된다
        print("try 구문 return 다음 문장")
    except:
        print("except 구문")
    finally:
        print("finally 구문")
    print("test 함수 end")
    
print("while end")


# In[184]:


list_number=[52, 2, 33, 123, 44]
#숫자만 리스트에 추가
try:
    input_num=int(input("정수 입력 : "))
    print("{}번째 요소 : {}".format(input_num,list_number[input_num]))
except ValueError as ex:
    print("정수를 입력 :",ex)
except IndexError as ex:
    print("리스트의 인덱스 범위 오류 :",ex)
except Exception as ex:
    print("알 수 없는 오류",ex)


# In[ ]:


#이름 전화번호를 파일에 저장하는 프로그램 작성
#파일 이름은 "dataset/elno.txt", 기존에 파일이 존재하면 데이터 추가로
#전화번호 입력은 숫자 3개를 입력받아 123-456-789 형식으로 저장,
#이름과 전화번호는 ' ' 분리해서 저장
#저장이 끝나면 파일을 닫고
#다시 파일을 open->'r'
#파일의 내용을 화면에 출력
#-- 홍길동 123-456-7899
#try ~ except ~ finally 사용해서 작성

