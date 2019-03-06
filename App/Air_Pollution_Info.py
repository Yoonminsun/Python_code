from urllib.request import Request,urlopen
from urllib.parse import quote_plus
import datetime
import json
import time

access_key='oQSz2oLeE2%2FyKkC5Bvap%2ByKJ7NjXePjiinT9FimEL9PX9o0aEMHImBYj3NVIi9ArzQx4avj62hoXKqANLvj%2FcA%3D%3D'

def get_Request_URL(url):
    req = Request(url)
    try:
        response = urlopen(req)
        if response.getcode() == 200 :
            if __name__ == '__main__':
                print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s'%(datetime.datetime.now(),url))
        return None
def get_Air_URL():
    global json_air_result,csv_air_result
    csv_air_result=[]
    json_air_result=[]
    end_point = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst'
    parameters = '?_returnType=json&ServiceKey='+access_key
    parameters+= '&sidoName=%s'%quote_plus(sidoName)
    parameters+= '&searchCondition='+'HOUR'
    parameters+= '&numOfRows=100'
    url = end_point + parameters
    retData = get_Request_URL(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData)
def Make_Air_json_csv():
    jsonData = get_Air_URL()
    yyyymmdd = time.strftime("%Y%m%d")
    day_time = time.strftime("%H%M")
    if (jsonData['list']):
        for prn_data in jsonData['list']:
            csv_air_result.append(prn_data['cityName'] + ',' + prn_data['dataTime']
                                  + ',' + prn_data['pm10Value'] + ',' + prn_data['pm25Value'])
            if prn_data['cityName'] == cityName:
                json_air_result.append({'cityName':prn_data['cityName'],'dataTime':prn_data['dataTime'],'pm10Value':prn_data['pm10Value'],
                                        'pm25Value':prn_data['pm25Value']})
        f = open('동구_실시간_미세먼지농도조회_%s%s.csv' % (yyyymmdd, day_time), 'w')
        f.write('\n'.join(csv_air_result))
        f.close()
    return json_air_result

json_air_result=[]
csv_air_result=['도시명,dataTime,미세먼지농도,초미세먼지농도']
sidoName = '대구'
cityName = '동구'

if __name__ == '__main__':
    Make_Air_json_csv()

