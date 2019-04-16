# 데이터 출처 : http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220982297456&redirect=Dlog&widgetTypeCall=true

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

positive = '1\t' # 긍정 리뷰의 헤더는 1
negative = '0\t' # 부정 리뷰의 헤더는 0
labels=[]
document=[]

with open('movie_review.txt','r',encoding='utf8') as file:
    for line in file:
        if line.startswith(positive): # 긍정인 경우
           labels.append(1)
           # 1  abcdefg.... => line[len(positive):] : abcdefg....
           document.append(line[len(positive):])
        elif line.startswith(negative): # 부정인 경우
            labels.append(0)
            document.append(line[len(negative):])

# CountVectorizer 클래스 : 문서를 단어 단위로 쪼개서 각 단어가 몇 번 나왔는지 세어 단어 카운팅 피처를 만든다
count_vector = CountVectorizer()
# word_count : (데이터,특성)\t카운트\n ...
word_count = count_vector.fit_transform(document)
# voca: 사용된 피처 단어 목록
voca = count_vector.get_feature_names()

# 위의 피처를 단어 빈도 피처로 변환
tf_trans = TfidfTransformer(use_idf=False).fit(word_count)
feature = tf_trans.transform(word_count)

with open('pre_movie_review.pickle','wb') as file:
    pickle.dump((labels,voca,feature),file)