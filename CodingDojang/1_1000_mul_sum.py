count_list=[0,0,0,0,0,0,0,0,0,0]
sum=0
for num in range(10,16):
    mul=1
    for index in str(num):
        mul*=int(index)
    sum+=mul
print(sum)