# 실습2 : 숫자 맞추기 게임
from random import * # random 모듈 불러오기
target=randint(1,10) # 1부터 10까지 랜덤 숫자 생성
flag = True # 루프 탈출 변수 정의
while flag: # 루프문
  dart=int(input("숫자를 맞춰보세요 : ")) # 숫자 입력받기
  sol = print("땡!") # 출력함수 정의
  if dart == target: # 랜덤숫자==입력숫자
    sol = print(f'맞았어요! 랜덤 숫자는 {target} 입니다!')    
    flag =False # 루프 탈출
