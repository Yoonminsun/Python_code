import random
input_list = [2,3,1,6,5,7]

for i in range(len(input_list)//2):
    del input_list[random.randint(0,len(input_list)-1)]

print(input_list)

## 외장함수 random을 이용하여 받은 값을 삭제할 리스트 인덱스로 이용

