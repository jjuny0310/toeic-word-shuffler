def vocaLoad():
    f = open("vocabulary.txt", 'r', encoding='UTF8')
    lines = f.readlines()

    # 플래그 변수
    day_flag = False
    basic_flag = False
    grade800_flag = False

    all_day_word = {}
    all_day_mean = {}
    day_count = 0

    basic_day_word = {}
    basic_day_mean = {}

    grade800_day_word = {}
    grade800_day_mean = {}


    for i in range(30):
        all_day_word[f"day{i+1}"] = []
        all_day_mean[f"day{i+1}"] = []
        basic_day_word[f"day{i+1}"] = []
        basic_day_mean[f"day{i+1}"] = []
        grade800_day_word[f"day{i+1}"] = []
        grade800_day_mean[f"day{i+1}"] = []

    # print(all_day_word)
    # print(all_day_mean)
    # print(lines)
    # print("=======================================")
    for i, line in enumerate(lines):
        if line.startswith("#day"):
            day_count += 1
            day_flag = True
            basic_flag = False
            grade800_flag = False
        elif line.startswith("-토익"):
            day_flag = False
            basic_flag = True
            grade800_flag = False
        elif line.startswith("-800점"):
            day_flag = False
            basic_flag = False
            grade800_flag = True
        elif line == "\n":
            day_flag = False
            basic_flag = False
            grade800_flag = False

        if day_flag:
            word_mean = lines[i].split("/")
            if len(word_mean) == 2:
                all_day_word[f"day{day_count}"].append((word_mean[0], ""))
                all_day_mean[f"day{day_count}"].append(word_mean[1].replace("\n", ""))
        elif basic_flag:
            word_mean = lines[i].split("/")
            if len(word_mean) == 2:
                basic_day_word[f"day{day_count}"].append((word_mean[0], ""))
                basic_day_mean[f"day{day_count}"].append(word_mean[1].replace("\n", ""))
        elif grade800_flag:
            word_mean = lines[i].split("/")
            if len(word_mean) == 2:
                grade800_day_word[f"day{day_count}"].append((word_mean[0], ""))
                grade800_day_mean[f"day{day_count}"].append(word_mean[1].replace("\n", ""))

    print(all_day_word)
    print(all_day_mean)
    print(basic_day_word)
    print(basic_day_mean)
    print(grade800_day_word)
    print(grade800_day_mean)

    return all_day_word, all_day_mean, basic_day_word, basic_day_mean, grade800_day_word, grade800_day_mean


if __name__ == '__main__':
    vocaLoad()
