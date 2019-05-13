from tkinter import *
from tkinter import ttk

temp=[]
operation={'r':['-','+','*','/'],'b':['AC',0,'=']}

## 버튼 눌렸을때 이벤트 함수
# 숫자와 연산의 경우를 구분
# 연산 및 삭제,리턴 입력시 텍스트 지워지도록 함
def button_pressed(value):
    global temp
    # 숫자
    if not value in operation['r'] and not value in operation['b'] or value==0:
        if temp and type(temp[len(temp)-1])==int:
            temp[len(temp)-1] = int(str(temp[len(temp)-1])+str(value))
        else:
            temp.append(value if type(value) == int else str(value))
        number_entry.insert("end",value)

    # 연산
    elif value in operation['r'] and number_entry.get()!='':
        temp.append(value if type(value) == int else str(value))
        number_entry.delete(0,'end')

    # = , AC
    else:
        if value=='AC':
            number_entry.delete(0,'end')
            temp=[]
        elif value=='=' and temp:
            number_entry.delete(0, 'end')
            result = operation_calc(temp)
            number_entry.insert(0,result)

## 연산 함수
# 입력받은 값들을 담은 clist에서 연산과 숫자를 구분하며 결과 리턴
def operation_calc(clist):
    result=clist[0]
    opt=''
    for i in range(1,len(clist)):
        i=clist[i]
        if type(i)==int:
            if opt=='-':
                result = result-i
            elif opt=='+':
                result = result + i
            elif opt=='/':
                result = result / i
            else:
                result = result * i
        else:
            opt=i
    return result

## 키보드로 입력 받기 위한 함수
# 숫자인 경우 int로 아니면 char 타입 그대로 인자 전달
# 쉬프트키 같은 다른 키들은 인식되지 않게 예외처리로 pass 해줌
def key_input(value):

    num = '0123456789'
    ope = '-+*/'
    try:
        if value.char in num:
            button_pressed(int(value.char))
        elif value.char in ope:
            button_pressed(value.char)
        elif value.keysym == "Return":
            button_pressed('=')
        elif value.keysym == 'BackSpace':
            button_pressed('AC')
    except Exception:
        pass


## 타이틀과 크기, 키보드 입력을 위한 bind
root = Tk()
root.title("Calculator_Yoon")
root.geometry("320x150")
root.bind('<Key>',key_input)

entry_value = StringVar(root,value='')

number_entry = ttk.Entry(root,textvariable=entry_value,width=20)
number_entry.grid(row=0,columnspan=3)

## GUI 구성
# 4*4 모양의 GUI
# 좌측 상단부터 3*3은 1~9, 우측과 하단 끝 부분은 나머지 연산 및 0 으로 생각하여
# for 문을 이용해 버튼 생성 (ttk.Button 구문을 여러번 쓸 필요 없도록)
# globals() 를 이용하여 반복되는 변수를 각각 생성하지 않고 for문이 돌면서 자동으로 생성되어 버튼값이 할당되도록 함
for i in range(4):
    for j in range(4):
        index = j + (3 * (i - 1))
        if j==3:
            btxt=operation['r'][i]
        elif i==0:
            btxt=operation['b'][j]
        else:
            btxt = index + 1

        globals()['num{}'.format(index)] = ttk.Button(root, text="%s"%btxt,width=10
                                                      ,command=lambda btxt=btxt: button_pressed(btxt))
        globals()['num{}'.format(index)].grid(row=4-i, column=j)

root.mainloop()

