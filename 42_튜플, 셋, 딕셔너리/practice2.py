# 실습2 : 딕셔너리 사용
dict1 = {"Alice":85, "Bob":90, "Charlie":95}
dict1["David"]=80
dict1["Alice"]=88
del(dict1["Bob"])
student=""
for student in dict1:
  print(student, dict1[student])