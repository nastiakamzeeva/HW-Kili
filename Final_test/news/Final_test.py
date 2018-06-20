import re

dict = {}

def write_in_file(dict):

    with open('new_file.txt', 'w', encoding='utf-8')as f:
        k = dict.keys()
        for keys in k:
            f.write('{}    {}'.format(keys, dict[keys] + '\n')

def search(noun):

    with open('{}.html'.format(noun), 'r') as f:
        f = f.read()
        count = len(re.findall(r'<."[а-яА-Я]"...."S'.format(noun), f))
    return count


def main():

    list = ['itartass1','itartass2','itartass3',
            'itartass4','itartass5','rbk2','rbk3',
            'rbk4','rbk6','rbk7','rian1','rian2','rian3','rian5']
    for nouns in list:
        c = search(nouns)
        dict.setdefault(nouns, c)
    print(dict)

    write_in_file(dict)

main()

