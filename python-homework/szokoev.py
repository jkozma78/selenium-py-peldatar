evin = int(input("Szökőév?"))

def fuggv_szokoev(ev):
    if (ev % 100 == 0 and ev % 400 != 0) or ev % 4 != 0:
        return False
    else:
        return True

print(fuggv_szokoev(evin))