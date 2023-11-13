# 실습2 : Numpy 모듈 사용해보기
import numpy as np
#6. 35~74까지 순차적인 수의 1차원 배열 만들고 10x4 행렬로 변환
print("6번")
arr1=np.arange(35,75)
arr2=arr1.reshape(10,4)
print(arr2)
#7. 6번 배열을 맨 끝의 행부터 역순으로 배열
print("7번")
arr3=np.zeros_like(arr2)
arr3[:,:]=arr2[::-1,:]
print(arr3)
#8. 6번 배열중 두번째 행부터 마지막 직전행까지, 세번째열부터 마지막열까지 슬라이싱
print("8번")
arr4=arr2[1:(arr2.shape[0]-1),2:]
print(arr4)
#9. 6번 배열에서 마지막 열에 해당하는 모든값 출력(1차원 배열로)
print("9번")
arr5=arr2[:,-1:].flatten()
print(arr5)
#9-1. 6번 배열에서 마지막열에 해당하는 모든값 출력(2차원 배열로)
print("9-1번")
arr6=arr2[:,-1:]
print(arr6)
#10. 9-1번에서 만든 배열을 역순으로 정렬해서 출력
print("10번")
arr7=np.zeros_like(arr6)
arr7[:]=arr6[::-1]
print(arr7)
#11. 1~50까지 난수 5x6 배열 생성, 짝수만 선택하여 출력
print("10번")
arr8=np.random.randint(1,51,size=(5,6))
arr8=arr8[arr8%2==0]
print(arr8)