in_str = input("입력: ")

for i in range(2,len(in_str),2):
    if ord(in_str[i-1])>47 and ord(in_str[i-1])<58:
        in_str = in_str[:i-1]+'*'+in_str[i:]
print(in_str)

# 짝수번째 문자가 숫자인지 확인하기위해 ord함수로 아스키코드값을 체크함
# 0~9는 아스키코드값으로 48~57
# 짝수번째이므로 2씩 증가하며 for문을 돌리고, 인덱스는 0부터 이므로 -1 하여 인덱싱