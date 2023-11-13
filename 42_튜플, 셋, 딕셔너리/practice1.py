import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for i in range(0, N):
  S.add(input())
count = 0
for i in range(0,M):
  t = input()
  if t in S:
      count += 1
print(count)