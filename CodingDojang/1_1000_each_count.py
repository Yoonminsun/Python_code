count_list=[0,0,0,0,0,0,0,0,0,0]

for num in range(10,16):
    for index in str(num):
        count_list[int(index)]+=1

print(count_list)
