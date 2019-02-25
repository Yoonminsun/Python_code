time_add=0
for time_h in range(24):
    for time_m in range(60):
        if str(time_h).find('3')!=-1:
            time_add+=60
        elif str(time_m).find('3')!=-1:
            time_add+=60
print(time_add)