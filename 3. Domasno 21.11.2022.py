#1 Zadaca: Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi, da se dodadat vo list i da se soberat site broevi vo listata
"""brojki = []
broj = 0
zbir_br = 0
for i in range(10):
    broevi = int(input("Vnesete go brojot tuka: "))
    brojki.append(broevi)
    zbir_br+=broevi
    broj+=1
print("Vie vnesovte vo total {} broevi: ".format(len(brojki)))
print("Broevite sto gi vnesovte se {}".format(brojki))
print("Sumata na site broevi sto vnesovte e: {}".format(zbir_br))"""

#2 Zadaca: Da se napravi programa vo koja korisntikot ke moze da vnese proizvolen broj na broevi, da se dodadt vo lista i da se najde najgolemiot broj

"""brojki = []
while True:
    x = int(input("Vnesete go vasiot broj: "))
    brojki.append(x)
    d = input("Dali sakate da vnesete uste podatoci: ")
    if d.upper()=="DA":
        pass
    else:
        break
najgolem_br = max(brojki)
print("Listata na brojki koi gi vnesovte e: ",brojki)
print("Najgolemiot broj od celata lista e: {}".format(najgolem_br))"""

#3 Zadaca: Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na elementi, da se ispecati listata i korisnikot da moze da izbere kolku elementi i koi elementi ke gi izbrise

"""predmeti = []
predmeti1 = []
while True:
    x = input("Vnesete gi predmetite koj sakate da gi slusate: ")
    predmeti.append(x)
    predmeti1.append(x)
    d = input("Dali sakate da vnesete uste predmeti: ")
    if d.upper()=="DA":
        pass
    else:
        break
print("Listata na predmeti koj sakate da ja slusate e: ", predmeti)

while True:
    d = input("Dali sakate da izbrisete predmet za sledniot semestar: ")
    if d.upper() == "DA":
        break

izbrisani_predmeti = []

while True:
    x = input ("Vnesete gi predmetite koi ne sakate da gi slusate veke: ") 
    izbrisani_predmeti.append(x)
    predmeti.remove(x)
    d = input("Dali sakate da izbrisete uste predmeti: ")
    if d.upper()=="DA":
        pass
    else:
        break
print("Predmetite koi gi slusavte prethodnata godina se: ",predmeti1)
print("Predmetite koi ne sakate da gi slusate slednata godina se: ",izbrisani_predmeti)
print("Predmetite koi ke gi slusate slednata godina se: ",predmeti)"""

#4 Zadaca: Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na iminja, da se dodadat vo lista, i da se najde najdolgoto ime

"""Iminja = []
while True:
    x = input("Vnesete gi iminjata na vasite vraboteni: ")
    Iminja.append(x)
    d = input("Dali sakate da vnesete uste podatoci: ")
    if d.upper()=="DA":
        pass
    else:
        break
print("Iminjata na vasite vraboteni sto gi vnesovte se: ",Iminja) 
najdolgo_ime = max(Iminja, key=len) 
print("Imeto so najgolemi bukvi e: ", najdolgo_ime)"""

#5 Zadaca: Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na broevi, da se dodadat vo lista i da se najde vtoriot najgolem broj

"""Broevi = []
while True:
    x = int(input("Vnesete go vasiot broj: "))
    Broevi.append(x)
    d = input("Dali sakate da vnesete uste broevi: ")
    if d.upper()=="DA":
        pass
    else:
        break
print("Broevite sto gi vnesovte se: ", Broevi)
Broevi.sort()
Broevi.reverse()
print("Vtoriot najgolem broj spored redosledot na broevite sto go vnesovte e: ",Broevi[1])"""

#6 Zadaca: Da se napravi programa koja ke bide upotrebuvana vo nekoja prodavnica za prodazba. Korisnikot da moze da vnesuva produkti se dodeka ne izbere deka saka da plati. Produktitte da se dodavaat vo edna lista, cenite vo druga lista. Koga ke izbere deka saka da plati da mu se ispecatat produktite i cenite vo nalik na "fiskalna smetka". Da ima moznost korisnikot da plati i da se presmeta dali i kolku treba da mu se vrati kusur

"""produkti = []
cena = []
zbir_cena = 0
while True:
    proizvodi = input("Vnesete go proizvodot: ")
    produkti.append(proizvodi)
    cena1 = int(input("Vnesete ja cenata na {} ".format(proizvodi)))
    cena.append(cena1)
    zbir_cena+=cena1
    nov_proizvod = input("Dali sakate da platite sega: ")
    if nov_proizvod.lower() == "da":
        print("Fiskalna smetka: {} ""Suma: {}".format(produkti,zbir_cena))
        break
    else:
        pass
print("Vkupno za plakanje imate {} denari".format(zbir_cena))
dava_za_plakanje = []
while True:
    dava_za_plakanje = int(input("Davate za plakanje: "))
    kusur = dava_za_plakanje - zbir_cena
    nedostasuva = zbir_cena - dava_za_plakanje
    
    if dava_za_plakanje > zbir_cena:
        print("Vaseto plakanje e zavrseno, vasiot kusur e {} denari".format(kusur))
        print("Vo vasta korpa gi imate slednite produkti ",produkti)
        break
    elif dava_za_plakanje == zbir_cena:
        print("Vaseto plakanje e zavrseno uspesno")
        print("Vo vasta korpa gi imate slednite produkti ",produkti)
        break
    elif dava_za_plakanje < zbir_cena:
        print("Za da se izvrsi vaseto plakanje vi nedostavuvaat uste {} denari".format(nedostasuva))
        
    doplata = int(input("Potrebni vi se uste {} denari za da izvrsite naplatata: ".format(nedostasuva)))
    kusur1 = doplata - nedostasuva 
    if doplata > nedostasuva:
        print("Vaseto plakanje e zavrseno, vasiot kusur e {} denari".format(kusur1))
        print("Vo vasta korpa gi imate slednite produkti ",produkti)
        break
    elif doplata == nedostasuva:
        print("Sega vVaseto plakanje e zavrseno uspesno")
        print("Vo vasta korpa gi imate slednite produkti ",produkti)
        break
print("Vasta pazaruvanje e uspesno zavrseno vo nasiot market, vi blagodarime")"""