# 실습5 : 최대 최소 중복 포함 제거한 리스트 평균 구하기

num_list=list(map(int, input("숫자 여러개를 띄어쓰기로 입력하세요 : ").split()))
max_num = max(num_list)
min_num = min(num_list)
print(f'가장 큰 값 : {max_num} / 가장 작은 값 : {min_num}')

while True:
    num_list.remove(max_num)
    if max_num not in num_list: break
while True:
    num_list.remove(min_num)
    if min_num not in num_list: break
num_list.sort()

average = sum(num_list)/len(num_list)
print(num_list)
print(f'최대 최소 제외한 평균값 : {average}')

# 기존 코드
# input_list = input("숫자 여러개를 띄어쓰기로 입력하세요 : ")
# string_list = input_list.split(" ")
# num_list = [int(item) for item in string_list] 
# max_count=num_list.count(max_num)
# min_count=num_list.count(min_num)

# flag_max =0
# while flag_max < max_count:
#     num_list.remove(max_num)
#     flag_max += 1

# flag_min =0
# while flag_min < min_count:
#     num_list.remove(min_num)
#     flag_min += 1