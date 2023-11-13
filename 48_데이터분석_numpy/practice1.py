# 실습1 : Numpy 모듈 사용해보기
import numpy as np
#1. 10개의 0으로 채워진 array
array1=np.zeros(10)
print(array1)
#2. 1번 array 5번째 값 1로 바꾸기
array1[5]=1
print(array1)
#3. 10~30까지 array
array2=np.arange(10,31)
print(array2)
#4. 0~99까지 난수 2x2 array
array3=np.random.randint(0,99, size=(2,2))
print(array3)
#5. 0~1까지 난수 2x4 array
array4=np.random.rand(2,4)
print(array4)