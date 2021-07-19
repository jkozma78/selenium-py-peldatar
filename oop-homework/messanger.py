# Készíts egy olyan Python osztályt, ami számolja a fogadott és elküldött üzenetetek és meg tudjá állapítani,
# hogy ez mennyibe került nekünk.
# Hogy milyen műveleteket végzett el a felhasználó az legyen egy listában tárolva
# (például: operations = [1,1,1,2,2,1,1,1,2,2,2,2,1,1]).
# Az 1-es jelentse azt, hogy fogadott egy db üzenetet, a 2-es pedig azt, hogy küldött egyet.
# Az osztály neve legyen az, hogy MessageBox.
# A megoldást egy messanger.py nevű file-ban kell beadnod.

operations = [1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1]


class MessageBox:
    def __init__(self, _list):
        self.receivedsms = f'Fogadott üzenetek száma: {_list.count(1)}'
        self.sentsms = f'Elküldött üzenetek száma: {_list.count(2)}'

    def sum(self):
       return f'Valami:{ self.sentsms * 2}'


print(MessageBox(operations).sum())