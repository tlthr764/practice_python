# 실습4
'''
a = input("첫번째 세자리 자연수")
b = input("두번째 세자리 자연수")
aa = int(a)
bb = int(b)
print(aa*(bb%10))
print(aa*(bb//10%10))
print(aa*(bb//100))
print(f'곱셈 결과 : {aa*bb}')
'''
"""
리스트
"""
# 실습5
'''
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[2])
sol2 = sorted(rainbow)
print(sol2)
rainbow.append("black")24
print(rainbow)
del rainbow[2:6]
print(rainbow)
'''
# 실습6 홀짝
"""
a=input("숫자를 입력하세요. ")
if int(a)%2 == 0:
    print("짝수입니다. ")
else :
    print("홀수입니다. ")
"""
'''
a=input("숫자를 입력하세요")
str = "짝수"
if int(a)%2==1:
    str = "홀수"
print(str)
'''
# 실습7 짝수
'''
score = input("점수를 입력 : ")
if len(score) == 3 :
    print("와우 ~ 만점입니다! 등급 : A+")
elif len(score) == 2 :
    if score[0] == 9 :
        print("등급 : A")
    elif score[0] == 8 :
        print("등급 : B")
    elif score[0] == 7 :
        print("등급 : C")
    elif score[0] == 6 :
        print("등급 : D")
    else :
        print("등급 : E")
else :
    print("재수강")
    '''

#실습8 교통비
age = int(input("나이를 입력하세요 : "))
pay = int(input("결제 방법을 선택하세요 (카드 : 1 현금 : 0)"))
way ="현금"
if pay&1 :
   way = "카드"
if age<8 or age >74 :
    price = 0
elif 7<age<14 :
    price = 450
elif 13<age<20 :
    if pay&1 :
      price = 720
    else :
      price = 1000
elif 19<age<75:
     if pay&1 :
      price = 1200
     else :
      price = 1300
else :
   print("오류")
print(f'나이 : {age} / 결제방법 : {way} / 요금 : {price}')