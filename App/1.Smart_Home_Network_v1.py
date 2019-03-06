import Weather_Realtime_Info_for_student
import Air_Pollution_Info
import Bus_stop_info
import Youtube_data_api
import Genie_music_crawling_re
import threading,time,ctypes,json
g_Radiator = False
g_Air_Conditioner = False
g_Balcony_Windows = False
g_Humidifier = False
g_Dehumidifier = False
g_AI_Mode = False
g_Smul_Mode=False

temperature=0
humidity=0
json_list_weather=[]
json_list_air=[]
json_weather = Weather_Realtime_Info_for_student
json_air = Air_Pollution_Info
json_Bus = Bus_stop_info
play_Youtube = Youtube_data_api
sidoName = '동구'

def g_value_false():
    global g_Radiator,g_AI_Mode,g_Air_Conditioner,g_Balcony_Windows,g_Humidifier,g_Dehumidifier
    g_Radiator=True
    g_Air_Conditioner=True
    g_Humidifier=True
    g_Dehumidifier=True
    control_temperature('R')
    control_temperature('A')
    control_humidity('H')
    control_humidity('D')
    g_Balcony_Windows = False
    g_AI_Mode = False
def terminate_ai_mode(ai_scheduler):
    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_scheduler.ident),exc)
    if res == 0:
        raise ValueError('nonexistent thread id')
    elif res>1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident,None)
        raise SystemError('PyhreadState_SetAsyncExc failed')
def print_main_menu():
    print('1. 기상정보 조회')
    print('2. 장비상태 확인')
    print('3. 장비제어')
    print('4. 스마트모드')
    print('5. TV 실행')
    print('6. 시뮬레이션 모드')
    print('7. 프로그램 종료')
def print_device_status(device_name, device_status):
    print('%s 상태: '%device_name,end='')
    if device_status == True:print('작동')
    else: print('정지')
def check_device_status():
    print_device_status('난방기',g_Radiator) # 기온 5도 이하,10도 이상
    print_device_status('에어컨',g_Air_Conditioner)# 기온 30도 이상, 18도 이하
    print_device_status('가습기',g_Humidifier) # 습도 40~60% 유지
    print_device_status('제습기',g_Dehumidifier)
    print_device_status('발코니(베란다) 창문',g_Balcony_Windows) # 비,미세먼지,난방기,에어컨
def print_device_menu():
    print('\n상태 변경할 기기를 선택하세요.')
    print('1. 난방기')
    print('2. 에어컨')
    print('3. 가습기')
    print('4. 제습기')
    print('5. 발코니(베란다) 창문')
def temperature_room():
    for data in json_list_weather:
        if data['category'] == 'T1H':
            return int(data['fcstValue'])
def temperature_change_up():
    global temperature,g_AI_Mode,g_Radiator
    while True:
        if g_Radiator == False:
            break
        else:
            time.sleep(2)
            # temperature = int(temperature)
            if g_Radiator==True:
                temperature+=1
            if g_AI_Mode==True:
                changed_status()
def temperature_change_down():
    global temperature,g_AI_Mode,g_Air_Conditioner
    while True:
        if g_Air_Conditioner == False:
            break
        else:
            time.sleep(1800)
            # temperature = int(temperature)
            if g_Air_Conditioner==True:
                temperature -= 1
            if g_AI_Mode==True:
                changed_status()
def control_temperature(RorA):
    global g_Radiator,g_Air_Conditioner
    if RorA=='R':
        g_Radiator = not g_Radiator
        g_Radiator_scheduler = threading.Thread(target=temperature_change_up)
        if g_Radiator==True:
            g_Radiator_scheduler.daemon=True
            g_Radiator_scheduler.start()
        else:
            while g_Radiator_scheduler.is_alive():
                try:
                    terminate_ai_mode(g_Radiator_scheduler)
                except:
                    pass
    elif RorA=='A':
        g_Air_Conditioner = not g_Air_Conditioner
        g_Air_Conditioner_scheduler = threading.Thread(target=temperature_change_down)
        if g_Air_Conditioner ==True:
            g_Air_Conditioner_scheduler .daemon=True
            g_Air_Conditioner_scheduler .start()
        else:
            while g_Air_Conditioner_scheduler.is_alive():
                try:
                    terminate_ai_mode(g_Air_Conditioner_scheduler )
                except:
                    pass
