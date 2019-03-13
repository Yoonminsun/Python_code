import MySQLdb
from xlrd import open_workbook
from xlwt import Workbook

input_file_1 = 'Basic_Student_Info.xlsx'
input_file_2 = 'Student_Language.xlsx'

con = MySQLdb.connect(host='localhost',port=3306,db='erd_students',user='open_source',passwd='1111',charset='utf8mb4')
c = con.cursor()

workbook_info = open_workbook(input_file_1)
workbook_lang = open_workbook(input_file_2)
worksheet_info = workbook_info.sheet_by_name('Sheet1')
worksheet_lang = workbook_lang.sheet_by_name('Sheet1')

delete_table_1 = "delete from basic_student_info"
delete_table_2 = "delete from student_language"
c.execute(delete_table_1)
c.execute(delete_table_2)
con.commit()

rows=()
id_num=0

def DB_Insert():
    global rows,id_num
    data=[]
    for row in range(1,worksheet_info.nrows):
        for each in worksheet_info.row(row):
            data.append(each.value)
        c.execute("INSERT INTO Basic_Student_Info VALUES ('%s','%s','%s',%s,'%s');"
                  %(data[0],data[1],data[2],data[3],data[4]))
        data=[]
    for row in range(1,worksheet_lang.nrows):
        for each in worksheet_lang.row(row):
            data.append(each.value)
        c.execute("INSERT INTO Student_Language VALUES ('%s','%s','%s','%s');"
                  %(data[0],data[1],data[2],data[3]))
        data=[]
    con.commit()
    c.execute("SELECT * FROM Basic_Student_Info b LEFT JOIN Student_Language s USING(Student_ID) ORDER BY Student_ID")
    rows = c.fetchall()
    id_num = int(rows[len(rows) - 1][0][3:]) + 1
def Print_Main_input():
    print('[ 메인 메뉴 ]')
    print('1. 요약 정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료')
    menu = int(input('메뉴 입력: '))
    return menu
def Print_Search_input():
    print('< 조회 서브 메뉴 >')
    print('1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위 메뉴')
    menu = int(input('메뉴 입력: '))
    return menu
def Print_Search_each_input():
    print('< 검색 조건 >')
    print('1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 학습 기간\n7. 컴퓨터 언어 레벨\n8. 상위메뉴')
    menu = int(input('메뉴 입력: '))
    return menu
def Count_Student_Info():
    list_20=[]
    list_30=[]
    list_40=[]
    c.execute("SELECT * FROM Basic_student_info")
    total = len(c.fetchall())
    c.execute("SELECT * FROM Basic_student_info WHERE Sex='남'")
    total_male = len(c.fetchall())
    c.execute("SELECT * FROM Basic_student_info WHERE Sex='여'")
    total_female = len(c.fetchall())
    c.execute("SELECT * FROM Basic_student_info WHERE Major='컴퓨터 공학' OR (Major LIKE '%통계%' OR Major='컴퓨터공학')")
    total_major = len(c.fetchall())
    c.execute("SELECT Student_ID FROM Student_Language")
    lang = c.fetchall()
    lang = set(lang)
    total_lang = len(lang)
    c.execute("SELECT Student_ID FROM Student_Language WHERE Level='상'")
    lang = c.fetchall()
    lang = set(lang)
    total_high = len(lang)
    c.execute("SELECT * FROM Student_Language WHERE Name='파이썬'")
    total_python = len(c.fetchall())
    c.execute("SELECT * FROM Basic_student_info WHERE Age <30 AND Age>19")
    age = c.fetchall()
    total_20 = len(age)
    for data in age:
        list_20.append('%s:%s'%(data[1],data[3]))
    c.execute("SELECT * FROM Basic_student_info WHERE Age <40 AND Age>29")
    age = c.fetchall()
    total_30 = len(age)
    for data in age:
        list_30.append('%s:%s' % (data[1], data[3]))
    c.execute("SELECT * FROM Basic_student_info WHERE Age <50 AND Age>39")
    age = c.fetchall()
    total_40 = len(age)
    for data in age:
        list_40.append('%s:%s' % (data[1], data[3]))

    list_info = [total,total_male,total_female,total_major,total_lang,total_high,total_python,
                 total_20,total_30,total_40]
    return list_info,list_20,list_30,list_40
