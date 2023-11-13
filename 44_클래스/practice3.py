# 실습3 : Calculator 클래스 상속 받아서 클래스 만들기
class Calculator(): # 부모클래스
    def __init__(self):
        self.value=100
    def sub(self,value): #부모클래스 sub함수
        self.value -=value
class MinLimitCalculator(Calculator): #자식클래스
    def sub(self,value): # sub함수 오버라이딩
      super().sub(value) #부모클래스 함수 상속 시 super() 사용
      if self.value < 0:
        self.value = 0

cal=MinLimitCalculator()
print(cal.value)
cal.sub(20)
print(cal.value)
cal.sub(90)
print(cal.value)