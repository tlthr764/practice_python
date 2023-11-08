# 실습 1 : 리스트 예제
rainbow = ['red','orange','yellow','green','blue','indigo','purple']

#1 2번 인덱스값 출력
print(rainbow[2])

#2 알파벳 순서로 정렬한 값 출력
print(sorted(rainbow))

#3 좋아하는 색 마지막에 추가하기
rainbow.append("skyblue")
print(rainbow)

#4 3~6번째 값 삭제하기
del rainbow[2:6]
print(rainbow)