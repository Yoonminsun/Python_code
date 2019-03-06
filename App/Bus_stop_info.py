from urllib.request import Request,urlopen
from urllib.parse import quote_plus
import datetime
import json

Codejson=[]
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

def get_Bus_stop_ID():
    global stopName
    stopName = input('정류장 이름을 입력하세요: ')
    end_point = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getSttnNoList?_type=json'
    parameters = '&serviceKey='+access_key
    parameters+= '&cityCode=%s'%get_cityCode()
    parameters+= '&nodeNm=%s'%quote_plus(stopName)
    url = end_point + parameters
    retData = get_Request_URL(url)
    if(retData == None):
        return None
    else:
        stop_json = json.loads(retData)
        if stop_json['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
            if type(stop_json['response']['body']['items']['item'])==dict:
                return stop_json['response']['body']['items']['item']['nodeid']
            else:
                print('여러개의 버스 정류장이 검색되었습니다.')
                for data in stop_json['response']['body']['items']['item']:
                    print('- %s'%data['nodenm'])
                input_stopnm = input('선택할 정류장이름을 입력하세요: ')
                for data in stop_json['response']['body']['items']['item']:
                    if data['nodenm'] == input_stopnm:
                        return data['nodeid']

def get_cityCode():
    global Codejson
    cityCode_url = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getCtyCodeList?_type=json'
    parameters = '&ServiceKey=%s'%access_key
    cityCode_url = cityCode_url+parameters
    CodeData = get_Request_URL(cityCode_url)
    if (CodeData == None):
        return None
    else:
        Codejson = json.loads(CodeData)
        if Codejson['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
            for prn_data in Codejson['response']['body']['items']['item']:
                if prn_data['cityname']==cityName:
                    return prn_data['citycode']

def get_arrive_info_URL():
    stopID = get_Bus_stop_ID()
    end_point = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList?_type=json'
    parameters = '&serviceKey=%s'%access_key
    parameters += '&cityCode=%s'%get_cityCode()
    parameters += '&nodeId=%s'%stopID
    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_arrive_info_json():
    jsonData = get_arrive_info_URL()
    if not jsonData['response']['body']['items']['item']:
        print('버스 운행 시간이 아닙니다.')
        return
    if jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
        for prn_data in jsonData['response']['body']['items']['item']:
            json_arrive_result.append({'routeid':prn_data['routeid'],'routeno':prn_data['routeno'],
                                       'arrprevstationcnt':prn_data['arrprevstationcnt'],
                                       'vehicletp':prn_data['vehicletp'],'arrtime':prn_data['arrtime']})
    return json_arrive_result

# def Make_arrive_info_CSV():
#     jsonData = get_arrive_info_URL()
#     if jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
#         for prn_data in jsonData['response']['body']['items']['item']:
#             csv_arrive_result.append(prn_data['routeid']+','+str(prn_data['routeno'])+','+
#                                        str(prn_data['arrprevstationcnt'])+','+prn_data['vehicletp']+','+str(prn_data['arrtime']))
#     return csv_arrive_result
def Print_arrive_time():
    Make_arrive_info_json()
    global json_arrive_result
    print('%s 정류장에서 운행하는 버스 목록' % stopName)
    for stop in json_arrive_result: print(stop['routeno'],end='  ')
    print()
    busRouteno = int(input('\n조회할 버스 번호를 입력하세요: '))
    for bus_data in json_arrive_result:
        if bus_data['routeno'] == busRouteno:
            print('%s 버스\n- 도착 예상 시간:%d분%d초' % (busRouteno,bus_data['arrtime']//60,bus_data['arrtime']%60))
            print('- 남은 정류장 수:%s\n- 차량 유형:%s'%(bus_data['arrprevstationcnt'],bus_data['vehicletp']))
            print()
            return
    print('%d번 버스의 도착 예정 정보가 없습니다.\n'%busRouteno)

cityName = '대구광역시'
stopName = ''
busStoplist = []
json_arrive_result=[]
if __name__ == '__main__':
    Print_arrive_time()