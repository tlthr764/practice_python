# 실습2 : 회원명부를 이용한 로그인 기능
def login():
  name,pw=input("이름과 비밀번호를 입력하세요. (양식 : [이름 비밀번호] )\n").split() # 이름, 비밀번호 입력받기
  file=open("./member.txt","r") # member.txt 읽기모드로 열기
  member_list=file.readlines() # member_list에 readlines로 정보 저장
  file.close() # member.txt 닫기
  member_dict={} # 딕셔너리 생성

  for i in range(len(member_list)): # 리스트 사이즈만큼 for문
    member_info=member_list[i].split() # 리스트 split
    member_dict[member_info[0]]=member_info[1] # name:pw 로 dict에 추가

  result="로그인 실패..." # 결과 실패 기본값 
  if name in member_dict.keys(): # name이 dict키일 때
    if member_dict[name] == pw: # name을 키로 가진 dict변수가 pw일 때
      result="로그인 성공!" # 결과 성공으로 변경
  return result # 결과 출력