age = int(input("Hány éves vagy?"))
drink = input("Mit szeretnél inni? (sör/kóla):")

if drink == "sör" and age >= 18 or drink == "kóla" and age <= 60:
    print(f"Egészségére, a {drink}")
elif age > 60:
    print("A koffein megemelheti a vérnyomásást")
elif age < 18:
    print("Nem adhatom ki")
else:
    print("Csak sör és kóla van!")