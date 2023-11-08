# 실습3 : 입출력 실습
# 1번
name = input("이름을 입력하세요. ")
age = int(input("나이를 입력하세요. "))
print(f'안녕하세요! {name}님 ({age}세)')

#2번
name2 = input("이름을 입력하세요. ") 
birth = int(input("태어난 년도를 입력하세요. "))
now = int(input("올해 년도를 입력하세요. "))
print(f'올해는 {now}년, {name2}님의 나이는 {now-birth+1}세 입니다')