# 실습3 : 로또 번호 뽑기
from random import * # random 모듈 불러오기
lotto_list=[] # 로또번호 리스트 생성
while True: # 루프문
  lotto=randint(1,45) # 1~45까지 랜덤숫자 생성
  if lotto not in lotto_list: # 중복 필터링 조건문
    lotto_list.append(lotto) # 리스트에 숫자 추가
  if len(lotto_list)==6: # 6개 숫자 뽑은 경우
    break # 루프 탈출
print(lotto_list)

 # random.sample : 중복없이 숫자 뽑기   
lotto_num=list(range(1,45))
lotto2=random.sample(lotto_num,6)
print(lotto2) 