import calc_module # 같은 폴더 내에 있는 calc_module.py 모듈 불러오기
import math # math 모듈 불러오기

print(calc_module.add(2,3))
print(calc_module.sub(2,3))
print(calc_module.mul(2,3))
print(calc_module.div(2,3))

print(math.floor(math.pi))
print(math.ceil(math.pi))
print(math.sqrt(9))
#반올림 : int(x+0.5)