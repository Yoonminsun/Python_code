from xml.etree.ElementTree import parse,Element,SubElement,dump,ElementTree

tree = parse('students_info_2.xml')
student_list = tree.getroot()
choice_menu=0
tag_students = student_list.findall('student')
count_students = len(student_list)
class Count:
    count_male = 0
    count_female = 0
    count_major = 0
    count_programming = 0
    count_level = 0
    count_python = 0
    age_20 = 0
    age_20_list = []
    age_30 = 0
    age_30_list = []
    age_40 = 0
    age_40_list = []
    id_plus = 0
    def count_information(self):
        self.count_male = 0
        self.count_female = 0
        self.count_major = 0
        self.count_programming = 0
        self.count_level = 0
        self.count_python = 0
        self.age_20 = 0
        self.age_20_list = []
        self.age_30 = 0
        self.age_30_list = []
        self.age_40 = 0
        self.age_40_list = []
        for student in range(count_students):
            if tag_students[student].get('sex')=='남':
                self.count_male+=1
            elif tag_students[student].get('sex')=='여':
                self.count_female+=1
            if tag_students[student].findtext('major')=='컴퓨터 공학':
                self.count_major+=1
            elif tag_students[student].findtext('major').find('통계')!=-1:
                self.count_major+=1
            if tag_students[student].find('practicable_computer_languages').find('language'):
                self.count_programming+=1
            if tag_students[student].find('practicable_computer_languages').find('language'):
                for lang in tag_students[student].find('practicable_computer_languages').findall('language'):
                    if lang.get('level')=='상':
                        self.count_level+=1
                    if lang.get('name')=='파이썬':
                        self.count_python+=1
            age = int(tag_students[student].findtext('age'))
            if age>=20 and age<30:
                self.age_20+=1
                self.age_20_list.append('%s %s'%(tag_students[student].get('name'),tag_students[student].findtext('age')))
            elif age>=30 and age<40:
                self.age_30+=1
                self.age_30_list.append('%s %s' % (tag_students[student].get('name'), tag_students[student].findtext('age')))
            elif age>=40 and age<50:
                self.age_40+=1
                self.age_40_list.append('%s %s' % (tag_students[student].get('name'), tag_students[student].findtext('age')))
            student+=1
count = Count()
count.id_plus = int(tag_students[len(student_list)-1].get('ID')[-3:])+1
def print_menu(menu): # 메뉴 출력 함수
    choice=0
    if menu==1:
        print('\n[ 메인 메뉴 ]')
        print('1. 요약정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료')
    elif menu==2:
        print('\n< 조회 서브 메뉴 >')
        print('1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위 메뉴')
    elif menu==3:
        print('\n< 검색 조건 >')
        print('1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 학습 기간\n7. 컴퓨터 언어 레벨\n8. 상위 메뉴')
    choice = int(input('메뉴 입력: '))
    return choice
def print_student(index): # 학생 정보 출력 함수
    tag_students = student_list.findall('student')
    print('* %s (%s)' %(tag_students[index].get('name'),tag_students[index].get('ID')))
    print(' - 성별: %s' % tag_students[index].get('sex'))
    print(' - 나이: %s' % tag_students[index].findtext('age'))
    print(' - 전공: %s' % tag_students[index].findtext('major'))
    print(' - 사용 가능한 컴퓨터 언어:', end=' ')
    if tag_students[index].find('practicable_computer_languages').find('language'):
        for lang in tag_students[index].find('practicable_computer_languages').findall('language'):
            print('\n > %s (학습기간: %s, Level:%s)' % (lang.get('name'), lang.find('period').get('value'),lang.get('level')),end='')
        print('\n')
    else:
        print('없음\n')
def print_age_list(age_list): # 나이대 출력 함수
    print('[ ',end='')
    for list in age_list:
        in_name,in_age = list.split(' ')
        print('%s:%s '%(in_name,in_age),end='')
    print(']')
