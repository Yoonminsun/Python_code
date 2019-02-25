my_list = [-1,1,3,-2,2]

list_positive=[]
list_negative=[]

list_positive = list(filter(lambda x:x>0, my_list))
list_negative = list(filter(lambda x:x<0, my_list))
my_list = list_negative + list_positive

print(my_list)

## 양수 인덱스를 찾으면 그 후 음수를 찾아 pop한 후 insert 해주는 방법
# index_positive=0
#
# for i in range(len(my_list)-1):
#     if my_list[i]>0:
#         index_positive = i
#     else:
#         continue
#     for i in range(i+1, len(my_list)-1):
#         if my_list[i]<0:
#             my_list.insert(index_positive,my_list.pop(i))
#
# print(my_list)

## 각 음수,양수를 필터링하여 리스트를 만든 후 다시 합치는 방법
# list_positive=[]
# list_negative=[]
#
# for i in my_list:
#     if i<0:
#         list_negative.append(i)
#     elif i>0:
#         list_positive.append(i)
#
# my_list = list_negative + list_positive
# print(my_list)



