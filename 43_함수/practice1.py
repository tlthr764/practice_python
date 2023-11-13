# 실습1 : 자판기 프로그램 함수화
drink =['게토레이','게토레이','나랑드사이다','레쓰비','삼다수','삼다수','삼다수','코카콜라']
#1. 남은 음료수 확인 함수
def check_machine():
  print(drink)

#2. 음료수가 있는지 확인 함수  
def is_drink():
  name=input("마시고 싶은 음료 이름을 입력하세요 : ")
  if name in drink:
    print(f'{name}의 갯수 : {drink.count(name)}')
  else :
    print(f'{name}은 현재 존재하지 않습니다!')

#3. 음료수 추가 함수    
def add_drink():
  add_some=input("추가할 음료 이름을 입력해주세요 : ")
  drink.append(add_some)
  drink.sort()

#4. 음료수 제거 함수
def remove_drink():
  remove_some=input("제거할 음료 이름을 입력하세요 : ")
  if remove_some in drink:
    drink.remove(remove_some)
  else:
    print(f'해당 {remove_some}은 자판기에 존재하지 않습니다!')