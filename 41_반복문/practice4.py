# 별찍기
#1
column = int(input("몇 줄? : "))
star = "*"
for i in range(column):
   print(star*(i+1))

#2 
column2 = int(input("몇 줄? : "))
space =" "
for i in range(column2):
  print(space*(column2-(i+1)),star*(i+1))

#3
column3 = int(input("몇 줄? : "))
for i in range(column3):
  print(space*(column3-(i+1)),star*(1+2*i))