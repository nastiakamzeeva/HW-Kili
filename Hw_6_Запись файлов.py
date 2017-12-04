f = open('text.txt', 'w')
str = []
print("Введите любое латинское слово.")
s = 'a'
while s!= ' ':
    s = input()
    if s.endswith('re'):
        str.append(s)
        continue
    if s.endswith('i'):
        str.append(s)
        continue
    if s.endswith('ri'):
        str.append(s)
        continue
    if s.endswith('isse'):
        str.append(s)
        continue
    if s.endswith('iri'):
        str.append(s)
        continue
for index in str:
    f.write(index + '\n')
f.close()