def humidity_room():
    for data in json_list_weather:
        if data['category'] == 'REH':
            return int(data['fcstValue'])
def humidity_change_up():
    global humidity, g_AI_Mode,g_Humidifier
    while True:
        if g_Humidifier == False:
            break
        else:
            time.sleep(1800)
            if g_Humidifier==True:
                humidity += 1
            if g_AI_Mode == True:
                changed_status()
def humidity_change_down():
    global humidity, g_AI_Mode,g_Dehumidifier
    while True:
        if g_Humidifier == False:
            break
        else:
            time.sleep(1800)
            if g_Dehumidifier==True:
                humidity -= 1
            if g_AI_Mode == True:
                changed_status()
def control_humidity(HorD):
    global g_Humidifier, g_Dehumidifier
    if HorD == 'H':
        g_Humidifier = not g_Humidifier
        g_Humidifier_scheduler = threading.Thread(target=humidity_change_up)
        if g_Humidifier == True:
            g_Humidifier_scheduler.daemon = True
            g_Humidifier_scheduler.start()
        else:
            while g_Humidifier_scheduler.is_alive():
                try:
                    terminate_ai_mode(g_Humidifier_scheduler)
                except:
                    pass
    elif HorD == 'D':
        g_Dehumidifier = not g_Dehumidifier
        g_Dehumidifier_scheduler = threading.Thread(target=humidity_change_down)
        if g_Dehumidifier == True:
            g_Dehumidifier_scheduler.daemon = True
            g_Dehumidifier_scheduler.start()
        else:
            while g_Dehumidifier_scheduler.is_alive():
                try:
                    terminate_ai_mode(g_Dehumidifier_scheduler)
                except:
                    pass
def control_device():
    global g_Radiator,g_Balcony_Windows,g_Humidifier,g_Air_Conditioner
    check_device_status()
    print_device_menu()
    menu_num = int(input('번호를 입력하세요: '))
    print()
    if menu_num ==1: control_temperature('R')
    elif menu_num ==2: control_temperature('A')
    elif menu_num ==3: control_humidity('H')
    elif menu_num ==4: control_humidity('D')
    elif menu_num ==5: g_Balcony_Windows = not g_Balcony_Windows
    check_device_status()
    if g_AI_Mode==True:
        changed_status()
def get_realtime_weather_info():
    global json_list_weather,json_list_air
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(3600)
            weather_time = json_weather.get_Realtime_Weather_Info()
            json_list_weather = json_weather.Make_Weather_Json(weather_time)
            json_weather.Make_Weather_CSV()
            json_list_air = json_air.Make_Air_json_csv()
            json_air.Make_Air_json_csv()
            changed_status()
def smart_mode():
    global g_AI_Mode
    print('1. 인공지능 모드 조회')
    print('2. 인공지능 모드 상태 변경')
    if g_Smul_Mode==False:
        print('3. 실시간 기상정보 Update')
    menu_num = int(input('메뉴를 선택하세요: '))
    if menu_num==1:
        print('현재 인공지능 모드:',end='')
        if g_AI_Mode == True: print('작동\n')
        else: print('중지\n')
    elif menu_num==2:
        ai_scheduler = threading.Thread(target=get_realtime_weather_info)
        g_AI_Mode = not g_AI_Mode
        print('현재 인공지능 모드:',end='')
        if g_AI_Mode == True:
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print('인공지능 모드 작동\n')
            changed_status()
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode(ai_scheduler)
                except:
                    pass
            print('인공지능 모드 정지\n')
    elif menu_num==3:
        get_weather_air_info()
