import numpy as np
import cv2
import math

# 좌표사이의 거리 계산 함수 작성
def calc_dist(list1,list2):
    a = list2[0] - list1[0]
    b = list2[1] - list1[1]
    return math.sqrt((a*a)+(b*b))

# Grayscale 형태로 이미지 read
card = cv2.imread('card.png',cv2.IMREAD_GRAYSCALE)
card_4 = cv2.imread('4_card.png')
card_4_gray = cv2.cvtColor(card_4,cv2.COLOR_BGR2GRAY)
cv2.imshow("find",card)

# 적절한 임계값 속성을 찾아 이진화 함
# theta에는 각 임계값, th_~ 에는 각 이진화된 이미지
theta, th_card_4= cv2.threshold(card_4_gray,150,255,cv2.THRESH_BINARY)

# 템플릿 매칭
# TM_CCOEFF 방법은 minMaxLoc 시 max_loc이 왼쪽 상단좌표
# 왼쪽상단에서 템플릿 이미지 shape 만큼 더한 것이 오른쪽 하단 좌표가 됨
w,h = card.shape
res = cv2.matchTemplate(card_4_gray,card,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
left_top = max_loc
right_bottm = (left_top[0]+h, left_top[1]+w)

# 거리계산을 위해 템플릿 매칭된 부분의 두 좌표를 리스트 형태로 변환
tv_lt = list(left_top)
tv_rb = list(right_bottm)

# 바깥의 경계선만 검출
contour, hier = cv2.findContours(th_card_4,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# 각 바깥 경계선이 검출된 부분의 좌표들과
# 템플릿 매칭된 부분의 왼쪽상단, 오른쪽하단의 좌표 사이의 거리를 계산하여
# 총 거리 합이 가장 작은 index의 경계선이 매칭된 부분이라 판단하고
# 해당 인덱스 경계선만 선을 그어줄 것임
vector_distance = []
contour_list=[]

# 경계선 마다 가지고있는 좌표 갯수가 달라 총합이 갯수에 비례할 수 있으므로
# 가장 작은 좌표의 갯수만큼만 거리를 구한다
min_count = [len(contour[i]) for i in range(len(contour))]
min_count = min(min_count)

for num in range(len(contour)):
    dist_sum = 0
    contour_list=[]
    for ct in range(min_count):
        contour_list.append(contour[num][ct][0])
    for i in contour_list:
        dist = calc_dist(tv_lt,i) + calc_dist(tv_rb,i)
        dist_sum += dist
    vector_distance.append(dist_sum)

# 거리 총 합이 가장 작은 인덱스 경계선만 draw
match_index = np.argmin(vector_distance)
cv2.drawContours(card_4,[contour[match_index]],-1,(0,255,0),3)

cv2.imshow("found_result",card_4)

cv2.waitKey(0)
cv2.destroyAllWindows()


