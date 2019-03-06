import urllib.request
from bs4 import BeautifulSoup
import re,time

html = urllib.request.urlopen('https://genie.co.kr/chart/top200')
soup = BeautifulSoup(html,'html.parser')
soup = str(soup)
music_rank_list = ['순위,제목,가수']
title_list=[]
artist_list=[]

def Make_rank_list_CSV():
    global title_list,artist_list
    yyyymmdd = time.strftime("%Y%m%d")
    day_time = time.strftime("%H%M")

    p = re.compile('class="select-check" title="(.+)" .+')
    title_list = p.findall(soup)
    p = re.compile(r'(?!>).</a>\n.+class="artist ellipsis".+>(.+)</a>')
    artist_list = p.findall(soup)

    for index in range(len(title_list)):
        title = title_list[index]
        artist = artist_list[index]
        if title.find(',')!=-1:
            title = '"'+title+'"'
        if artist.find(',')!=-1:
            artist = '"'+artist+'"'
        music_rank_list.append('%d,%s,%s'%(index+1,title,artist))
    f = open('지니차트_TOP50_%s%s.csv'%(yyyymmdd,day_time),'w')
    f.write('\n'.join(music_rank_list))
    f.close()

def Print_rank():
    global music_rank_list
    Make_rank_list_CSV()
    print('\n< 음악 Top 50 > _ 지니뮤직')
    for index in range(len(title_list)):
        print('%d>> %s _ %s'%(index+1,title_list[index],artist_list[index]))
    return music_rank_list