def Print_Info(list_info,list_20,list_30,list_40):
    print('< 요약 정보 >')
    print('* 전체 학생수: %d명'%list_info[0])
    print('* 성별')
    print('  - 남학생: %d명 (%.1f%%)'%(list_info[1],(list_info[1]/list_info[0])*100))
    print('  - 여학생: %d명 (%.1f%%)'%(list_info[2],(list_info[2]/list_info[0])*100))
    print('* 전공 여부')
    print('  - 전공자(컴퓨터 공학, 통계): %d명 (%.1f%%)'%(list_info[3],(list_info[3]/list_info[0])*100))
    print('  - 프로그래밍 언어 경험자: %d명 (%.1f%%)'%(list_info[4],(list_info[4]/list_info[0])*100))
    print('  - 프로그래밍 언어 상급자: %d명 (%.1f%%)'%(list_info[5],(list_info[5]/list_info[0])*100))
    print('  - 파이썬 경험자: %d명 (%.1f%%)'%(list_info[6],(list_info[6]/list_info[0])*100))
    print('* 연령대')
    print('  - 20대: %d명 (%.1f%%) '%(list_info[7],(list_info[7]/list_info[0])*100),end='')
    print(list_20)
    print('  - 30대: %d명 (%.1f%%) ' % (list_info[8], (list_info[8] / list_info[0]) * 100), end='')
    print(list_30)
    print('  - 40대: %d명 (%.1f%%) ' % (list_info[9], (list_info[9] / list_info[0]) * 100), end='')
    print(list_40)
def Input_Student():
    global rows,id_num
    lang_name=''
    level=''
    period=''
    print('< 신규 학생 정보 입력 >')
    name = input('- 이름을 입력하세요(종료는 Enter 입력): ')
    if not name: return
    id = 'ITT{0:03d}'.format(id_num)
    id_num+=1
    sex = input('- 성별을 입력하세요: ')
    age = input('- 나이를 입력하세요: ')
    major = input('- 전공을 입력하세요: ')
    c.execute("INSERT INTO Basic_Student_Info VALUES ('%s','%s','%s',%s,'%s');"
              % (id, name, sex, age, major))
    print('- 사용 가능한 컴퓨터 언어를 입력하세요.')
    while True:
        lang_name = input('  > 언어 이름(종료는 Enter 입력):')
        if not lang_name: break
        level = input('  > 수준(상,중,하): ')
        period = input('  > 학습 기간(년/개월 단위): ')
        c.execute("INSERT INTO Student_Language VALUES ('%s','%s','%s','%s')"
                  %(id,lang_name,level,period))
    con.commit()
    c.execute("SELECT * FROM Basic_Student_Info b LEFT JOIN Student_Language s USING(Student_ID) ORDER BY Student_ID")
    rows = c.fetchall()
def Search_Student_Each(menu):
    search_str = input('검색어를 입력하세요: ')
    if menu==1:
        c.execute("SELECT * FROM Basic_student_info WHERE Student_ID='%s'"%search_str)
        info = c.fetchall()
    elif menu==2:
        c.execute("SELECT * FROM Basic_student_info WHERE Name LIKE '%{0}%'".format(search_str))
        info = c.fetchall()
    elif menu==3:
        c.execute("SELECT * FROM Basic_student_info WHERE Age=%s" % search_str)
        info = c.fetchall()
    elif menu==4:
        c.execute("SELECT * FROM Basic_student_info WHERE Major LIKE '%{0}%'".format(search_str))
        info = c.fetchall()
    elif menu==5:
        c.execute("SELECT Student_ID FROM Student_Language WHERE Name='%s'"%search_str)
        lang=c.fetchall()
    elif menu==6:
        c.execute("SELECT Student_ID FROM Student_Language WHERE Period='%s'" % search_str)
        lang = c.fetchall()
        lang = set(lang)
        lang = tuple(lang)
    elif menu==7:
        c.execute("SELECT Student_ID FROM Student_Language WHERE Level='%s'" % search_str)
        lang = c.fetchall()
        lang = set(lang)
        lang = tuple(lang)
    if menu<5:
        if len(info)>1:
            for data in info:
                print('- %s (%s, %s, %s)'%(data[0],data[1],data[2],data[3]))
        elif len(info)==1:
            Search_Student_Print(info[0][0])
        else:
            print('검색결과가 없습니다.')
    else:
        if len(lang)>1:
            for data in lang:
                c.execute("SELECT * FROM Basic_Student_info WHERE Student_ID='%s'" %data[0])
                info = c.fetchall()[0]
                print('- %s (%s, %s, %s)'%(info[0],info[1],info[2],info[3]))
        elif len(lang)==1:
            Search_Student_Print(lang[0][0])
        else:
            print('검색결과가 없습니다.')
def Search_Student_Print(ID):
    c.execute("SELECT * FROM Basic_student_info WHERE Student_ID='%s'"%ID)
    info = c.fetchall()[0]
    c.execute("SELECT * FROM Student_Language WHERE Student_ID='%s'"%ID)
    lang = c.fetchall()

    print('\n* %s (%s)'%(info[0],info[1]))
    print('- 성별: %s'%info[2])
    print('- 나이: %d'%info[3])
    print('- 전공: %s'%info[4])
    if not lang: print('- 사용 가능한 컴퓨터 언어: 없음')
    else:
        print('- 사용 가능한 컴퓨터 언어')
        for data in lang:
            print('  > %s (학습기간: %s, Level: %s)'%(data[1],data[3],data[2]))
