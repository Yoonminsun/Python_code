while True:
    sum=0
    input_z = int(input("범위 입력(0은 종료): "))
    if input_z == 0:
        exit()
    input_x,input_y = map(int,input("x,y 공백구분 입력 : ").split(' '))
    for i in range(input_z+1):
        if i%input_x==0 or i%input_y==0:
            sum+=i

    print(sum)