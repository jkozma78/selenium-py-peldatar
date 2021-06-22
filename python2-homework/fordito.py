szam_list = []
szam = 1
while szam != 0:
    szam = int(input("Adj meg pozitív, egész számokat:"))
    szam_list.append(szam)
print(szam_list[::-1])
