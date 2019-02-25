name_str = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
count_kim=0
count_lee=0
count_jeayoung=0

list_list = name_str.split(',')

for i in list_list:
    if i=='이재영':
        count_jeayoung+=1
    if i[0]=='이':
        count_lee+=1
    elif i[0]=='김':
        count_kim+=1

print("김씨:%d명  이씨:%d명"%(count_kim,count_lee))
print("이재영 이름 횟수:%d번"%count_jeayoung)
list_set = set(list_list)
list_list = list(list_set)
list_list.sort()
print(list_list)
