import pandas as pd
from sklearn import svm, metrics, model_selection
# 데이터로드
csv = pd.read_csv('iris.csv')
# 고정변수와 종속변수 나누기
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]
# 머신 러닝 모델 생성
clf = svm.SVC(gamma='auto')
# 크로스 밸리데이션 하기 (학습데이터, 테스트데이터 번갈아 나눠줌)
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean()) ## 0.98