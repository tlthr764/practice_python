# 과제3 : 자판기 프로그램 응용
# 조건1. 사용자는 소비자 또는 주인 입력, 그 외의 값 잘못된 값으로 출력
# 조건2. 소비자일 때 마시고 싶은 음료 입력
# 조건2-1. 값이 있으면 vending_machine에서 제거, 없으면 없음 출력
# 조건3. 주인일 때 추가, 삭제 두가지 종류 입력 (조건1과 동일)
# 조건3-1. 추가일 때 추가 음료수 입력 리스트에 추가 후, 같은값끼리 연결되게 출력
# 조건3-2. 삭제일 때 삭제 음료수 입력 값이 있으면 제거, 없으면 없음 출력
vending_machine=['게토레이','게토레이','레쓰비','레쓰비','생수','생수','이프로'] #음료리스트

while True: 
  print(f'남은 음료수 : {vending_machine}') #음료리스트 출력
  user=input("사용자 종류를 입력하세요\n1. 소비자\n2. 주인\n") #조건1
  if user=="1" or user=="소비자": #조건1. 소비자
    drink,num=map(str,input("마시고 싶은 음료와 개수를 입력해주세요 (양식 : 음료 개수)\n").split()) #조건2
    if drink in vending_machine: #조건2. 값 존재
      drink_count=vending_machine.count(drink)
      if int(num)<drink_count+1:
        while True:
          vending_machine.remove(drink) #조건2-1. 음료 제거
          if drink not in vending_machine: break
      else:
        print(f'{drink}가 부족합니다! 현재 {drink}의 개수 : {drink_count}') #조건2-1. 음료 부족
    else:
      print(f'{drink}는 현재 자판기에 존재하지 않습니다...') #조건2. 값 없음
  elif user=="2" or user=="주인": #조건1. 주인
    work=input("할 일을 선택하세요\n1. 추가\n2. 삭제\n") #조건3
    if work=="1" or work=="추가": #조건3. 추가
      new_drink,new_num=map(str,input("추가할 음료와 개수를 입력해주세요 (양식 : 음료 개수)\n").split()) #조건3-1
      if int(new_num)>0:
        for i in range(int(new_num)):
          vending_machine.append(new_drink) #조건3-1. 음료 리스트에 추가
        vending_machine.sort() #조건3-1. 같은값끼리 연결
        print("추가 완료")
      else: 
        print("※오류 : 잘못된 입력입니다!") #조건3-1. 음료 개수 오입력
    elif work=="2" or work=="삭제": #조건3. 삭제
      del_drink,del_num=map(str,input("삭제할 음료와 개수를 입력해주세요 (양식 : 음료 개수)\n").split()) #조건3-2
      if del_drink in vending_machine: #조건3-2. 값 존재
        del_count=vending_machine.count(del_drink)
        if int(del_num)<del_count+1:
          while True:
            vending_machine.remove(del_drink) #조건3-2. 음료 삭제
            if del_drink not in vending_machine: break
          print("삭제 완료")  
        else:  
           print(f'삭제하려는 {del_drink}의 개수가 현재 개수보다 많습니다! 현재 {del_drink}의 개수 : {del_count}') #조건3-2. 입력 개수 초과
      else:
        print(f'{del_drink}는 현재 자판기에 존재하지 않습니다...') #조건3-2. 값 없음
    else:
      print("※오류 : 잘못된 일입니다!") #조건3. 잘못된 입력
  else:
      print("※오류 : 잘못된 사용자입니다!") #조건1. 잘못된 입력
