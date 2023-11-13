# 실습1 : 랜덤 모듈 사용해보기
from random import * # random 모듈 불러오기
rand_list=[] # 리스트 생성
for _ in range(4): # 4개 숫자 받기
  rand_list.append(randint(1,100)) # 1부터100까지 숫자 랜덤 생성 및 추가
rand_list.sort()
print(rand_list)