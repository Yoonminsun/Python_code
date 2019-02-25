my_list = []
num1=0
num2=0
in_count=0
add=0
carry=0
carry_count=0

while True:
    in_str = input()
    if in_str=='0 0':
        break
    my_list.append(in_str)

for i in my_list:
    num1,num2 = i.split(' ')
    while in_count<len(num1):
        add = int(num1[in_count]) + int(num2[in_count]) + carry
        carry=0
        in_count+=1
        if add>=10:
            carry=add-9
            carry_count+=1
    if carry_count==0:
        print("No carry operation.")
    else:
        print("%d carry operation."%carry_count)
    carry_count=0
    in_count=0
    add=0
    carry=0

# 각 인덱스마다 더하여 10이상이면 carry_count를 +1 해주는 방식으로 구현함

