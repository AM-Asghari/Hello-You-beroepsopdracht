import time

stuk_2 = False
stuk_3 = False
stuk_4 = False
stuk_5 = False
stuk_6 = False
stuk_7 = False
stuk_8 = False
stuk_9 = False
stuk_10 = False


stuk_1 = True
while stuk_1:
    print("")
    print("Hello You!")
    print("In deze tekst based applicatie ga je het verhaal van Musa Ghani, een 18 jarige afghaanse vluchteling, volgen uit het perspectief van de vluchteling.")
    print("")

    print("Je ouders hebben sambosa, je favoriete gerecht, gemaakt voor het avond eten om te vieren dat je aangenomen bent voor de opleiding jurist in Kabul.")
    print("Na het avond eten besluit je: ")
    print("A. het nieuws te gaan kijken")
    print("B. je oom een paar straten verder op te bezoeken omdat ze naar het buitenland gaan verhuizen")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("Je zet het nieuws aan en gaat op de bank zitten met je ouders. 'De Taliban heeft de stad Bist Hazari overgenomen en zijn nu onderweg naar Shahre Naow. Het zal niet lang meer duren tot ze de hoofdstad Kabul gaan bezetten.' Je ziet beelden van de stad Bist Hazari, het ziet er ernstig uit.")
        print("Je ouders verzamelen in paniek het laatste beetje geld dat ze hebben. Net genoeg geld om een persoon naar Europa te smokkelen.")
        print("Ze besluiten om jou naar Nederland te sturen voor je eigen veiligheid.")
        print("")
        time.sleep(2)
        stuk_2 = True
        stuk_1 = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("Je komt aan bij je oom thuis nadat jullie even hebben bijgepraat gaat hij samen met zijn vrouw en je neefje verder met inpakken.")
        print("De telefoon gaat, je oom neemt op.")
        print("Je oom vertelt je dat je ouders hebben gebeld, blijkbaar is de Taliban onderweg naar Kabul en ze willen dat je met je oom mee reist voor je eigen veiligheid")
        print("")
        time.sleep(2)
        stuk_3 = True
        stuk_1 = False

while stuk_2:
    print("")
    print("Je vlucht naar Turkije met de auto.")
    print("Eenmaal Turkije moet je opzoek naar een smokkelaar om je in Griekenland te krijgen waar een kennis van je Vader je gaat helpen om in Nederland te komen.")
    print("In Turkije vind je een smokkelaar van Turkse afkomst en een smokkelaar van Griekse afkomst.")
    print("De Griekse smokkelaar heeft een betere boot dan de Turkse man, maar je hebt niet genoeg geld om hem te betalen na de reis.")
    print("De Turkse smokkelaar heeft een wat slechtere boot, maar je hebt genoeg geld om met hem mee te reizen.")
    print("Je besluit om: ")
    print("A. met de Griek te reizen")
    print("B. met de Turk te reizen")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("De reis duurt lang en je hebt niet veel ruimte om te bewegen. Naar de wc gaan kan niet.")
        print("Je komt in Griekenland aan. De kennis van je vader wacht daar op je en helpt je verder.")
        print("")
        time.sleep(2)
        stuk_4 = True
        stuk_2 = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("De reis duurt lang. Er is zo weinig ruimte dat de meeste mensen op elkaar liggen. De golven slaan heftig tegen de boot aan.")
        print("")
        time.sleep(2)
        stuk_5 = True
        stuk_2 = False

while stuk_3:
    print("")
    print("Je ouders hebben je vliegticket betaald met het kleine beetje geld wat ze hadden. Je oom neemt je mee met het vliegtuig naar Griekenland")
    print("Eenmaal in Griekenland aangekomen kom je in contact met een kennis van je vader. Je oom en zijn familie gaan naar Italie.")
    print("Je oom en jij scheiden hier jullie wegen nadat hij je in contact heeft gebracht met een kennis van je Vader in Griekenland")
    print("")
    time.sleep(2)
    stuk_4 = True
    stuk_3 = False

while stuk_4:
    print("")
    print("De kennis van je vader stelt zichzelf voor. Hij vertelt dat hij je vader kent van de basisschool, ze waren vroeger beste vrienden.")
    print("De kennis helpt je naar Nederland te reizen vanuit Griekenland.")
    print("In Nederland aangekomen brengt hij je contact met het IND, zij bepalen of je terug moet of mag blijven in Nederland.")
    print("")
    time.sleep(2)
    stuk_6 = True
    stuk_4 = False

while stuk_5:
    print("")
    print("De golven worden steeds heftiger, de kleine boot kan het niet aan.")
    print("De boot zinkt. Sommige mensen in de boot houden de hoop dat er hulp aan komt.")
    print("De hulp is nooit aangekomen.")
    print("Hier eindigt helaas je verhaal.")
    print("")
    time.sleep(2)
    stuk_5 = False

