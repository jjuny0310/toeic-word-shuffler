from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
from load import *
import random


menu = Tk()

fontStyle = tkFont.Font(family="Lucida Grande", size=14, weight="bold")
word_fontStyle = tkFont.Font(family="Lucida Grande", size=13, weight="bold")

DAY_NUM = load.DAY_NUM

r1 = IntVar()
r1.set(1)

r2 = IntVar()
r3 = IntVar()
r4 = IntVar()
day_checkval = {}

# 단어 불러오기
all_day, basic, grade800 = load.load()


def backSpace():
    run.withdraw()
    menu.deiconify()

# 단어 재 셔플
def reShuffleWord():
    for i in treeview.get_children():
        treeview.delete(i)
    insertWord()


# 단어 삽입
def insertWord():
    global cur_idx, treelist, word_num
    treelist = []
    cur_idx = 0

    if r1.get():
        for i in range(DAY_NUM):
            if day_checkval[f"day{i+1}"].get():
                for init_word in all_day[f"day{i+1}"]:
                    treelist.append(init_word)

    if r2.get():
        for i in range(DAY_NUM):
            if day_checkval[f"day{i + 1}"].get():
                for init_word in basic[f"day{i + 1}"]:
                    treelist.append(init_word)

    if r3.get():
        for i in range(DAY_NUM):
            if day_checkval[f"day{i + 1}"].get():
                for init_word in grade800[f"day{i + 1}"]:
                    treelist.append(init_word)

    # 단어 셔플
    random.shuffle(treelist)
    
    # 단어 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i, values=treelist[i][0], iid=i)


# 키 입력 이벤트
def keyEvent(event):
    global cur_idx

    treeview.set(cur_idx, column="two", value=treelist[cur_idx][1])
    cur_idx += 1


# 체크박스 모두 선택
def allCheckBoxOn():
    r1.set(1); r2.set(1); r3.set(1); r4.set(1)
    for i in range(DAY_NUM):
        day_checkval[f"day{i+1}"].set(1)


# 체크박스 초기화
def allCheckBoxOff():
    r1.set(0); r2.set(0); r3.set(0); r4.set(0)
    for i in range(DAY_NUM):
        day_checkval[f"day{i+1}"].set(0)


# 테이블 크기 변경 비활성화
def tableResizeBlock(event):
    if treeview.identify_region(event.x, event.y) == "separator":
        return "break"


# Run 윈도우-----------------------------------------------------------------------------------------------
def createRunWindow():
    global treeview, run
    
    menu.withdraw()

    run = Toplevel(menu)
    run.title("VOCA - RUN")
    run.geometry("900x770+300+0")
    # run.resizable(False, False)

    # 토익 단어장
    voca_label = Label(run, text=f"토익 단어장", font=fontStyle)
    voca_label.grid(row=0, column=0)

    voca_frame = Frame(run, pady=3)
    run.grid_rowconfigure(1, weight=1)
    run.grid_columnconfigure(0, weight=1)

    voca_frame.grid(row=1, column=0, sticky="nsew")

    voca_frame.grid_rowconfigure(0, weight=1)
    voca_frame.grid_columnconfigure(1, weight=1)

    # 스타일(Treeview)
    style = ttk.Style(run)
    style.theme_use("classic")
    style.configure("Treeview", font=word_fontStyle, rowheight=30)

    treeview = ttk.Treeview(voca_frame, columns=["one", "two"], displaycolumns=["one", "two"])
    treeview.pack(side="left", fill="y", expand=True)

    # 스크롤 바 생성
    scroll = ttk.Scrollbar(voca_frame, orient="vertical", command=treeview.yview)
    scroll.pack(side='right', fill='y')

    treeview.configure(yscrollcommand=scroll.set)

    # 테이블 사이즈 변경 비활성화
    treeview.bind('<Button-1>', tableResizeBlock)

    # 테이블 설정
    treeview.column("#0", width=65)
    treeview.heading("#0", text="번호")

    treeview.column("#1", width=400, anchor="center")
    treeview.heading("one", text="단어", anchor="center")

    treeview.column("#2", width=400, anchor="center")
    treeview.heading("two", text="의미", anchor="center")

    insertWord()


    # RUN 관련 버튼
    runbtn_frame = Frame(run, pady=3)
    runbtn_frame.grid(row=2, column=0)

    runbtn_frame.grid_rowconfigure(0, weight=1)
    runbtn_frame.grid_columnconfigure(1, weight=1)

    shuffle_btn = Button(runbtn_frame, text="단어 섞기", font=fontStyle, command=reShuffleWord)
    back_btn = Button(runbtn_frame, text="뒤로가기", font=fontStyle, command=backSpace)
    shuffle_btn.grid(row=3, column=0, sticky='ew')
    back_btn.grid(row=3, column=1, sticky='ew')

    # 키 입력 이벤트
    run.bind("<space>", keyEvent)


# Run 윈도우 END-----------------------------------------------------------------------------------------------


# Main(Menu 윈도우)-----------------------------------------------------------------------------------------------
def main():
    global day_checkval

    menu.title("VOCA - MENU")
    menu.geometry("830x300+350+200")
    menu.resizable(False, False)

    # 옵션1. DAY 선택
    option1 = Label(menu, text='1. DAY 선택(1일 ~ 30일)', font=fontStyle)
    option1.grid(row=0, column=0, sticky='w')

    label1 = Label(menu)
    label1.grid(row=1, column=0)

    day_checkbtn = {}
    for i in range(DAY_NUM):
        day_checkval[f"day{i+1}"] = IntVar()
        day_checkbtn[f"day{i+1}"] = Checkbutton(label1, text=f"DAY{i+1}", variable=day_checkval[f"day{i+1}"]).grid(row=2+int(i//10), column=(i % 10))
    day_checkval["day1"].set(1)

    menu.grid_rowconfigure(4, minsize=50)

    # 옵션2. 범위 선택
    option2 = Label(menu, text='2. 단어 범위 선택', font=fontStyle)
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