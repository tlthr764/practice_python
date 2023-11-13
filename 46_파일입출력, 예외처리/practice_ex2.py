# enumerate() 함수
# for루프에서 i,j,k와 같은 인덱스변수를 증가시키지 않고,
# enumerate() 함수를 사용

# for 루프 : for <원소> in <목록>
# <목록> : 리스트, 튜플, 문자열, 반복자, 제너레이터 등 순회가능한 데이터 타입
# <원소> : 순회변수, <목록> 부분에 넘긴 원소들이 루프가 도는 동안 하나씩 차례로 할당
for letter in ['A','B','C']:
  print(letter)

# 원소뿐만 아니라 인덱스도 함께 출력하기
i=0
for letter in ['A','B','C']:
  print(i, letter)
  i+=1
# i 변수가 for문이 종료된 이후에도 네임스페이스에 남아있음!

# range(), len() 함수 사용하여 인덱스 목록 출력하기
letters = ['a','b','c']
for i in range(len(letters)):
  letter=letters[i]
  print(i,letter)
# pythonic 하지는 않다!

# enumerate() 함수 사용
for entry in enumerate(letters):
  print(entry)
# 인덱스와 원소 다른 변수에 할당하기
for index, entry in enumerate(letters):
  print(index,entry)
# 시작 인덱스 변경
for index, entry in enumerate(letters,start=100):
  print(index,entry)