def Update_Student():
    global rows
    update_student_ID = input('수정할 학생의 ID를 입력하세요: ')
    index = 5
    c.execute("SELECT * FROM Basic_student_info WHERE Student_ID='%s'" % update_student_ID)
    info = c.fetchall()[0]
    c.execute("SELECT * FROM Student_Language WHERE Student_ID='%s'"%update_student_ID)
    lang = c.fetchall()
    print('1. 이름: %s'%info[1])
    print('2. 성별: %s'%info[2])
    print('3. 나이: %d'%info[3])
    print('4. 전공: %s'%info[4])
    if not lang:
        print('5. 사용가능한 컴퓨터 언어: 없음 (수정시 추가)')
    else:
        print('사용 가능한 컴퓨터 언어')
        for data in lang:
            print('%d. %s' % (index, data[1]))
            print('%d. Level: %s'%((index+1),data[2]))
            print('%d. 학습기간: %s'%((index+2),data[3]))
            index+=3

    choice = int(input('수정할 항목의 번호를 입력하세요: '))
    if not choice==5 and lang:
        modify = input('수정할 값을 입력하세요: ')

    if choice==1:
        c.execute("UPDATE Basic_student_info SET Name='%s' WHERE Student_ID='%s'"%(modify,info[0]))
    elif choice==2:
        c.execute("UPDATE Basic_student_info SET Sex='%s' WHERE Student_ID='%s'" % (modify, info[0]))
    elif choice==3:
        c.execute("UPDATE Basic_student_info SET Age=%s WHERE Student_ID='%s'" % (int(modify), info[0]))
    elif choice==4:
        c.execute("UPDATE Basic_student_info SET Major='%s' WHERE Student_ID='%s'" % (modify, info[0]))
    elif choice==5 and not lang:
        print('- 사용 가능한 컴퓨터 언어를 입력하세요.')
        while True:
            lang_name = input('  > 언어 이름(종료는 Enter 입력):')
            if not lang_name: break
            level = input('  > 수준(상,중,하): ')
            period = input('  > 학습 기간(년/개월 단위): ')
            c.execute("INSERT INTO Student_Language VALUES ('%s','%s','%s','%s')"
                      % (info[0], lang_name, level, period))
    elif (choice-5)%3==0:
        c.execute("UPDATE Student_Language SET Name='%s' WHERE Student_ID='%s' AND Name='%s'"
                  %(modify,info[0],lang[(choice-5)//3][1]))
    elif (choice-6)%3==0:
        c.execute("UPDATE Student_Language SET Level='%s' WHERE Student_ID='%s' AND Name='%s'"
                  % (modify, info[0], lang[(choice - 5) // 3][1]))
    elif (choice-7)%3==0:
        c.execute("UPDATE Student_Language SET Period='%s' WHERE Student_ID='%s' AND Name='%s'"
                  % (modify, info[0], lang[(choice - 5) // 3][1]))
    con.commit()
    c.execute(
        "SELECT * FROM Basic_Student_Info b LEFT JOIN Student_Language s USING(Student_ID) ORDER BY Student_ID")
    rows = c.fetchall()
def Delete_Student():
    global rows
    delete_ID = input('삭제할 ID를 입력하세요: ')
    c.execute("DELETE FROM Basic_student_info WHERE Student_ID='%s'" %delete_ID)
    c.execute("DELETE FROM Student_Language WHERE Student_ID='%s'" % delete_ID)
    print('삭제되었습니다.')
    con.commit()
    c.execute("SELECT * FROM Basic_Student_Info b LEFT JOIN Student_Language s USING(Student_ID) ORDER BY Student_ID")
    rows = c.fetchall()
DB_Insert()
menu = Print_Main_input()
while True:
    if menu==1:
        list_info, list_20, list_30, list_40 = Count_Student_Info()
        Print_Info(list_info, list_20, list_30, list_40)
        menu = Print_Main_input()
    elif menu==2:
        Input_Student()
        menu = Print_Main_input()
    elif menu==3:
        search_menu = Print_Search_input()
        if search_menu==1:
            each_menu = Print_Search_each_input()
            if each_menu==8:
                pass
            else:
                Search_Student_Each(each_menu)
        elif search_menu==2:
            print('< 전체 학생 데이터 >')
            c.execute("SELECT Student_ID FROM Basic_student_info")
            ID_list = c.fetchall()
            for id in ID_list:
                Search_Student_Print(id)
        elif search_menu==3:
            menu = Print_Main_input()
    elif menu==4:
        Update_Student()
        menu = Print_Main_input()
    elif menu==5:
        Delete_Student()
        menu = Print_Main_input()
    elif menu==6:
        print('학생 정보 분석 완료!')
        exit()