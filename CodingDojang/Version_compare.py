ver1 = input('입력: ').split('.')
ver2 = input('입력: ').split('.')
for index in range(3):
    if int(ver1[index])>int(ver2[index]):
        print('.'.join(ver1),'>','.'.join(ver2))
        break
    elif int(ver1[index])<int(ver2[index]):
        print('.'.join(ver1), '<', '.'.join(ver2))
        break
    elif index==2:
        print('.'.join(ver1), '=', '.'.join(ver2))

