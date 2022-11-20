# a simple dictionary which saves data to a sanakirja.txt -file
def lisaa_sana(suomi: str, enkku: str, kirja: list):
    kirja.append((suomi, enkku))
    with open("sanakirja.txt", "w") as tiedosto:
        for rivi in kirja:
            tiedosto.write(f"{rivi[0]};{rivi[1]}\n")

def hae_sana(haku: str, sanakirja: list):
    for rivi in sanakirja:
        for alkio in rivi:
            if haku in alkio:
                print(f"{rivi[0]} - {rivi[1]}")

def main():
    while True:
        rivit = []
        with open("sanakirja.txt") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.strip()
                osat = rivi.split(";")
                rivit.append((osat[0], osat[1]))
        print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
        valinta = int(input("Valinta: "))
        # EXIT
        if valinta == 3:
            print("Moi!")
            break
        # ADD
        elif valinta == 1:
            suomeksi = input("Anna sana suomeksi: ")
            enkuksi = input("Anna sana englanniksi: ")
            lisaa_sana(suomeksi, enkuksi, rivit)
            print("Sanapari lisätty")
        # SEARCH
        elif valinta == 2:
            hakusana = input("Anna sana: ")
            hae_sana(hakusana, rivit)

main()