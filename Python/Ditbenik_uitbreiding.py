import time
print("Hello you!")
print("Ik ben Mosawer")
print("Wie ben jij?")
name = input("Type je naam in: ")
print("Hallo ", name,"!")
print("")

mijn_hobby_is = False
hoe_oud_ben_ik = False
mijn_favoriete_serie_is = False
mijn_huisdier_is_een = False
woning = False
favoriete_stad = False
favoriete_game = False

voor_mbo_deed_ik = True
while voor_mbo_deed_ik:
    print("")
    print("Leer me kennen door middel van deze vragen!")
    print("Voordat ik naar het MA kwam deed ik: ")
    print("A. HAVO op haarlemmermeerlycuem in Hoofddorp")
    print("B. VWO op haarlememermeerlycuem in Hooofddorp")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Ja, ik deed HAVO op het haarlemmermeerlycuem!")
        print(" ")
        time.sleep(3)
        mijn_hobby_is = True
        voor_mbo_deed_ik = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Nee, helaas!")
        print("")
        time.sleep(3)
        hoe_oud_ben_ik = True
        voor_mbo_deed_ik = False

while hoe_oud_ben_ik:
    print("")
    print("Ik ben zoveel jaar oud: ")
    print("A. 22")
    print("B. 20")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Nee, ik ben 20 jaar oud!")
        print(" ")
        time.sleep(3)
        woning = True
        hoe_oud_ben_ik = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Ja, ik ben 20 jaar oud!")
        print("")
        time.sleep(3)
        mijn_favoriete_serie_is = True
        hoe_oud_ben_ik = False

while mijn_hobby_is:
    print("")
    print("Mijn hobby is: ")
    print("A. Skaten en boksen")
    print("B. Voetballen en zwemmen")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Ja, ik skate al 3 jaar en ik heb 2 jaar gebokst!")
        print(" ")
        time.sleep(3)
        mijn_favoriete_serie_is = True
        mijn_hobby_is = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Nee, helaas!")
        print("")
        time.sleep(3)
        mijn_huisdier_is_een = True
        mijn_hobby_is = False

while mijn_favoriete_serie_is:
    print("")
    print("Mijn favoriete serie is: ")
    print("A. Breaking bad")
    print("B. Fresh prince of Bell Air")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Nee, mijn favoriete serie is Fresh prince of Bell Air!")
        print(" ")
        time.sleep(3)
        mijn_favoriete_serie_is = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Ja, ik heb alle seizoenen fysiek gekocht!")
        print("")
        time.sleep(3)
        mijn_favoriete_serie_is = False

while mijn_huisdier_is_een:
    print("")
    print("Mijn is een: ")
    print("A. Vogel")
    print("B. Hond")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Ja, ze heet cisko!")
        print(" ")
        time.sleep(3)
        woning = True
        mijn_huisdier_is_een = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Nee, ik heb een vogel maar ik wil ook nog een hond kopen")
        print("")
        time.sleep(3)
        woning = True
        mijn_huisdier_is_een = False

while woning:
    print("")
    print("Ik woon: ")
    print("A. Bij mijn ouders")
    print("B. Op mezelf")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Ja!")
        print(" ")
        time.sleep(3)
        favoriete_game = True
        woning = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Nee, maar ik wil in december (2021) op mezelf gaan wonen!")
        print("")
        time.sleep(3)
        favoriete_stad = True
        woning = False

while favoriete_stad:
    print("")
    print("Mijn favoriete stad is: ")
    print("A. Amsterdam")
    print("B. Hoofddorp")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Ja!")
        print(" ")
        time.sleep(3)
        favoriete_game = True
        favoriete_stad = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Nee, maar ik woon er wel!")
        print("")
        time.sleep(3)
        favoriete_stad = False

while favoriete_game:
    print("")
    print("Mijn favoriete game is: ")
    print("A. Minecraft")
    print("B. Terraria")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("[!] Nee, helaas!")
        print(" ")
        time.sleep(3)
        favoriete_game= False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("[!] Jal!")
        print("")
        time.sleep(3)
        favoriete_game = False
