import os

ruudustik1 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik2 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik3 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik4 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik5 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik6 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik7 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik8 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik9 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik10 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}

väljakKogu1 = {
    "0" : ruudustik1,
    "1" : ruudustik2,
    "2" : ruudustik3,
    "3" : ruudustik4,
    "4" : ruudustik5,
    "5" : ruudustik6,
    "6" : ruudustik7,
    "7" : ruudustik8,
    "8" : ruudustik9,
    "9" : ruudustik10
}

kõrvaline1 = väljakKogu1.copy()

ruudustik11 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik12 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik13 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik14 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik15 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik16 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik17 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik18 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik19 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik20 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}

väljakKogu2 = {
    "0" : ruudustik11,
    "1" : ruudustik12,
    "2" : ruudustik13,
    "3" : ruudustik14,
    "4" : ruudustik15,
    "5" : ruudustik16,
    "6" : ruudustik17,
    "7" : ruudustik18,
    "8" : ruudustik19,
    "9" : ruudustik20
}

kõrvaline2 = väljakKogu2.copy()

legend1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
legend2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def printVäljak(väljakKogu):
    print (" ", end= "|")
    for x in range (len(legend1)):
        print (legend1[x], end= "|")
    print ("")
    counter = 0
    for x in väljakKogu.values():
        print ("-"*22)
        print (legend2[counter], end= "")
        print ("", end= "|")
        for y in x.values():
            print (y, end= "|")
        print("")
        counter += 1

def paigutus(väljakKogu, rida, asukoht, suurus, horisontaal, suund):
    while True:
        if suund == 1:
            if int(rida) + suurus<10:
                kontroll = laevaPosKontroll(suurus, rida, asukoht, väljakKogu, suund)
                if kontroll == True:
                    for x in range(suurus):
                        horisontaal = väljakKogu[str(int(rida)+x)]
                        horisontaal[asukoht] = 0
                break
        if suund == 2:
            if int(rida) - suurus>=0:
                kontroll = laevaPosKontroll(suurus, rida, asukoht, väljakKogu, suund)
                if kontroll == True:
                    for x in range(suurus):
                        horisontaal = väljakKogu[str(int(rida)-x)]
                        horisontaal[asukoht] = 0
                break
        if suund == 3:
            if int(asukoht) - suurus>0:
                kontroll = laevaPosKontroll(suurus, rida, asukoht, väljakKogu, suund)
                if kontroll == True:
                    for x in range(suurus):
                        horisontaal[str(int(asukoht)-x)] = 0
                break
        if suund == 4:
            if int(asukoht) + suurus<11:
                kontroll = laevaPosKontroll(suurus, rida, asukoht, väljakKogu, suund)
                if kontroll == True:
                    for x in range(suurus):
                        horisontaal[str(int(asukoht)+x)] = 0
                break
        suund = int(input("1=alla, 2=üles, 3=vasak, 4=parem"))


def laevadePaigutamine(väljakKogu):
    printVäljak(väljakKogu)
    outerloop = True
    laevad = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    counter = 0
    while outerloop == True:
        while counter < 10:
            suurus = laevad[counter]
            print ("Paiguta laev, mille suurus on", suurus)
            rida = input("Vali rida")
            asukoht = input("Vali asukoht")
            suund = int(input("1=alla, 2=üles, 3=vasak, 4=parem"))
            try:
                horisontaal = väljakKogu[rida]
            except:
                print ("ei sobi")
                continue
            for x in horisontaal:
                if x == asukoht:
                    while True:
                        if horisontaal[x] == " ":
                            paigutus(väljakKogu, rida, asukoht, suurus, horisontaal, suund)
                            outerloop = False
                            printVäljak(väljakKogu)
                            counter = counter + 1
                            break
                        else:
                            print("siin juba on laev")
    return 20
                        
def rünnak(omaVäljak, vastaseVäljak, elud, kõrvaline):
    outerloop = True
    while outerloop == True and elud>0:
        printVäljak(kõrvaline)
        printVäljak(omaVäljak)
        print ("Mis asukohta ründad")
        rida = input("Vali rida")
        asukoht = input("Vali asukoht")
        try:
            horisontaalVastane = vastaseVäljak[rida]
        except:
            print ("ei sobi")
            continue
        for x in horisontaalVastane:
            if x == asukoht:
                while True:
                    if horisontaalVastane[x] == 0:
                        horisontaalVastane[x] = " "
                        kõrvaline[x] = "+"
                        elud = elud -1
                        uuesti = True
                        break
                    elif horisontaalVastane[x] == " ":
                        kõrvaline[x] = "x"
                        uuesti = False
                        break
        if uuesti == False:
            outerloop = False
    return elud                       

def laevaPosKontroll(suurus, rida, asukoht, väljakKogu, suund):
    kontroll = True
    rida = int(rida)
    asukoht = int(asukoht)
    if suund > 0 and suund < 3:
        for x in väljakKogu:
            counter = 1
            if (rida-(suurus+1) <= int(x) <= rida+1 and suund == 2) or ((rida-1 <= int(x) <= rida+(suurus+1) and suund == 1)):
                ruudustik = väljakKogu[x]
                for y in ruudustik:
                    if asukoht-1 <= int(y) <= asukoht+1:
                        if ruudustik[str(counter)] == 0:
                            print("siin kandis ei ole piisavalt ruumi(1 ruut igas suunas)")
                            kontroll = False
                    counter = counter + 1
    else:
        for x in väljakKogu:
            counter = 1
            if rida-1 <= int(x) <= rida+1:
                ruudustik = väljakKogu[x]
                for y in ruudustik:
                    if (asukoht-(suurus+1) <= int(y) <= asukoht+1 and suund == 4) or ((asukoht-1 <= int(y) <= asukoht+(suurus+1) and suund == 3)):
                        if ruudustik[str(counter)] == 0:
                            print("siin kandis ei ole piisavalt ruumi(1 ruut igas suunas)")
                            kontroll = False
                    counter = counter + 1
    if kontroll == True:
        return True
    else:
        return False

print ("Tere tulemast laevadepommitamise mängu.")
print ("Igal mängijal on kokku kümme laeva.")
print ("Neli ühe ruudulist laeva, kolm kaheruudulist laeva, kaks kolmeruudulist laeva ja üks neljaruuduline laev.")
print ("Laevade paigutamine toimub suurimaist väiksemateni sinu valitud ruutudele.")
print ("\n")
print ("Mängija 1")
elud1 = laevadePaigutamine(väljakKogu1)
os.system('cls' if os.name == 'nt' else 'clear')
print ("\n")
print ("Mängija 2")
elud2 = laevadePaigutamine(väljakKogu2)
os.system('cls' if os.name == 'nt' else 'clear')


while True:
    elud2 = rünnak(väljakKogu1, väljakKogu2, elud2, kõrvaline1)
    os.system('cls' if os.name == 'nt' else 'clear')
    if elud2 == 0:
        print("mängija1 võitis")
        break
    elud1 = rünnak(väljakKogu2, väljakKogu1, elud1, kõrvaline2)
    os.system('cls' if os.name == 'nt' else 'clear')
    if elud1 == 0:
        print("mängija2 võitis")
        break