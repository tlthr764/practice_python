# 실습3 : 점수를 입력 받아 등급 나누기
score = input("점수를 입력하세요. ")
grade = 'F'
if int(score) > 89 :
  grade='A'
elif int(score) > 79 :
  grade = 'B'
elif int(score) > 69 :
  grade = 'C'
elif int(score) > 59 :
  grade = 'D'
else : 
  grade = 'E'
print(f'점수 : {score}, 등급 : {grade}')