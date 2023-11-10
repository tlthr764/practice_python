# 실습1 : 1부터n까지 정수의 합 계산
# 번외 : 홀수의 합만 구하기
num = int(input("정수를 입력하세요 : "))
num_list = list(range(1,num+1))
odd_list = list(range(1,num+1,2))
sum1=sum(num_list)
sum2=sum(odd_list)
print(f'{num}까지 정수의 합 계산\n정수의 합 : {sum1}\n홀수의 합 : {sum2}')