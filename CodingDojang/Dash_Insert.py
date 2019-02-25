num_str = input('입력: ')
num_str_list=[]
ex_num=num_str[0]
num_str_list.append(ex_num)
for index_num in range(1,len(num_str)):
    if int(ex_num)%2==0 and int(num_str[index_num])%2==0:
        num_str_list.append('*')
        num_str_list.append(num_str[index_num])

    elif int(ex_num)%2==1 and int(num_str[index_num])%2==1:
        num_str_list.append('-')
        num_str_list.append(num_str[index_num])
    else:
        num_str_list.append(num_str[index_num])
    ex_num = num_str[index_num]

print(''.join(num_str_list))