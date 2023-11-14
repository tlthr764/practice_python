# 실습1 : Numpy 모듈 사용해보기
import numpy as np
data = [1,1,2,3,4,5,5,5,5,7,8,9,10,11,24,100]
#1. 중복제거한 배열 출력
unique_data,indexes,counts=np.unique(data,return_counts=True,return_index=True)
print(unique_data)
#2. 1의 결과의 최대,최소,평균값 출력
max_num=np.max(unique_data)
min_num=np.min(unique_data)
mean_num=np.mean(unique_data)
print(f'최대값 : {max_num}, 최소값 : {min_num}, 평균값 : {mean_num}')
#3. 1의 결과의 모든 합 출력
sum_num=np.sum(unique_data)
print(f'중복제거데이터의 모든합 : {sum_num}')
#4. 중복을 제거하지 않은 배열의 중간값 출력
print(f'원 배열의 중간값 : {np.median(data)}')