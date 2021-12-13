from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
from load import vocaLoad

menu = Tk()

fontStyle = tkFont.Font(family="Lucida Grande", size=14, weight="bold")
word_fontStyle = tkFont.Font(family="Lucida Grande", size=11, weight="bold")

word_num = 0
cur_idx = 0

r1 = IntVar()
r2 = IntVar()
r3 = IntVar()
r4 = IntVar()
day_checkval = {}

# 단어 불러오기
all_day_word, all_day_mean, basic_day_word, basic_day_mean, grade800_day_word, grade800_day_mean = vocaLoad()


# 단어 넣기
def insertWord():
    global cur_idx
    cur_idx = 0
    treelist = [("Tom", ""), ("Bani", "")]

    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i], iid=i)


# 키 입력 이벤트
def keyEvent(event):
    global cur_idx

    mean_list = ["하나", "둘"]
    treeview.set(cur_idx, column="two", value=mean_list[cur_idx])
    cur_idx += 1


# 체크박스 모두 선택
def allCheckBoxOn():
    r1.set(1); r2.set(1); r3.set(1)
    for i in range(30):
        day_checkval[f"day{i+1}"].set(1)


# 체크박스 초기화
def allCheckBoxOff():
    r1.set(0); r2.set(0); r3.set(0)
    for i in range(30):
        day_checkval[f"day{i+1}"].set(0)


# 테이블 사이즈 변경 비활성화
def tableResizeBlock(event):
    if treeview.identify_region(event.x, event.y) == "separator":
        return "break"

# Run 윈도우-----------------------------------------------------------------------------------------------
def createRunWindow():
    global treeview

    run = Toplevel(menu)
    run.title("VOCA - RUN")
    run.geometry("700x500")

    # 토익 단어장
    voca_label = Label(run, text=f"토익 단어장(단어 개수 : {word_num})")
    voca_label.grid(row=0, column=0)

    voca_frame = Frame(run, pady=3)
    run.grid_rowconfigure(1, weight=1)
    run.grid_columnconfigure(0, weight=1)

    voca_frame.grid(row=1, column=0, sticky="nsew")

    voca_frame.grid_rowconfigure(0, weight=1)
    voca_frame.grid_columnconfigure(1, weight=1)

    # 스타일(Treeview)
    style = ttk.Style(run)
    style.theme_use("clam")
    style.configure("Treeview", font=word_fontStyle)

    treeview = ttk.Treeview(voca_frame, columns=["one", "two"], displaycolumns=["one", "two"])
    treeview.pack(fill="y", expand=True)

    # 테이블 사이즈 변경 비활성화
    treeview.bind('<Button-1>', tableResizeBlock)

    # 테이블 설정
    treeview.column("#0", width=50)
    treeview.heading("#0", text="Num")

    treeview.column("#1", width=300, anchor="center")
    treeview.heading("one", text="단어", anchor="center")

    treeview.column("#2", width=300, anchor="center")
    treeview.heading("two", text="의미", anchor="center")

    insertWord()


    # RUN 관련 버튼
    runbtn_frame = Frame(run, pady=3)
    runbtn_frame.grid(row=2, column=0)

    runbtn_frame.grid_rowconfigure(0, weight=1)
    runbtn_frame.grid_columnconfigure(1, weight=1)

    shuffle_btn = Button(runbtn_frame, text="단어 다시섞기", font=fontStyle)
    shuffle_btn.pack()

    # 키 입력 이벤트
    run.bind("<space>", keyEvent)


# Run 윈도우 END-----------------------------------------------------------------------------------------------


# Main(Menu 윈도우)-----------------------------------------------------------------------------------------------
def main():
    global day_checkval

    menu.title("VOCA - MENU")
    menu.geometry("830x300")
    menu.resizable(False, False)

    # 옵션1. DAY 선택
    option1 = Label(menu, text='1. DAY 선택(1~30)', font=fontStyle)
    option1.grid(row=0, column=0, sticky='w')

    label1 = Label(menu)
    label1.grid(row=1, column=0)

    day_checkbtn = {}
    for i in range(30):
        day_checkval[f"day{i+1}"] = IntVar()
        day_checkbtn[f"day{i+1}"] = Checkbutton(label1, text=f"DAY{i+1}", variable=day_checkval[f"day{i+1}"]).grid(row=2+int(i//10), column=(i % 10))

    menu.grid_rowconfigure(4, minsize=50)

    # 옵션2. 범위 선택
    option2 = Label(menu, text='2. 범위 선택', font=fontStyle)
    option2.grid(row=5, column=0, sticky='w')

    label2 = Label(menu)
    label2.grid(row=6, column=0, sticky='w')

    range1 = Checkbutton(label2, text="핵심 빈출 단어", variable=r1)
    range2 = Checkbutton(label2, text="토익 기초 단어", variable=r2)
    range3 = Checkbutton(label2, text="800점 완성 단어", variable=r3)
    range4 = Checkbutton(label2, text="900점 완성 단어", variable=r4)

    range1.grid(row=7, column=0)
    range2.grid(row=7, column=1)
    range3.grid(row=7, column=2)
    range4.grid(row=7, column=3)

    menu.grid_rowconfigure(7, minsize=50)

    # MENU 윈도우 버튼 관련
    done_btn = Button(menu, text="선택 완료", font=fontStyle, command=createRunWindow)
    all_select_btn = Button(menu, text="모두 선택", font=fontStyle, command=allCheckBoxOn)
    reset_btn = Button(menu, text="초기화", font=fontStyle, command=allCheckBoxOff)

    done_btn.grid(row=8, column=0, sticky='ew')
    all_select_btn.grid(row=8, column=1, sticky='ew')
    reset_btn.grid(row=8, column=2, sticky='ew')

    menu.mainloop()
# Menu 윈도우 END-----------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()