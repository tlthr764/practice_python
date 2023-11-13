# 실습1 : 사칙연산 클래스 만들기
class Cal:
  def __init__(self,a,b): # 생성자
    self.a = a
    self.b = b
  def add(self): # 덧셈함수
    return self.a+self.b 
  def sub(self): # 뺄셈함수
    return self.a-self.b
  def mul(self): # 곱셈함수
    return self.a*self.b
  def div(self): # 나눗셈함수
    return self.a/self.b
  
N, M = map(int, input().split()) # 2개의 숫자 input받기
sol = Cal(N,M)
print(sol.add())
print(sol.sub())
print(sol.mul())
print(sol.div())