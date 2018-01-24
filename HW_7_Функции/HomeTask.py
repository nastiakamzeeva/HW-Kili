# coding=utf-8
import random


# Существительные для 1 и 2 строк
def noun(number):
    # сущ ед. числа
    with open("NounS.txt") as file:
        singular_nouns = [row.strip() for row in file]
    # сущ мн. числа
    with open("NounP.txt") as file:
        plural_nouns = [row.strip() for row in file]
    # мы ожидаем, что функция будет получать в качестве аргумента либо строку 's' - для сущ. ед.ч.
    if number == 's':
        return random.choice(singular_nouns)
    # либо любую другую строку - для сущ. мн.ч.
    return random.choice(plural_nouns)


# глаголы для 1 строки
def verb(number):
    # глаголы ед. числа
    with open("VerbS.txt") as file:
        singular_verbs = [row.strip() for row in file]
    # глаголы мн. числа
    with open("VerbP.txt") as file:
        plural_verbs = [row.strip() for row in file]
    if number == 's':
        return random.choice(singular_verbs)
    return random.choice(plural_verbs)


# Прилагательные для 2 строки
def adj(number):
    # Прилагательные ед. числа
    with open("AdjS.txt") as file:
        singular_adj = [row.strip() for row in file]
    # Прилагательные мн. числа
    with open("AdjP.txt") as file:
        plural_adj = [row.strip() for row in file]
    if number == 's':
        return random.choice(singular_adj)
    return random.choice(plural_adj)


# глаголы для 3 строки
def verb2():
    with open("Verb2.txt") as file:
        verbs = [row.strip() for row in file]
    return random.choice(verbs)


# наречия для 3 строки
def adv():
    with open("Adv.txt") as file:
        adv = [row.strip() for row in file]
    return random.choice(adv)


# пунктуация
def punctuation():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def check(s):
    syb = 0
    for i in s:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
                letter == "i" or letter == "o" or \
                letter == "u" or letter == "y" \
                or letter == "A" or letter == "E" or \
                letter == "I" or letter == "O" or \
                letter == "U" or letter == "Y":
            syb += 1
    return syb

# создание строки 1
def verse1():
    ss = ""
    syb = 0
    x = random.randint(0, 1)
    if x == 1:
        while syb != 5:
            syb = 0
            s = noun('s') + ' ' + verb('s') + punctuation()
            syb = check(s)
            ss = s
    if x == 0:
        while syb != 5:
            syb = 0
            s = noun('a') + ' ' + verb('a') + punctuation()
            syb = check(s)
            ss = s
    return ss


# создание строки 2
def verse2():
    ss = ""
    syb = 0
    x = random.randint(0, 1)
    if x == 1:
        while syb != 7:
            syb = 0
            s = noun('s') + ' ' + adj('s') + punctuation()
            syb = check(s)
            ss = s
    if x == 0:
        while syb != 7:
            syb = 0
            s = noun('a') + ' ' + adj('a') + punctuation()
            syb = check(s)
            ss = s
    return ss


# создание строки 3
def verse3():
    ss = ""
    syb = 0
    while syb != 5:
        syb = 0
        s = adv() + ' ' + verb2() + punctuation()
        syb = check(s)
        ss = s
    return ss


# вывод всех строк
def main():
    print(verse1())
    print(verse2())
    print(verse3())


main()
