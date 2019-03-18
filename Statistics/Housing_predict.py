import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from itertools import combinations
import operator

print("< Housing Predict >")
house = pd.read_csv('Housing.csv',sep=',',header=0)
columns_change = ['driveway01','recroom01','fullbase01','gashw01','airco01','prefarea01']
columns_ori = ['driveway','recroom','fullbase','gashw','airco','prefarea']

for index in range(len(columns_ori)):
    house[columns_change[index]] = np.where(house[columns_ori[index]] == 'yes', 1, 0)

dependent_variable = house['price']
independent_variables_list = ['lotsize','bedrooms','bathrms','stories','driveway01','recroom01','fullbase01','gashw01','airco01',
                'garagepl','prefarea01']

delta_plus = lambda x,y:x+x*y
delta_minus = lambda x,y:x-x*y
match_dic_5 = {}
match_dic_10 = {}
match_dic_20 = {}

for num in range(1,12):
    combi_list = list(combinations(independent_variables_list,num))
    for tup in combi_list:
        my_formula = 'price ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=house).fit()
        # print(lm.summary())
        independent_variables = house[list(tup)]
        y_predicted = lm.predict(independent_variables)
        match_count_5=0
        match_count_10=0
        match_count_20=0
        for index in range(len(y_predicted)):
            ### 5%
            if delta_minus(house['price'][index], 0.05) < y_predicted[index] < delta_plus(house['price'][index], 0.05):
                match_count_5 += 1
            ### 10%
            if delta_minus(house['price'][index], 0.1) < y_predicted[index] < delta_plus(house['price'][index], 0.1):
                match_count_10 += 1
            ### 20%
            if delta_minus(house['price'][index],0.2)<y_predicted[index]<delta_plus(house['price'][index],0.2):
                match_count_20+=1
        print('\n>> '+my_formula.replace('price ~ ',''))
        print('>> 5% match count=', match_count_5)
        print('>> 10% match count=', match_count_10)
        print('>> 20% match count=',match_count_20)
        print('>> 5%% 정답률: %.2f %%' % (match_count_5 / len(y_predicted) * 100))
        print('>> 10%% 정답률: %.2f %%' % (match_count_10 / len(y_predicted) * 100))
        print('>> 20%% 정답률: %.2f %%'%(match_count_20/len(y_predicted)*100))
        match_dic_5['%s' % my_formula.replace('price ~ ', '')] = match_count_5 / len(y_predicted) * 100
        match_dic_10['%s' % my_formula.replace('price ~ ', '')] = match_count_10 / len(y_predicted) * 100
        match_dic_20['%s'%my_formula.replace('price ~ ','')] = match_count_20/len(y_predicted)*100

### 최댓값 찾기
match_dic_5 = sorted(match_dic_5.items(),key=operator.itemgetter(1),reverse=True)
match_dic_10 = sorted(match_dic_10.items(),key=operator.itemgetter(1),reverse=True)
match_dic_20 = sorted(match_dic_20.items(),key=operator.itemgetter(1),reverse=True)
print(match_dic_5)
print(match_dic_10)
print(match_dic_20)
print('총 조합 갯수 = %d'%(len(match_dic_5)))
print('5%% MAX 조합: %s >> %.2f %%'%(match_dic_5[0][0],match_dic_5[0][1]))
print('10%% MAX 조합: %s >> %.2f %%'%(match_dic_10[0][0],match_dic_10[0][1]))
print('20%% MAX 조합: %s >> %.2f %%'%(match_dic_20[0][0],match_dic_20[0][1]))
