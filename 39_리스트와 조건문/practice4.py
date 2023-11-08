# 실습4 : 교통비를 낼때 나이와 결제방법에 따른 금액 출력
age = int(input("나이를 숫자로 입력해주세요 : "))
pay = input("결제방법을 입력해주세요 ('카드' 또는 '현금'만 입력) : ")
fee_card = [0, 450, 720, 1200]
fee_cash = [0, 450, 1000, 1300]
fee = fee_card
if pay=="현금" :
  fee = fee_cash
if 19<age<75 :
  output = fee[3]
elif 13<age<20 :
  output = fee[2]
elif 7<age<14 :
  output = fee[1]
else :
  output = fee[0]
print(f'나이 : {age}')
print(f'결제방법 : {pay}')
print(f'요금 : {output}')