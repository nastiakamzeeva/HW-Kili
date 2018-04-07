#задание1
with open('text.xml', encoding='utf-8') as f:
    f = f.read()
    line = 0
    for i in f:
        line += 1
    num_lines = sum(1 for line in f)
    print(num_lines)
