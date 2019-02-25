rotation_num=0
list_in = input("입력: ").split(' ')
rotation_num = int(list_in[0])
del list_in[0]

for i in range(abs(rotation_num)):
    if rotation_num>0:
        list_in.insert(0,list_in.pop(-1))
    elif rotation_num<0:
        list_in.append(list_in.pop(0))

print(list_in)

# 회전수가 양,음 인것에 따라 다르게 구현, 0일 경우는 그대로