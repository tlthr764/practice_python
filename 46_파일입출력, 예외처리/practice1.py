# 실습1 : 회원명부 작성하기
file_w = open("./member.txt","w") # 파일 데이터 쓰기 위해 열기
for i in range(3): # 3명의 명부 작성
  name, pw = map(str, input(f'{i+1}번째 회원 정보를 입력해주세요 (양식 : 이름 비밀번호) : ').split()) # map으로 input
  file_w.write(name+" "+pw+"\n") # 데이터 쓰기
file_w.close() # 파일 닫기
file_r = open("./member.txt","r") # 파일 데이터 읽기 위해 열기
print(file_r.read())
file_r.close() # 파일 닫기