#실습2 : 입력한 숫자만큼 카운트하고 발사 출력
import time
count_num = int(input("카운트 할 초를 입력하세요 : "))
if count_num > 0 :
  count_list = list(range(count_num,0,-1))
  for i in range(count_num):
    print(count_list[i]," ",end="")
    time.sleep(1)
  print("발사")  
else :
  print("잘못된 입력입니다!")