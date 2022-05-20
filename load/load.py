DAY_NUM = 30

# 단어장 불러오기
def load():
    # 단어장 load
    voca = open("load/vocabulary.txt", 'r', encoding='UTF8')
    lines = voca.readlines()

    # 플래그 변수
    day_flag = False
    basic_flag = False
    grade800_flag = False
    grade900_flag = False

    all_day = {}
    basic = {}
    grade800 = {}
    grade900 = {}

    day_count = 0


    for i in range(DAY_NUM):
        all_day[f"day{i + 1}"] = []
        basic[f"day{i + 1}"] = []
        grade800[f"day{i + 1}"] = []
        grade900[f"day{i + 1}"] = []

    # 텍스트 분리
    for i, line in enumerate(lines):
        if line.startswith("-day") or line.startswith("-Day") or line.startswith("-DAY"):
            day_count += 1
            day_flag = True
            basic_flag = False
            grade800_flag = False
            grade900_flag = False
        elif line.startswith("-토익"):
            day_flag = False
            basic_flag = True
            grade800_flag = False
            grade900_flag = False
        elif line.startswith("-800점"):
            day_flag = False
            basic_flag = False
            grade800_flag = True
            grade900_flag = False
        elif line.startswith("-900점"):
            day_flag = False
            basic_flag = False
            grade800_flag = False
            grade900_flag = True
        elif line == "\n":
            day_flag = False
            basic_flag = False
            grade800_flag = False
            grade900_flag = False

        if day_flag:
            word_mean = lines[i].split("/")
            if len(word_mean) == 2:
                all_day[f"day{day_count}"].append([(word_mean[0], ""), word_mean[1].replace("\n", "")])
        elif basic_flag:
            word_mean = lines[i].split("/")
            if len(word_mean) == 2:
                basic[f"day{day_count}"].append([(word_mean[0], ""), word_mean[1].replace("\n", "")])
        elif grade800_flag:
            word_mean = lines[i].split("/")
            if len(word_mean) == 2:
                grade800[f"day{day_count}"].append([(word_mean[0], ""), word_mean[1].replace("\n", "")])
        elif grade900_flag:
            word_mean = lines[i].split("/")
            if len(word_mean) == 2:
                grade900[f"day{day_count}"].append([(word_mean[0], ""), word_mean[1].replace("\n", "")])

    return all_day, basic, grade800, grade900

