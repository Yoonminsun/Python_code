my_list = [5,2,4,6,1,3]
index_current=1
move_flag=0
insertion_position=0

while index_current<len(my_list):
    for i in range(index_current-1,-1,-1):
        if my_list[i]>my_list[index_current]:
            insertion_position=i
            move_flag=1
    if move_flag==1:
        my_list.insert(insertion_position,my_list.pop(index_current))
    index_current+=1
    move_flag=0

print(my_list)

# 아래 기능의 sort 프로그램 작성
# 1.배열의 두번째 인덱스부터 시작하여 시작한 인덱스(검정색 블록) 좌측의 항목 중 자신이 들어가야 할 위치를 판단(소트되도록)하여 이동 한다.
# 2.좌측의 배열 요소들은 본인보다 좌측에 값이 삽입되어 들어올 경우 한칸씩 우측으로 이동한다.
#   단, 삽입되어 들어오는 요소(그림에서 검정색 블록)가 있던 인덱스(원래의 위치)까지만 이동한다.
# 3.마지막 인덱스까지 위 과정을 반복한다.
