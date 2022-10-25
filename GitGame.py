letsplay = input("Haluatko pelata peliä? (kyllä/ei)\n")

while True:
    count = 0    
    if letsplay != "kyllä":
        print("Ei sitten! :(")
        break
    question1 = str(input("Montako varvasta kissalla on? a) 20 b) 18 c) 16\n"))
    if question1 == "b" or question1 == "18":
        count += 1
        print("Oikein!")
    else:
        print("Väärin...")
    question2 = str(input("Montako virallista koirarotua on olemassa? a) noin 500 b) noin 400 c) noin 300\n"))
    if question2 == "c" or question2 == "300":
        count += 1
        print("Oikein!")
    else:
        print("Väärin...")        
    question3 = str(input("Kuinka monta nenää etanalla on? a) 0 b) 1 c) 4\n"))
    if question3 == "c" or question3 == "4":
        count += 1
        print("Oikein!")
    else:
        print("Väärin...")
    question4 = str(input("Kuinka monet aivot meritähdellä on? a) 0 b) 1 c) 2\n"))
    if question4 == "a" or question4 == "0":
        count += 1
        print("Oikein!")
    else:
        print("Väärin...")

    print(f"Sait oikein {0}/6!")
    break
