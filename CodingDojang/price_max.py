ori_price=10
ori_perform=150
plus_price=3
plus_perform_list = [30,70,15,40,65]
plus_perform_list.sort(reverse=True) # 성능 높은 것 부터 정렬
p_to_p = ori_perform/ori_price
for plus in plus_perform_list:
    if p_to_p<(ori_perform+plus)//(ori_price+3):
        ori_price+=3
        ori_perform+=plus
        p_to_p = ori_perform//ori_price
print(p_to_p)
