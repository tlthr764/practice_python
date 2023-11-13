# 실습2 : 회원명부를 이용한 로그인 기능
import practice2 # practice2 모듈 불러오기
result=practice2.login() # practice2 login 함수 불러오기
print(result)

# 실습3 : 로그인 성공 시 전화번호 저장하기
flag=False # 새로운 사람일때 변수 정의
if result=="로그인 성공!": # 로그인 성공시
  tel=input("전화번호를 입력하세요.\n") # 전화번호 입력
  file_tel=open("./member_tel.txt","r+") # member_tel 파일 r+ 모드로 열기
  while True: # 루프
    position=file_tel.tell() # 위치값 저장
    tel_line=file_tel.readline() # 한줄씩 파일 읽기
    if tel_line.find(practice2.name)!=-1: # 이미 존재하는 사람일 경우
      file_tel.seek(position) # 커서 위치값으로 이동
      file_tel.write(practice2.name+" "+tel+"\n") # 전화번호 수정
      print(f'{practice2.name}님의 전화번호가 {tel}로 수정했습니다!')
      break # 루프탈출
    if tel_line=="": # 파일을 다 읽었을경우
      flag = True # 새로운 사람 True
      break # 루프탈출
  if flag: # 새로운 사람일 경우
    file_tel.write(practice2.name+" "+tel+"\n") # 그대로 전화번호 추가
    print(f'{practice2.name}님의 전화번호 {tel}을 추가했습니다!')
  file_tel.close() # 파일 닫기