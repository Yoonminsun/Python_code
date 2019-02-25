my_list = []
n,k = map(int,input("입력(n,k/ 공백구분):").split(' '))
index_current=0
cycle=0

for i in range(1,n+1):
    my_list.append(i)

while len(my_list)!=1:
    for i in range(len(my_list)):
        index_current+=1 # k와의 배수관계를 알아보기위해 1부터 시작
        if index_current%k==0:
            # 현재 index는 계속 증가하며 k의 배수인지 확인, 다음 라운드에서 인덱스 카운트를 이어서 하기 위함
            del my_list[i-cycle]
            # 요소가 지워져서 index가 하나씩 줄어들기 때문에 한 cycle 안에서는 index를 점차 줄여 삭제
            cycle+=1
    cycle=0
print(my_list[0]) # 마지막 남은 병사



