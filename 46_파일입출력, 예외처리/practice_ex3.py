# 순열과 조합
# 순열 : 반복가능한 객체(길이 n)에 대해서 중복 허용하지 않고 r개를 뽑아 나열
# 조합 : 반복가능한 객체(길이 n)에 대해서 중복을 허용하지 않고 r개를 뽑기
# 순열은 순서를 고려(순서가 다르면 다른 경우의 수)하고 조합은 고려하지 않는다
from itertools import *
# 순열 permutations
print("순열")
for i in permutations([1,2,3,4], 2):
  print(i, end=" ")

# 조합 combinations
print("\n조합")
for i in combinations([1,2,3,4], 2):
  print(i, end=" ")

# 중복순열 product
print("\n중복순열")
for i in product([1,2,3,4],'ab'):
  print(i,end=" ")
print()
for i in product(range(2),range(2),range(2)):
  print(i,end=" ")
print()
for i in product([1,2,3,4],repeat=2):
  print(i,end=" ")

# 중복조합 combinations_with_replacement
print("\n중복조합")
for cwr in combinations_with_replacement([1,2,3,4],2):
  print(cwr,end=" ")