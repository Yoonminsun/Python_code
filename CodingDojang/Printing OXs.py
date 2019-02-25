n = int(input('n 입력: '))
for i in range(n,0,-1):
    print('O'*(i-1),'X'*(n-i+1),sep='')