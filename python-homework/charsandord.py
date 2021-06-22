sor = 0

for char in range(ord("a"), ord("z")+1):
    sor += 1
    print(char, chr(char), end=" ")
    if sor == 3:
        print()
        sor = 0