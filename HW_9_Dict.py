import re


def openF():
    print('Enter the name of the file: ')
    file_name = str(input())
    file = open(file_name)
    return file


def words(file):
    r = []
    for s in file:
        t = re.split("[\s;:\-_*\".,?!()]", s)
        t = [a for a in t if
             a != '']
        r.extend(t)
    return r


def search(s):
    dic = {'-ed': 0, '-y': 0}
    ss = []
    s2 = []
    for i in s:
        if i[-2:] == 'ed' or i[-2:] == 'ED':
            ss.append(i)
            dic['-ed'] += 1
    for i in ss:
        i.split()
        if i[-3:] == 'ied' or i[-3:] == 'yed' or i[-3:] == 'IED' or i[-3:] == 'YED':
            s2.append(i)
            dic['-y'] += 1
    print('The number of words ending in [-ed]:', dic['-ed'])
    print('Words formed from verbs in [-y]:', dic['-y'])


def main():
    file = openF()
    r = words(file)
    search(r)


main()
