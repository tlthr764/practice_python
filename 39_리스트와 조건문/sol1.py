# 과제1 : 리스트 슬라이싱
# 1) 정수 n 입력 받아 1부터 n까지  정수 리스트 만들기
# 2) 슬라이싱 사용해서 홀수,짝수만 출력

#1.
n = int(input("정수 n을 입력하세요. ")) 
num_list = list(range(1,n+1))
print(f'전체: {num_list}')

#2.
print(f'홀수 : {num_list[::2]}')
print(f'짝수 : {num_list[1::2]}')