# reads course results from 4 different files, calculates results and saves them to tulos.csv and tulos.txt files

def nimet(opiskelijatiedot1):
    nimet = {}
    with open(opiskelijatiedot1) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if osat[0] == "opnro":
                continue
            nimet[osat[0]] = osat[1] + " " + osat[2]
    return nimet

def tehtavatietoja(tehtavientiedot):
    sortatut = {}
    with open(tehtavientiedot) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if osat[0] == "opnro":
                continue
            sortatut[osat[0]] = []
            for arvosana in osat[1:]:
                sortatut[osat[0]].append(int(arvosana))
    return sortatut

def koepisteet(kpisteet):
    ktulokset = {}
    with open(kpisteet) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if osat[0] == "opnro":
                continue
            ktulokset[osat[0]] = []
            for pisteet in osat[1:]:
                ktulokset[osat[0]].append(int(pisteet))
    return ktulokset

def asanat(opisktiedot, tehtavtiedot, kptulokset, kurssitiedot):
    arvosanat = {}
    yhtpist = {}
    lkm = {}
    tehpist = {}
    koepist = {}

    n = "nimi"
    t = "teht_lkm"
    t2 = "teht_pist"
    k = "koe_pist"
    y = "yht_pist"
    a = "arvosana"
    space = " "
    open('tulos.csv', 'w').close()

    with open(kurssitiedot) as tiedot, open("tulos.txt", "w") as tulokset:
        merkki = "="
        for rivi in tiedot:
            osat = rivi.split(": ")
            if osat[0] == "nimi":
                nimi = osat[1]
                nimi = nimi.strip()
            if osat[0] == "laajuus opintopisteina":
                opisteet = osat[1]
                opisteet = opisteet.strip()
        lopputulos = (f"{nimi}, {opisteet} opintopistettä")
        tulokset.write(f"{lopputulos}\n")
        tulokset.write(f"{merkki * len(lopputulos)}\n")
        tulokset.write(f"{n:30}{t:10}{t2:10}{k:10}{y:10}{a:10}\n")

    for opisknumero, nimi in opisktiedot.items():
        if opisknumero in tehtavtiedot:
            summa = 0
            yhteensa = 0
            for alkio in tehtavtiedot[opisknumero]:
                summa += alkio
            if summa < 4:
                ppisteet = 0
            elif summa >= 4 and summa < 8:
                ppisteet = 1
            elif summa >= 8 and summa < 12:
                ppisteet = 2
            elif summa >= 12 and summa < 16:
                ppisteet = 3
            elif summa >= 16 and summa < 20:
                ppisteet = 4
            elif summa >= 20 and summa < 24:
                ppisteet = 5
            elif summa >= 24 and summa < 28:
                ppisteet = 6
            elif summa >= 28 and summa < 32:
                ppisteet = 7
            elif summa >= 32 and summa < 36:
                ppisteet = 8
            elif summa >= 36 and summa < 40:
                ppisteet = 9
            elif summa >= 40:
                ppisteet = 10

            for tulos in kptulokset[opisknumero]:
                yhteensa += tulos
            kokon = yhteensa + ppisteet

            if kokon < 15:
                arvosana = 0
            elif kokon >= 15 and kokon < 18:
                arvosana = 1
            elif kokon >= 18 and kokon < 21:
                arvosana = 2
            elif kokon >= 21 and kokon < 24:
                arvosana = 3
            elif kokon >= 24 and kokon < 28:
                arvosana = 4
            elif kokon > 27:
                arvosana = 5
            
            arvosanat[nimi] = arvosana
            yhtpist[nimi] = kokon
            lkm[nimi] = summa
            tehpist[nimi] = ppisteet
            koepist[nimi] = yhteensa

            with open("tulos.txt", "a") as tulokset:
                tulokset.write(f"{nimi.strip():30}{summa:<10}{ppisteet:<10}{yhteensa:<10}{kokon:<10}{arvosana}\n")
            with open("tulos.csv", "a") as tulokset:
                tulokset.write(f"{opisknumero};{nimi.strip()};{arvosana}\n")

        else:
            print("ei löydy")


def main():
    if False:
        # input values
        opiskelijatiedot = input("Opiskelijatiedot: ")
        tehtavatiedot = input("Tehtävätiedot: ")
        pisteetkoe = input("Koepisteet: ")
        kurssitiedot = input("kurssin tiedot: ")
    else:
        # for testing
        opiskelijatiedot = "opiskelijat1.csv"
        tehtavatiedot = "tehtavat1.csv"
        pisteetkoe = "koepisteet1.csv"
        kurssitiedot = "kurssi1.txt"
    
    opiskelijat = nimet(opiskelijatiedot)
    tehtavat = tehtavatietoja(tehtavatiedot)
    pisteet = koepisteet(pisteetkoe)
    asanat(opiskelijat, tehtavat, pisteet, kurssitiedot)

main()