def changed_status(): # 기준에 따라 기기 상태 바꾸는 함수
    last_time = json_list_weather[0]['fcstTime']
    global g_Radiator,g_Balcony_Windows,g_Air_Conditioner,temperature,humidity
    if temperature<=5 and g_Radiator==False:
        control_temperature('R')
        print('기온이 5℃ 이하 이므로 난방기를 작동합니다.')
    elif temperature >= 10 and g_Radiator == True:  # 기온 10도 이상, 난방기 작동시 정지
        control_temperature('R')
        print('기온이 10℃도 이상이므로 난방기를 정지합니다.')
    if temperature>= 30 and g_Air_Conditioner == False:  # 기온 30도 이상, 에어컨 정지시 작동
        control_temperature('A')
        print('기온이 30℃ 이상이므로 에어컨을 작동합니다.')
    elif temperature <= 18 and g_Air_Conditioner == True:  # 기온 18도 이하, 에어컨 작동시 정지
        control_temperature('A')
        print('기온이 18℃ 이하이므로 에어컨을 정지합니다.')
    if humidity<30 and g_Humidifier==False:
        control_humidity('H')
        print('습도가 30% 미만이므로 가습기를 작동합니다.')
    elif humidity>50 and g_Humidifier==True:
        control_humidity('H')
        print('습도가 50% 초과이므로 가습기를 정지합니다.')
    if humidity>60 and g_Dehumidifier==False:
        control_humidity('D')
        print('습도가 60% 초과이므로 제습기를 작동합니다.')
    elif humidity<40 and g_Dehumidifier==True:
        control_humidity('D')
        print('습도가 40% 미만이므로 제습기를 정지합니다.')
    for result in json_list_weather:
        if g_Balcony_Windows==True:
            if result['fcstTime'] == last_time and result['category'] == 'RN1': # 창문
                if int(result['fcstValue'])>0: # 비 예보가 있으면 창문 닫음
                    g_Balcony_Windows=False
                    print('곧 비 예보가 있으므로 창문을 닫습니다.')
                elif g_Radiator==True: # 난방기가 켜진 경우 창문 닫음
                    g_Balcony_Windows=False
                    print('난방기가 작동 중 이므로 창문을 닫습니다.')
                elif g_Air_Conditioner==True: # 에어컨이 켜진 경우 창문 닫음
                    g_Balcony_Windows=False
                    print('에어컨이 작동 중 이므로 창문을 닫습니다.')
            elif 81<=int(json_list_air[0]['pm10Value']) <= 150 or 51<=int(json_list_air[0]['pm25Value']) <= 100:
                g_Balcony_Windows = False
                print('미세먼지 등급이 "나쁨" 이므로 창문을 닫습니다.')
            elif int(json_list_air[0]['pm10Value']) >= 151 or int(json_list_air[0]['pm25Value']) >= 101:
                g_Balcony_Windows = False
                print('미세먼지 등급이 "매우나쁨" 이므로 창문을 닫습니다.')
def TV_on():
    print('1. 버스 도착정보 조회\n2. 유튜브 검색/재생\n3. 음악 차트 조회')
    menu = int(input('실행할 메뉴를 선택하세요: '))
    if menu==1:
        json_Bus.Print_arrive_time()
    elif menu==2:
        play_Youtube.play_video()
    elif menu==3:
        music_list = Genie_music_crawling_re.Print_rank()
        menu_music = int(input('\n1.유튜브로 음악 재생\n2.종료\n메뉴를 선택하세요: '))
        if menu_music==1:
            choice_music = int(input('재생할 음악 순위를 선택하세요: '))
            rank,title,artist = music_list[choice_music].split(',')
            play_Youtube.play_music('%s %s'%(title,artist))
            return
        elif menu_music==2:
            return
def Simulation_mode():
    global json_list_weather,json_list_air,temperature,humidity,g_Smul_Mode
    g_Smul_Mode=True
    json_list_weather=[]
    json_list_air=[]
    with open('./시뮬레이션_초단기예보조회.json','r',encoding='UTF8') as weatherfile:
        json_object = json.load(weatherfile)
    json_string = json.dumps(json_object)
    json_list_weather = json.loads(json_string)
    with open('./시뮬레이션_미세먼지농도조회.json','r',encoding='UTF8') as airfile:
        json_object2 = json.load(airfile)
    json_string2 = json.dumps(json_object2)
    json_list_air = json.loads(json_string2)
    temperature = temperature_room()
    humidity = humidity_room()
