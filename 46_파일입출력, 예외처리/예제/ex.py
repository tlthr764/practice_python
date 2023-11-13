# 예제 : 파일 입출력
# w : 파일 쓰기 (기존 내용 모두 사라지고 새로 작성)
f=open("./test.txt","w")
print(f.tell())
f.write("Hello World\nHi\n")
print(f.tell())
f.close()

# r : 파일 열기 (기본값)
f2 = open("./test.txt","r")
f_list =f2.readlines()
print(f_list)
f2.close()

# a : 파일 뒷부분에 쓰기
f3 = open("./test.txt","a")
f3.write("Hello World 2\n")
f3.close()

# 유용한 단축키들
# Shift+Alt : 여러 문장 선택
# Ctrl+/ : 주석 지정/해제
# F2 : 이름 변경(변수, 파일 등)
