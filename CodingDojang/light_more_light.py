light_list = []
onoff_list = []
onoff=False
while True:
    n = int(input())
    if n==0:
        break
    else:
        light_list.append(n)

    for j in range(1,n+1):
        if int(n) % j==0:
            onoff = not onoff
    if onoff==True:
        onoff_list.append('yes')
    else:
        onoff_list.append('no')
    onoff=False

for i in onoff_list:
    print(i)

# 입력받으면서 바로 onoff를 체크하여 리스트에 넣고 마지막에 출력
# 나누어떨어질때마다 boolean 타입 onoff 변수를 not으로 계속 변경해주어 최종 변수값에 따라 yes, no 를 리스트에 삽입