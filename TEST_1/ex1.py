### задача 1 ###
with open('dict.txt', 'r', encoding = 'utf-8')as f:
    lines = f.readlines()
for line in lines:
    line = line.split('|')
    if len(line[0]) >= 20:
        print(line, '\n')
