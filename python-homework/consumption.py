onroad = float(input("Országúti fogyasztás:"))
incity = float(input("Városi fogyasztás:"))
petrol = float(input("Üzemanyag ára:"))
roaddistance = float(input("Országúton megtett út hossza:"))
citydistance = float(input("Városban megtett út hossza:"))

consumption1 = (onroad / roaddistance)*100
consumption2 = (incity / citydistance)*100

print(f"Fogyasztás: {consumption1 + consumption2} liter")