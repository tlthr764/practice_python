# 실습4 : 정수 입력 받기
while True:
  try:
    num=int(input("숫자 입력 : "))
  except ValueError:
    print("정수가 아님! 정수를 입력해주세요!")
  else:
    print(f"정수 입력 성공 : {num}")
    break
# 모든 에러 표시
# except Exception as err
#    print(err)