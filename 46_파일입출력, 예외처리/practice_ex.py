# 람다(lambda) 함수
# lambda 인자 : 표현식

# add 기본형
def add(x,y):
  return x+y
# add함수 람다함수로 표현
add = lambda x,y:x+y

mylist=[1,2,3,4,5]
# 리스트의 각 요소에 2곱하기
mylist2=[]
for i in mylist:
  mylist2.append(2*i)
print(mylist2)

#1. 리스트 각 요소에 2곱하기 : 람다함수로
mylist3=list(map(lambda x: x*2, mylist))
print(mylist3)
#2. 리스트에서 홀수만 추출 : filter()함수 사용
mylist4=list(filter(lambda x:x%2==1,mylist))
print(mylist4)

#3. 리스트 길이순으로 정렬
wordlist=['apple','banana','cherry','deltaforce']
wordlist2=sorted(wordlist, key=lambda x: -len(x))
print(wordlist2)

#4. 리스트의 모든 요소 곱하기 : reduce()함수 사용
from functools import reduce
result=reduce(lambda x,y:x*y,mylist)
print(result)