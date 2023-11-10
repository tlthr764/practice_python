# 실습3 : 구구단 만들기
gugudan = int(input("몇 단을 출력할까요? : "))
if 0<gugudan<10:
  for i in range(1,10):
    print(gugudan," * ",i," = ",i*gugudan)
else : 
  print("잘못된 입력입니다!")