while stuk_6:
    print("")
    print("Eenmaal bij het IND aangekomen moet je ze overtuigen dat je niet veilig bent in je Afghanistan.")
    print("Het IND haalt een tolk erbij zodat hij je verhaal kan vertellen.")
    print("Je vertelt dat: ")
    print("A. De taliban heeft je stad bezet dus je bent gevlucht uit angst")
    print("B. Je liegt dat je een verslaggever was in Afghanistan die openlijk tegen het beleid van de taliban was")
    print("C. Je vertelt dat je ouders de beslissing voor je hebben gemaakt omdat zij bang zijn voor de taliban")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("De tolk vertaalt wat je hebt verteld.")
        print("Het IND besluit dat je geen gevaar loopt voor de taliban omdat je niks verkeerd hebt gedaan.")
        print("Je wordt op het vliegtuig terug naar Afghanistan gezet.")
        print("")
        time.sleep(2)
        stuk_7 = True
        stuk_7 = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("Het IND besluit dat je in Nederland mag blijven omdat je als verslaggever niet veilig bent in Aghanistan.")
        print("Ze besluiten je door te sturen naar een asiel zoekers centrum in Almere Buiten.")
        print("")
        time.sleep(2)
        stuk_8 = True
        stuk_6 = False
    elif restartInput == "c" or restartInput == "C":
        print("")
        print("Het IND besluit dat je geen gevaar loopt voor de taliban omdat je niks verkeerd hebt gedaan.")
        print("Je wordt op het vliegtuig terug naar Afghanistan gezet.")
        print("")
        time.sleep(2)
        stuk_7 = True
        stuk_6 = False

while stuk_7:
    print("Je zit in de vliegtuig naar Afghanistan.")
    print("Je denkt bij jezelf 'mijn hele reis is voor niks geweest'.")
    print("Je komt aan in Aghanistan.")
    print("Hier eindigt helaas je verhaal.")
    print("")
    time.sleep(2)
    stuk_7 = False

while stuk_8:
    print("")
    print("Je komt aan in Almere buiten.")
    print("De COA heeft je een woning gegeven met een slaapkamer, woonkamer, keuken en badkamer.")
    print("Je mag zonder verblijfsvergunning nog niet werken of je rijbewijs halen.")
    print("Je besluit om in afwachting van je verblijfsvergunning te: ")
    print("A. Nederlands te leren zodat je opnieuw kan beginnen met het studeren om jurist te worden.")
    print("B. Nederlands te leren om de lokale gemeenschap beter te leren kennen.")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("Je merkt dat Nederlands een heel moeilijke taal is maar je krijgt het al snel onder de knie en je begint je studie als jurist in het engels op universitair niveau.")
        print("")
        time.sleep(2)
        stuk_9 = True
        stuk_8 = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("Je spreekt de taal vloeiend en bent begonnen met een opleiding op MBO niveau als buschauffeur.")
        print("Je leert de mensen in Almere een beetje kennen en je leert de weg in je nieuwe stad.")
        print("In de biebliotheek in het centrum leer je iemand kennen haar naam is Tess.")
        print("")
        time.sleep(2)
        stuk_10 = True
        stuk_8 = False

while stuk_9:
    print("")
    print("Je hebt je studie afgerond en je spreekt vloeiend Nederlands. Het is je 23e verjaardag precies vandaag krijg je te horen dat je een verblijfsvergunning hebt gekregen.")
    print("Het perfecte verjaardagscadeau. Je kan nu opzoek naar een sociale huurwoning en je loopt stage bij een bedrijf in Almere.")
    print("Na het afronden van je stage wordt je aangenomen bij het bedrijf waar je stage liep.")
    print("Je verdient aardig wat geld.")
    print("Je besluit om: ")
    print("A. Een huis te kopen")
    print("B. Je ouders naar Nederland proberen te krijgen.")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("Je koopt een huis in Bloemendaal.")
        print("Je bent heel blij met je werk maar je verveelt je in je vrije tijd.")
        print("In je nieuwe huis in Bloemendaal besluit je een atelier te maken.")
        print("Musa Ghani sterft op 89 jarige leeftijd aan ouderdom.")
        print("Hij heeft een gelukkig leven geleid.")
        print("Hier eindigt je verhaal")
        stuk_9 = False
    elif restartInput == "B" or  restartInput == "b":
        print("")
        print("Je hebt je ouders overtuigd om naar Nederland te komen.")
        print("Het IND besluit dat je ouders een verblijfsvergunning krijgen omdat jij er al een hebt.")
        print("Je bent na 5 jaar hereningd met je ouders.")
        print("Jullie kopen samen een sociale huurwoning.")
        print("Je leeft nog lang en gelukkig met je ouders in Almere.")
        print("Hier eindigt je verhaal.")
        stuk_9 = False

while stuk_10:
    print("")
    print("Je gaat steeds vaker met Tess om wanneer je niet aan het werk bent.")
    print("Je vraagt Tess of ze een relatie met je wilt en ze zegt ja.")
    print("Je bent nu 26, na 7 jaar een relatie met Tess te hebben gehad besluit je: ")
    print("A. Om haar ten huwelijk te vragen")
    print("B. Om het uit te maken met Tess")
    restartInput = input("Kies een optie: ")
    if restartInput == "a" or restartInput == "A":
        print("")
        print("Je vraagt Tess ten huwelijk en ze zegt ja.")
        print("Jullie kopen samen een groot huis in Aerdenhout om een famillie te starten.")
        print("Na een aantal jaar samen met Tess hebben jullie 3 kinderen.")
        print("Een zoon van 18 jaar oud, een zoon van 15 jaar oud en een dochter van 10.")
        print("Musa Ghani woont nog lang en gelukkig met zijn vrouw Tess en hun kinderen in Aerdenhout.")
        print("Hier eindigt je verhaal.")
        stuk_10 = False
    elif restartInput == "b" or restartInput == "B":
        print("")
        print("Je hebt het uit gemaakt met Tess.")
        print("Zonder Tess voelt je leven als chauffeur leeg.")
        print("Je raakt verslaafd aan alcohol om je je te vermaken in je dagelijkse leven.")
        print("Musa Ghani sterft op 54 jarige leeftijd aan alcohol vergiftiging.")
        print("Hier eindigt helaas je verhaal.")
        stuk_10 = False
