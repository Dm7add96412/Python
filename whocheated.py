# a program which will check the best score of each excercise and if it's returned within the 3 hour time limit from two .csv-files
# returns a dictionary of the results
from datetime import datetime, timedelta
import csv

def viralliset_pisteet():
    
    with open("palautus.csv") as palautus, open("tentin_aloitus.csv") as aloitus:
        koea = {}
        palau = {}
        final = {}
        for rivi in csv.reader(aloitus, delimiter=";"):
            nimi1 = rivi[0]
            aika1 = rivi[1].split(":")
            tunnit1 = int(aika1[0])
            minuutit1 = int(aika1[1])
            start = datetime(2022, 10, 30, tunnit1, minuutit1)
            koea[nimi1] = start

        for alkio in csv.reader(palautus, delimiter=";"):
            nimi = alkio[0]
            teht = alkio[1]
            pisteet = int(alkio[2])
            aika = alkio[3].split(":")
            tunnit = int(aika[0])
            minuutit = int(aika[1])
            stop = datetime(2022, 10, 30, tunnit, minuutit)
            erotus = stop - koea[nimi]
            if erotus.seconds < 10800:
                if nimi not in palau.keys():
                    palau[nimi] = {}
                    palau[nimi][teht] = pisteet
                else:
                    if teht in palau[nimi].keys():                                    
                        if pisteet > palau[nimi][teht]:
                            palau[nimi][teht] = pisteet
                    else:
                        palau[nimi][teht] = pisteet


        for key, value in palau.items():
            piste = 0
            for score in value.values():
                piste += score
            final[key] = piste

    return final

if __name__ == "__main__":
    tulokset = viralliset_pisteet()
    print(tulokset)