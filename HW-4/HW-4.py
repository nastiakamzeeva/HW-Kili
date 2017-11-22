with open("poem.txt", encoding = "utf-8") as f:
    poem = f.read()
poem = poem.replace(' —', '')
poem = poem.replace(':', '')

splited_poem = poem.split()

n = 0
for word in splited_poem:
    if word.endswith(","):
        n += 1
for word in splited_poem:
    if word.endswith("."):
        n += 1
m = 100-(n/len(splited_poem))*100
print(m, "%")
