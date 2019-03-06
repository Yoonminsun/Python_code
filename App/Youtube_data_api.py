from urllib.request import Request,urlopen
from urllib.parse import quote_plus
import json,webbrowser

access_key = 'AIzaSyCGfzKFx8QlyHG2orNJNKgHR6jusqtuI4o'
# 비디오 보기 https://www.youtube.com/watch?v=비디오id&list=재생목록id
# 재생목록 보기 https://www.youtube.com/playlist?list=재생목록id
def get_Request_URL(url):
    req = Request(url)
    try:
        response = urlopen(req)
        if response.getcode() == 200 :
            if __name__ == '__main__':
                print('Url Request Success')
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        return None
def get_search_URL(): # 재생목록,채널은 제외하고 비디오만 가져오도록 함
    print('\n- 검색 기준\n1.기본검색\n2.시간순(최근)\n3.높은 평가순\n4.문자순\n5.조회수\n6.종료')
    input_order = int(input('검색 기준을 선택하세요.'))
    if input_order==1:
        order=''
    elif input_order==2:
        order = 'date'
    elif input_order==3:
        order = 'rating'
    elif input_order==4:
        order = 'title'
    elif input_order==5:
        order = 'viewCount'
    elif input_order==6:
        return 0
    input_search = input('검색어를 입력하세요: ')
    end_point = 'https://www.googleapis.com/youtube/v3/search'
    parameters = '?key=%s'%access_key
    parameters += '&part=snippet'
    parameters += '&maxResults=%d'%50
    parameters += '&type=video'
    parameters += '&q=%s'%quote_plus(input_search)
    if order:
        parameters += '&order=%s'%order
    url = end_point+parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)
def Make_search_jason():
    jsonData = get_search_URL()
    if jsonData==0:
        return 0
    num=0
    if jsonData:
        for prn_data in jsonData['items']:
            search_video_list.append({'index':num%5+1,'title':prn_data['snippet']['title'],'videoId':prn_data['id']['videoId']})
            num+=1
def play_video():
    if Make_search_jason()==0:
        print('유튜브 검색을 종료합니다.')
        return
    start_index=0
    end_index=5
    while True:
        print('\n동영상 검색 결과')
        for index in range(start_index,end_index):
            try:
                if search_video_list[index]:
                    print('%d>> %s'%(search_video_list[index]['index'],search_video_list[index]['title']))
            except:
                pass
        choice = int(input('\n1.영상 선택 재생\n2.다음 목록 검색\n3.이전 목록 검색\n4.종료\n메뉴 선택:'))
        if choice==1:
            choice_video = int(input('재생할 영상의 번호를 입력하세요: '))
            videoID =  search_video_list[start_index+choice_video-1]['videoId']
            break
        elif choice==2:
            start_index+=5
            end_index+=5
            if len(search_video_list)<=start_index:
                print('\n더 이상 다음 목록이 없습니다.\n')
                start_index-=5
                end_index-=5
                continue
        elif choice==3:
            start_index-=5
            end_index-=5
            if start_index<0:
                print('\n더 이상 이전 목록이 없습니다.\n')
                start_index+=5
                end_index+=5
                continue
        elif choice==4:
            print('유튜브 검색을 종료합니다.')
            return
        else:
            print('\n없는 메뉴 입니다.')
            continue
    end_point = 'https://www.youtube.com/'
    parameters = 'watch?v=%s'%videoID
    url = end_point+parameters
    webbrowser.open(url)
def play_music(input_search):
    music_jason=[]
    end_point = 'https://www.googleapis.com/youtube/v3/search'
    parameters = '?key=%s' % access_key
    parameters += '&part=snippet'
    parameters += '&maxResults=%d' %1
    parameters += '&type=video'
    parameters += '&q=%s' % quote_plus(input_search)
    url = end_point+parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        music_jason =  json.loads(retData)
        url = 'https://www.youtube.com/watch?v=%s'%music_jason['items'][0]['id']['videoId']
        webbrowser.open(url)
search_video_list = []
if __name__ == '__main__':
    # play_video()
    play_music('옥탑방 엔플라잉')
    # Make_search_jason()
