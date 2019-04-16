# 사용 모델 : LogisticRegression
# 고정 변수 항목 : review text에 쓰인 단어들, 단어 빈도
# 분석 목표(예측값) : 리뷰가 긍정인지 부정인지 판별

# 종속 변수가 0 또는 1 인 분류 예측 문제이므로 로지스틱 회귀분석 모델 사용
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

with open('pre_movie_review.pickle','rb') as file:
    label, voca, feature = pickle.load(file)

# train_test_split을 사용하여 학습데이터셋, 테스트데이터셋 분리 (default: train 75%, test 25%)
train_data, test_data, train_label, test_label = train_test_split(feature,label)

classifier = LogisticRegression()
classifier.fit(train_data,train_label)

print('학습 정확도: %.2f %%'%(classifier.score(train_data,train_label)*100))
print('테스트 정확도: %.2f %%\n'%(classifier.score(test_data,test_label)*100))

# 각 피처에 대한 편회귀계수( 계수별 영향도 )
weight = classifier.coef_[0, :]
pair = []
for index,value in enumerate(weight):
    pair.append((abs(value), voca[index]))
pair.sort(key=lambda x:x[0], reverse=True)
for pr in pair[:20]:
    print('영향도: %4.4f => 단어: %s'%pr)

