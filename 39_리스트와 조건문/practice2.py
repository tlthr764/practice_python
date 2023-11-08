# 실습2 : 숫자를 입력받아 홀짝 구분하기
num = int(input("숫자를 입력해주세요. "))
sol = "홀수"
if num%2 == 0 :
  sol = "짝수"
print(f'숫자 {num}은 {sol}입니다.')