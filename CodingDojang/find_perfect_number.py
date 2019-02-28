num_range = int(input('자연수 입력:'))
sum=0
for in_num in range(1,num_range+1):
    for num in range(1,in_num):
        if in_num%num==0:
            sum+=num
    if sum==in_num:
        print(in_num)
    sum=0