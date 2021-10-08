while True:
    print("Hello you!")
    print("Ik ben Mosawer")
    print("Wie ben jij?")
    name = input("Type je naam in: ")
    print("Hallo ", name,"!")
    print("")

    print("Ik ben een nieuwkomer op het Mediacollege Amsterdam.")
    print("Door een aantal vragen te beantwoorden leer jij me beter kennen!")
    print("")

    print("Voor ik naar het MBO op het Mediacollege Amsterdam kwam deed ik op de middelbare school:")
    print("  A: MAVO Op Kaj Munk in Hoofddorp")
    print("  B: VWO Op het Montesorri Lyceum Amsterdam")
    print("  C: HAVO Op Haarlemmermeer Lyceum in Hoofddorp")
    answer = input("Kies A, B of C: ")

    if answer == "A" or answer == "a":
        print("Nee het goeie antwoord is C Maar, ik woon wel in Hoofddorp")
    elif answer == "B" or answer == "b":
        print("Nee het goeie antwoord is C maar, ik kom wel af en toe naar Amsterdam om mijn hobby te beoefenen")
    elif answer == "C" or answer == "c":
        print("Ja, ik ben helaas drie keer blijven zitten op het Haarlemmermeer Lyceum en een keer op HAVO VAVO op Nova College")
    print("")
    print("Mijn Hobbys zijn:")
    print("A: Skaten en boksen")
    print("B: Voetballen en Netflix")
    print("C: Zwemmen en hardlopen")
    answer = input ("Kies A, B of C: ")

    if answer == "A" or answer == "a":
        print("Ja, ik skate en boks nu al bijna drie jaar!")
    if answer == "b" or answer == "B":
        print("Nee ik hou niet van voetballen en kijk niet zo vaak netflix")
    if answer == "C" or answer == "c":
        print("Nee maar ik vind het af en toe wel leuk om te doen")
    print("")
    print("Ik ben al zo oud:")
    print("  A: 19")
    print("  B: 21")
    print("  C: 20")
    answer = input ("Kies A, B of C: ")
        
    if answer == "A" or answer == "a":
        print("Nee het goeie antwoord is C")
    elif answer == "B" or answer == "b":
        print("Nee het goeie antwoord is C")
    elif answer == "C" or answer == "c":
        print("Ja ik ben 20 jaar oud!")
    print("")
    print("Ik hoop dat je me wat beter hebt leren kennen!")
    print("Wil je de quiz nog een keer doen?")
    print("Type Ja of Nee")
    inputText = input()
    print("input:", inputText)
    if inputText == "nee":
        break