def Simulation_save_CSV():
    global json_list_weather,json_list_air
    csv_Data_weather = ['baseDate,baseTime,category,fcstDate,fcstTime,fcstValue,nx,ny']
    csv_Data_air = ['도시명,dataTime,미세먼지농도,초미세먼지농도']
    for prn_data in json_list_weather:
        csv_Data_weather.append(str(prn_data.get('baseDate'))+','+str(prn_data.get('baseTime'))+','+
                                    prn_data.get('category')+','+str(prn_data.get('fcstDate'))+','+
                                    str(prn_data.get('fcstTime'))+','+str(prn_data.get('fcstValue'))+','+
                                    str(prn_data.get('nx'))+','+str(prn_data.get('ny')))
    f = open('./시뮬레이션_초단기예보조회.csv','w')
    f.write('\n'.join(csv_Data_weather))
    f.close()

    for prn_data in json_list_air:
        csv_Data_air.append(prn_data['cityName'] + ',' + prn_data['dataTime']
                              + ',' + prn_data['pm10Value'] + ',' + prn_data['pm25Value'])
    f = open('./시뮬레이션_미세먼지농도조회.csv','w')
    f.write('\n'.join(csv_Data_air))
    f.close()
def get_weather_air_info(): #시뮬->기본으로 돌아갈때 다시 정보 받아오는 함수
    global json_list_weather,json_list_air,temperature,humidity
    json_weather.get_Realtime_Weather_Info()
    json_list_weather = json_weather.json_weather_result
    json_list_air = json_air.Make_Air_json_csv()
    temperature = temperature_room()
    humidity = humidity_room()
def print_weather_air_info():
    global json_list_air,json_list_weather,temperature,humidity
    last_time = json_list_weather[0]['fcstTime']
    for data in json_list_weather:
        if data['fcstTime'] == last_time:
            if data['category'] == 'T1H':
                print('- 외부 기온:%s(℃)'%data['fcstValue'])
            elif data['category'] == 'REH':
                print('- 외부 습도:%s(%%)'%data['fcstValue'])
            elif data['category'] =='RN1':
                print('- 강수량:%s(mm/h)'%data['fcstValue'])
    pm10 = int(json_list_air[0]['pm10Value'])
    pm25 = int(json_list_air[0]['pm25Value'])
    print('- 미세먼지 농도:%d(㎍/㎥\n- 초미세먼지 농도:%d(㎍/㎥)' % (pm10, pm25))
    if pm10 <= 30 or pm25 <= 15:
        print('- 미세먼지 예보 등급: 좋음')
    elif pm10 <= 80 or pm25 <= 50:
        print('- 미세먼지 예보 등급: 보통')
    elif pm10 <= 150 or pm25 <= 100:
        print('- 미세먼지 예보 등급: 나쁨')
    elif pm10 >= 151 or pm25 >= 101:
        print('- 미세먼지 예보 등급: 매우나쁨')
    print('- 내부 기온:%s(℃)'%temperature)
    print('- 내부 습도:%s(%%)\n'%humidity)
print('<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>')
get_weather_air_info()
while True:
    if not g_Smul_Mode:
        print_main_menu()
        try:
            menu_num = int(input('메뉴를 선택하세요: '))
            print()
        except:
            pass
        if menu_num==1:
            print_weather_air_info()
        elif menu_num==2:
            check_device_status()
        elif menu_num==3:
            control_device()
        elif menu_num==4:
            smart_mode()
        elif menu_num==5:
            TV_on()
        elif menu_num==6:
            g_value_false()
            Simulation_mode()
        elif menu_num==7:
            break
    else:
        print('\n<< 시뮬레이션 모드 작동 중 >>')
        menu_num = int(input('1. 장비제어\n2. 스마트모드변경\n3. 시뮬레이션 기상정보 조회\n4. 시뮬레이션 종료\n메뉴를 선택하세요: '))
        print()
        if menu_num==1:
            control_device()
        elif menu_num==2:
            smart_mode()
        elif menu_num==3:
            print_weather_air_info()
        elif menu_num==4:
            g_value_false()
            Simulation_save_CSV()
            get_weather_air_info()
            g_Smul_Mode = False