def search_student(in_search,choice_menu_condition): # 학생 조회 함수
    tag_students = student_list.findall('student')
    count_students = len(student_list)
    found = []
    found_count=0
    for student in range(count_students):
        if choice_menu_condition==1:
            if tag_students[student].get('ID') == in_search:
                found.append(student)
                print_student(found[0])
                return
        elif choice_menu_condition==2: # 중복 가능
            if tag_students[student].get('name').find(in_search)!=-1:
                found.append("%s %s"%(str(student),tag_students[student].get('name')))
                found_count += 1
        elif choice_menu_condition==3: # 중복 가능
            if tag_students[student].findtext('age') == in_search:
                found.append("%s %s"%(str(student),tag_students[student].findtext('age')))
                found_count += 1
        elif choice_menu_condition==4: # 중복 가능
            if tag_students[student].findtext('major') == in_search:
                found.append("%s %s"%(str(student),tag_students[student].findtext('major')))
                found_count += 1
        elif choice_menu_condition==5: # 중복 가능
            if tag_students[student].find('practicable_computer_languages').find('language'):
                for lang in tag_students[student].find('practicable_computer_languages').findall('language'):
                    if lang.get('name')==in_search:
                        found.append("%s %s"%(str(student),lang.get('name')))
                        found_count += 1
        elif choice_menu_condition==6: # 중복 가능
            if tag_students[student].find('practicable_computer_languages').find('language'):
                for lang in tag_students[student].find('practicable_computer_languages').findall('language'):
                    if lang.find('period').get('value') == in_search:
                        found.append("%s %s"%(str(student),lang.find('period').get('value')))
                        found_count += 1
                        break
        elif choice_menu_condition==7: # 중복 가능
            if tag_students[student].find('practicable_computer_languages').find('language'):
                for lang in tag_students[student].find('practicable_computer_languages').findall('language'):
                    if lang.get('level') == in_search:
                        found.append("%s %s"%(str(student),lang.get('level')))
                        found_count += 1
                        break
    print("\n- %s에 대한 검색 결과"%in_search)
    if found_count==0: print('없음')
    for index in range(found_count):
        found_index, found_value = found[index].split(' ')
        found_index = int(found_index)
        print("%s (%s, %s, %s)"%(tag_students[found_index].get('ID'),tag_students[found_index].get('name'),
                                 tag_students[found_index].findtext('age'),tag_students[found_index].get('sex')))
def insert_student(): # 학생 입력 함수
    print('< 신규 학생 정보 입력 >')
    input_name = input("- 이름을 입력하세요 (종료는 'Enter' 입력): ")
    if input_name=='': return
    input_ID = 'ITT{0:03d}'.format(count.id_plus)
    count.id_plus+=1
    input_sex = input("- 성별을 입력하세요: ")
    input_age = input("- 나이를 입력하세요: ")
    input_major = input("- 전공을 입력하세요: ")
    insert = SubElement(student_list, 'student', attrib={'name':input_name, 'ID':input_ID, 'sex':input_sex})
    practicable = SubElement(insert, 'practicable_computer_languages')
    SubElement(insert, 'age').text = input_age
    SubElement(insert, 'major').text = input_major
    print("- 사용 가능한 컴퓨터 언어를 입력하세요")
    while True:
        input_language_name = input("언어 이름 (종료는 'Enter' 입력): ")
        if input_language_name=='':
            ElementTree(student_list).write('students_info_2.xml',encoding='UTF-8',xml_declaration=True)
            return
        input_period = input('학습 기간(년/개월 단위): ')
        input_level = input('수준(상,중,하): ')
        language = SubElement(practicable, 'language',attrib={'name':input_language_name,'level':input_level})
        SubElement(language,'period',attrib={'value':input_period})
