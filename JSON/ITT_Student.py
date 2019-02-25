import json

my_path = './ITT_Student.json'
choice_menu = 0
json_big_data=[]
input_name=''
input_age=''
input_address=''
input_course_num=0
input_code=''
input_course_name=''
input_teacher=''
input_start=''
input_end=''
course_yn=''
def open_json():
    with open(my_path, encoding='UTF8')as json_file: json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)
    return json_big_data
def write_json(json_big_data):
    with open(my_path,'w',encoding='utf8') as outfile:
        readable_result = json.dumps(json_big_data,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(readable_result)
        print('ITT_Student.json SAVED')
def print_menu(num):
    if num==1: # 메인
        print('\n<< json기반 주소록 관리 프로그램 >>')
        print('1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료')
        choice_menu = int(input('메뉴를 선택하세요: '))
        return choice_menu
    elif num==2: # 조회
        print('\n1. 전체 학생정보 조회')
        print('검색 조건 선택')
        print('2. ID 검색\n3. 이름 검색\n4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강중인 학생\n8. 현재 수강 중인 강의명\n9. 현재 수강 강사\n0. 이전 메뉴')
        choice_menu = int(input('메뉴를 선택하세요: '))
        return choice_menu
    elif num==3: # 수정
        print('\n1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전 메뉴')
        choice_menu = int(input("메뉴 번호를 입력하세요: "))
        return choice_menu
    elif num==4: # 수정
        print('\n1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소')
        choice_menu = int(input("메뉴 번호를 입력하세요: "))
        return  choice_menu
    elif num==5: # 삭제
        print('삭제할 유형을 선택하세요.\n1. 전체 삭제\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전메뉴')
        choice_menu = int(input('메뉴 번호를 선택하세요: '))
        return choice_menu
def search_info(choice_condition):
    found_count=0
    found=[]
    if choice_condition==1:
        for index in range(len(json_big_data)):
            print_info(index)
        return
    elif choice_condition==0:
        return
    if choice_condition!=7:
        in_search = input('검색어를 입력하세요: ')
    for index in range(len(json_big_data)):
        in_total = json_big_data[index]['total_course_info']
        if choice_condition==2: # student_ID
            if json_big_data[index]['student_ID']==in_search:
                found.append(index)
                break
        elif choice_condition==3: # student_name
            if json_big_data[index]['student_name'].find(in_search)!=-1:
                found.append(index)
                found_count += 1
        elif choice_condition==4: # student_age
            if json_big_data[index]['student_age'] == int(in_search):
                found.append(index)
                found_count += 1
        elif choice_condition==5: # address
            if json_big_data[index]['address'].find(in_search)!=-1:
                found.append(index)
                found_count += 1
        elif choice_condition == 6:  # num_of_course_learned
            if in_total['num_of_course_learned'] == int(in_search):
                found.append(index)
                found_count += 1
        elif choice_condition == 7:  # len(learning_course_info)
            if in_total['learning_course_info']:
                found.append(index)
                found_count += 1
        for in_learn in in_total['learning_course_info']:
            if choice_condition==8: # course_name
                if in_learn['course_name'].find(in_search)!=-1:
                    found.append(index)
                    found_count += 1
                    break
            elif choice_condition==9: # teacher
                if in_learn['teacher'] == in_search:
                    found.append(index)
                    found_count += 1
                    break
    if found_count>1:
        print('복수 개의 결과가 검색되었습니다.\n----- 요약 결과 -----')
        for student in found:
            print('>> 학생 ID: %s, 학생 이름: %s'%(json_big_data[student]['student_ID'],json_big_data[student]['student_name']))
    else:
        try:
            print_info(found[0])
        except IndexError:
            print('검색결과 없음')
def print_info(index):
    if file_found(index)==0:
        return
    print('\n* 학생 ID:', json_big_data[index]['student_ID'])
    print('* 이름:', json_big_data[index]['student_name'])
    print('* 나이:', json_big_data[index]['student_age'])
    print('* 주소:', json_big_data[index]['address'])
    print('* 수강 정보')
    in_total = json_big_data[index]['total_course_info']
    print(' + 과거 수강 횟수: ', in_total['num_of_course_learned'])
    for in_learn in in_total['learning_course_info']:
        print('  강의 코드:', in_learn['course_code'])
        print('  강의명:', in_learn['course_name'])
        print('  강사:', in_learn['teacher'])
        print('  개강일:', in_learn['open_date'])
        print('  종료 일:', in_learn['close_date'])
def search_ID_index(in_search):
    for index in range(len(json_big_data)):
            if json_big_data[index]['student_ID']==in_search:
                return index
def modify_info(in_search):
    index = search_ID_index(in_search)
    print_info(index)
    choice_menu = print_menu(3)
    in_total = json_big_data[index]['total_course_info']
    if choice_menu!=0 and choice_menu!=5:
        in_modify = input("변경할 값을 입력하세요: ")
        if choice_menu==1: # 학생 이름
            json_big_data[index]['student_name'] = in_modify
        elif choice_menu==2: # 나이
            json_big_data[index]['student_age'] = int(in_modify)
        elif choice_menu==3: # 주소
            json_big_data[index]['address'] = in_modify
        elif choice_menu==4: # 과거 수강 횟수
            in_total['num_of_course_learned'] = int(in_modify)
    else:
        if choice_menu==0:
            return
        elif choice_menu==5:
            if len(in_total['learning_course_info']) <1:
                print('현재 수강중인 강의가 없습니다.')
                return
            choice_menu = print_menu(4)
            if choice_menu!=0:
                if len(in_total['learning_course_info'])>1:
                    choice_modify = input('여러 항목이 있습니다. 변경할 강의의 코드를 입력하세요: ')
                    in_modify =  input('변경할 값을 입력하세요: ')
                    for in_learn in in_total['learning_course_info']:
                        if in_learn['course_code'] == choice_modify:
                            if choice_menu==1:
                                   in_learn['course_code'] = in_modify
                            elif choice_menu==2:
                                    in_learn['course_name'] = in_modify
                            elif choice_menu==3:
                                    in_learn['teacher'] = in_modify
                            elif choice_menu==4:
                                    in_learn['open_date'] = in_modify
                            elif choice_menu==5:
                                    in_learn['close_date'] = in_modify
                else:
                    in_modify = input("변경할 값을 입력하세요: ")
                    if choice_menu == 1:  # 강의 코드
                        in_total['learning_course_info'][0]['course_code'] = in_modify
                    elif choice_menu == 2:  # 강의명
                        in_total['learning_course_info'][0]['course_name'] = in_modify
                    elif choice_menu == 3:  # 강사
                        in_total['learning_course_info'][0]['teacher'] = in_modify
                    elif choice_menu == 4:  # 개강일
                        in_total['learning_course_info'][0]['open_date'] = in_modify
                    elif choice_menu == 5:  # 종료일
                        in_total['learning_course_info'][0]['close_date'] = in_modify
            else:
                return
    print_info(index)
def remove_info(in_search):
    index = search_ID_index(in_search)
    if file_found(index)==0:
        return
    choice_menu = print_menu(5)
    if choice_menu==1:
        del json_big_data[index]
        print('삭제 되었습니다')
    elif choice_menu==2:
        in_total = json_big_data[index]['total_course_info']
        if len(in_total['learning_course_info']) < 1:
            print('현재 수강 중인 과목이 없습니다.')
        else:
            for in_learn in in_total['learning_course_info']:
                    print('- 강의코드:', in_learn['course_code'])
                    print('  강의명:', in_learn['course_name'])
                    print('  강사:', in_learn['teacher'])
                    print('  개강일:', in_learn['open_date'])
                    print('  종료일:', in_learn['close_date'])
            in_course_code = input('삭제할 과목 코드를 입력하세요: ')
            for course_index in range(len(in_total['learning_course_info'])):
                if in_total['learning_course_info'][course_index]['course_code'] == in_course_code:
                    del in_total['learning_course_info'][course_index]
                    print('삭제 되었습니다.')
    elif choice_menu==3:
        return
def file_found(index):
    try:
        json_big_data[index]
    except TypeError:
        print('검색결과 없음.')
        return 0
while True:
    try:
        json_big_data = open_json()
    except FileNotFoundError:
        choice_menu = int(input('파일이 없습니다.\n1. 신규 생성\n2. 파일 경로 입력\n메뉴 선택: '))
        if choice_menu==1:
            id_plus = 1
            choice_menu=1
            break
        elif choice_menu==2:
            # test path = D:\Python_local_repository\02 Data Science\json dir
            my_path = input('파일 경로 입력: ') + '\ITT_Student.json'
            json_big_data = open_json()
            id_plus = int(json_big_data[len(json_big_data) - 1]['student_ID'][-3:]) + 1
            choice_menu = print_menu(1)
            break
    else:
        id_plus = int(json_big_data[len(json_big_data) - 1]['student_ID'][-3:]) + 1
        choice_menu = print_menu(1)
        break
while True:
    if choice_menu==1: # 입력
        input_name = input('이름 (예: 홍길동): ')
        input_age = int(input('나이 (예: 29): '))
        input_address = input('주소 (예: 대구광역시 동구 아양로 135): ')
        input_course_num = int(input('과거 수강 횟수 (예: 1): '))
        input_ID = 'ITT{0:03d}'.format(id_plus)
        id_plus+=1
        index = len(json_big_data)
        json_big_data.append({"address":input_address, "student_ID":input_ID,"student_age":input_age,"student_name":input_name})
        json_big_data[index]['total_course_info'] = {'learning_course_info': [],'num_of_course_learned':input_course_num}
        json_big_data
        course_yn = input('현재 수강 과목이 있습니까?(예: y/n): ')
        count=0
        while course_yn=='y':
            input_code = input('강의코드 (예: IB171106, OB0104 ..): ')
            input_course_name = input('강의명 (예: IOT 빅데이터 실무반): ')
            input_teacher = input('강사 (예: 이현구): ')
            input_start = input('개강일 (예: 2017-11-06): ')
            input_end = input('종료일 (예: 2018-09-05): ')
            json_big_data[index]["total_course_info"]["learning_course_info"].append\
                ({"close_date":input_end,"course_code":input_code,"course_name":input_course_name,"open_date":input_start,"teacher":input_teacher})
            course_yn = input('현재 수강 과목이 더 있습니까?(예: y/n): ')
            count+=1
        choice_menu = print_menu(1)
    elif choice_menu==2: # 조회
        print('아래 메뉴를 선택하세요.')
        choice_condition = print_menu(2)
        search_info(choice_condition)
        choice_menu = print_menu(1)
    elif choice_menu==3: # 수정
        in_search = input("수정할 학생ID를 입력하세요: ")
        modify_info(in_search)
        choice_menu = print_menu(1)
    elif choice_menu==4: # 삭제
        in_search = input("삭제할 학생ID를 입력하세요: ")
        remove_info(in_search)
        choice_menu = print_menu(1)
    elif choice_menu==5: # 종료
        write_json(json_big_data)
        print('학생 정보 관리 프로그램을 종료합니다.')
        exit()