lines = []
file = open('data.txt', 'a')
for i in open('adat.txt'):
    lines.append(i)


file.writelines(str(lines))