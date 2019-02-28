import urllib.request
from bs4 import BeautifulSoup
import re,os,time


dir_num=1
dir_name = './naver_ranking1'
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
soup = str(soup)
tags_list = ['순위,영화명,변동폭']
p=re.compile(r'title="(.+)">\1</a>\n</div>\n</td>\n.+\n.+\n<td class="ac">.+alt="([a-z]+)".+\n<td class=.+(\d+)')
match_list = p.findall(soup)

def search_file_list(dir_name):
    try:
        file_list = os.listdir(dir_name)
        return len(file_list)
    except Exception:
        pass
def search_dir_list(dir_name):
    global dir_num
    dir_name = './naver_ranking%d' %dir_num
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        return dir_name
    else:
        file_len = search_file_list(dir_name)
        if file_len<3:
            return dir_name
        else:
            dir_num+=1
            dir_name = search_dir_list(dir_name)
            return dir_name


for index in range(len(match_list)):
    if match_list[index][0].find(',')!=-1:
        title = '"'+match_list[index][0]+'"'
    else:
        title = match_list[index][0]
    if match_list[index][1]=='up':
        change = '+'+match_list[index][2]
    elif match_list[index][1]=='down':
        change = '-'+match_list[index][2]
    else:
        change = match_list[index][2]
    tags_list.append(str(index + 1) + ',' + title + ',' + change)

dir_name = search_dir_list(dir_name)
file_name = '/%s'%time.strftime('%Y-%m-%d_%H%M%S',time.localtime())

f = open('%s%s.csv'%(dir_name,file_name),'w')
f.write('\n'.join(tags_list))
f.close()