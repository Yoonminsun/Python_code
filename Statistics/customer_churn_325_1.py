# 목적: 로지스틱 모델을 통해 이탈 고객 예측하기
import numpy as np
import pandas as pd
import statsmodels.api as sm
from itertools import combinations
import operator
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv',sep=',',header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]
churn['churn01'] = np.where (churn['churn'] == 'True.',1.,0. )
churn['intl_plan01'] = np.where(churn['intl_plan'] == 'yes',1.,0.)
churn['vmail_plan01'] = np.where(churn['vmail_plan'] == 'yes',1.,0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']

churn_list = [data for data in churn['churn01']]

independent_variables_list = ['account_length','intl_plan01','vmail_plan01','vmail_message','day_mins',
                              'day_calls','day_charge','eve_mins','eve_calls','eve_charge',
                              'night_mins','night_calls','night_charge','intl_mins','intl_calls','intl_charge',
                              'custserv_calls']

# Fit a logistic regression model
dependent_variable = churn['churn01']
match_dic={}
for num in range(1,18):
    combi_list = list(combinations(independent_variables_list, num))
    for tup in combi_list:
        list_str = ' '.join(tup)
        print(list_str)
        independent_variables = churn[list(tup)]
        independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
        logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
        new_observations_with_constant = sm.add_constant(independent_variables, prepend=True)
        y_predicted = logit_model.predict(new_observations_with_constant)
        y_predicted_rounded = [round(score, 0) for score in y_predicted]
        match_count = 0
        for index in range(len(churn_list)):
            if churn_list[index] == y_predicted_rounded[index]:
                match_count += 1
        print('Match Count =',match_count)
        print('정답률 = %.2f%%'%((match_count/len(churn_list))*100))
        match_dic[list_str] = '%.2f %%' % ((match_count / len(churn_list)) * 100)

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
print(match_dic)
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합:",match_dic[0])
end = datetime.fromtimestamp(time.time())
print(start)
print(end)
print(end-start)



