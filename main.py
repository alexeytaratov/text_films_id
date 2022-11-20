text = []
text2 = []
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
print(text)

for i in range(len(text)):
    if (text[i] != '\n') and (('#' in text[i]) != True) and (('---' in text[i]) != True):
        text2.append(text[i])

for i in range(len(text2)):
    text2[i] = str(i) + ' ' + str(text2[i])
print(text2)

with open('text2.txt', 'w', encoding='utf-8') as f2:
    for line in text2:
        f2.write(line)