def modify_student(choice_ID): # 학생정보 수정 함수
    index_print=5
    index=0
    tag_students = student_list.findall('student')
    for student in range(count_students):
        if tag_students[student].get('ID') == choice_ID:
            index = student
    print('1. 이름: %s' %tag_students[index].get('name'))
    print('2. 성별: %s' %tag_students[index].get('sex'))
    print('3. 나이: %s' %tag_students[index].findtext('age'))
    print('4. 전공: %s' %tag_students[index].findtext('major'))
    print('  사용 가능한 컴퓨터 언어')
    if tag_students[index].find('practicable_computer_languages').find('language'):
        for lang in tag_students[index].find('practicable_computer_languages').findall('language'):
            print('%d. %s'%(index_print,lang.get('name')))
            print('%d. 학습기간: %s'%(index_print+1,lang.find('period').get('value')))
            print('%d. Level: %s'%(index_print+2,lang.get('level')))
            index_print+=3
    else:
        print('5. 없음 (신규 추가)\n')

    choice_modify = int(input('수정할 항목의 번호를 입력하세요: '))
    if ((choice_modify-5)%3)!=0:
        str_modify = input('수정할 값을 입력하세요: ')
    if choice_modify==1:
        tag_students[index].set('name',str_modify)
    elif choice_modify==2:
        tag_students[index].set('sex', str_modify)
    elif choice_modify==3:
        tag_students[index].find('age').text = str_modify
    elif choice_modify==4:
        tag_students[index].find('major').text = str_modify
    elif ((choice_modify-5)%3)==0:
        if not tag_students[index].find('practicable_computer_languages').find('language'):
            while True:
                input_language_name = input("언어 이름 (종료는 'Enter' 입력): ")
                if input_language_name == '':
                    ElementTree(student_list).write('students_info_2.xml',encoding='UTF-8',xml_declaration=True)
                    print_student(index)
                    return
                input_period = input('학습 기간(년/개월 단위): ')
                input_level = input('수준(상,중,하): ')
                language = SubElement(tag_students[index].find('practicable_computer_languages'),'language')
                language.attrib['name']=input_language_name
                language.attrib['level']=input_level
                SubElement(language, 'period', attrib={'value': input_period})
        else:
            str_modify = input('수정할 값을 입력하세요: ')
            lang = tag_students[index].find('practicable_computer_languages').findall('language')
            lang[(choice_modify-5)//3].set('name',str_modify)
    elif ((choice_modify-6)%3)==0:
        lang = tag_students[index].find('practicable_computer_languages').findall('language')
        lang[(choice_modify - 5)// 3].find('period').set('value', str_modify)
    elif ((choice_modify-7)%3)==0:
        lang = tag_students[index].find('practicable_computer_languages').findall('language')
        lang[(choice_modify-5)//3].set('level',str_modify)
    ElementTree(student_list).write('students_info_2.xml',encoding='UTF-8',xml_declaration=True)
    print_student(index)
def search_ID_index(choice_ID): # ID 기준으로 index를 찾는 함수
    count_students = len(student_list)
    tag_students = student_list.findall('student')
    for student in range(count_students):
        if tag_students[student].get('ID') == choice_ID:
            return student
def remove_student(choice_ID): # 학생 삭제 함수
    student = search_ID_index(choice_ID)
    try:
        tag_remove = tag_students[student]
        student_list.remove(tag_remove)
        ElementTree(student_list).write('students_info_2.xml',encoding='UTF-8',xml_declaration=True)
        print('삭제되었습니다.')
    except TypeError:
        print('없는 ID 입니다.')

choice_menu = print_menu(1)
while True:
    count_students = len(student_list)
    tag_students = student_list.findall('student')
    if choice_menu==1: # 요약 정보
        count.count_information()
        print('<요약 정보>')
        print('* 전체 학생수: %d 명'%count_students)
        print('* 성별')
        print('- 남학생: %d명 (%0.1f%%)'%(count.count_male,(count.count_male/count_students)*100))
        print('- 여학생: %d명 (%0.1f%%)'%(count.count_female,(count.count_female/count_students)*100))
        print('* 전공여부')
        print('- 전공자(컴퓨터 공학, 통계): %d명 (%0.1f%%)'%(count.count_major,(count.count_major/count_students)*100))
        print('- 프로그래밍 언어 경험자: %d명 (%0.1f%%)'%(count.count_programming,(count.count_programming/count_students)*100))
        print('- 프로그래밍 언어 상급자: %d명 (%0.1f%%)'%(count.count_level,(count.count_level/count_students)*100))
        print('- 파이썬 경험자: %d명 (%0.1f%%)'%(count.count_python,(count.count_python/count_students)*100))
        print('* 연령대')
        print('- 20대: %d명 (%0.1f%%)'%(count.age_20,(count.age_20/count_students)*100),end=' ')
        print_age_list(count.age_20_list)
        print('- 30대: %d명 (%0.1f%%)'%(count.age_30,(count.age_30/count_students)*100),end=' ')
        print_age_list(count.age_30_list)
        print('- 40대: %d명 (%0.1f%%)'%(count.age_40,(count.age_40/count_students)*100),end=' ')
        print_age_list(count.age_40_list)
        choice_menu = print_menu(1)
    elif choice_menu==2: # 입력
        insert_student()
        choice_menu = print_menu(1)
    elif choice_menu==3: # 조회
        choice_sub = print_menu(2)
        if choice_sub==1:
            choice_condition = print_menu(3)
            if choice_condition==8:
                pass
            else:
                in_search=input("검색어를 입력하세요: ")
                search_student(in_search, choice_condition)
        elif choice_sub==2:
            count_students = len(student_list)
            for student in range(count_students):
                print_student(student)
        elif choice_sub==3:
            choice_menu = print_menu(1)
    elif choice_menu==4: # 수정
        choice_ID = input("수정할 학생의 ID를 입력하세요: ")
        modify_student(choice_ID)
        choice_menu = print_menu(1)
    elif choice_menu==5: # 삭제
        choice_ID = input("삭제할 학생의 ID를 입력하세요: ")
        remove_student(choice_ID)
        choice_menu = print_menu(1)
    elif choice_menu==6: # 종료
        print('학생 정보 분석 완료!')
        exit()