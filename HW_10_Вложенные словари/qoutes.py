import random


def get_dict():
    d = {}
    quest = []
    with open("words.txt", encoding='utf-8') as f:
        tip = ''
        for line in f:
            if line == '\ufeffСлово,Подсказка\n':
                continue
            if tip == '':
                word, tip = line.split(',', maxsplit=1)
                quest.append(word)
                tip = tip[:-1]
                tip_list = d.setdefault(word, [])
                tip_list.append(tip)
                tip = ''
    return d, quest


def question(d, quest):
    s = list(set(quest))
    n = len(s)
    q = s[random.randint(0, n)]  # загаданное слово
    tip = d.get(q)  # подсказка
    l = len(tip)
    a = tip[random.randint(0, l - 1)]
    str = a + ' '
    for w in a:
        str = str + '.'
    return q, str


def riddle(q, str):
    print(str)
    while True:
        ans = input()
        ans = ans.lower()
        if ans == q.lower():
            print("Вы угадали.")
            break
        else:
            print("Попробуйте снова.")


def main():
    print("Введите подходящее слово вместо точек.")
    d, quest = get_dict()
    q, str = question(d, quest)
    riddle(q, str)


main()
