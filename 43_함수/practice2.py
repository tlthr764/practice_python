# 실습2 : 재귀함수로 피보나치 수 구하기
def fibonacci(n):
  if n==1 or n==2:
    return 1
  elif n >2:
    return fibonacci(n-1) + fibonacci(n-2)
  
for i in range(1,11):
  print(fibonacci(i)," ", end="")

# dict(딕셔너리) 명령어를 사용하여 재귀함수 호출을 단축 가능 -> 시간단축
memory = {1:1, 2:1}

def fibo_memory(n):
  if n in memory:
    return memory[n]
  else :
    memory[n]=fibo_memory(n-1)+fibo_memory(n-2)
    return memory[n]

print() 
for i in range(1,100):
  print(fibo_memory(i)," ", end="")