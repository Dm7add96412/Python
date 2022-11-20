# city bike station coordinates and distances
# reads station details from .csv-file and calculates distances
import math

# station details: name and coordinates
def hae_asematiedot(tiedosto: str):
    with open(tiedosto) as tiedot:
        tietoja = {}
        for rivi in tiedot:
            rivi = rivi.replace("\n", "")
            uusirivi = rivi.split(";")
            if uusirivi[0] == "Longitude":
                continue
            koordinaatit = (float(uusirivi[0]), float(uusirivi[1]))
            tietoja[uusirivi[3]] = koordinaatit
    return tietoja

# station distances
def etaisyys(asemat: dict, asema1: str, asema2: str):
    x_kilometreina = (asemat[asema1][0] - asemat[asema2][0]) * 55.26
    y_kilometreina = (asemat[asema1][1] - asemat[asema2][1]) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    return etaisyys

# the longest distance
def suurin_etaisyys(asemat):
    stations = []
    i = 0
    pisin = -1
    for key in asemat.keys():
        stations.append(key)
    for key in asemat.keys():
        for alkio in stations:
            matka = etaisyys(asemat, key, alkio)
            if matka >= pisin:
                pisin = matka
                palautus = (key, alkio, pisin)
            else:
                continue
    return palautus

def main():
    asemat = hae_asematiedot("stations1.csv")
    e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
    print(e)
    e = etaisyys(asemat, "Viiskulma", "Kaivopuisto")
    print(e)
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)

if __name__ == "__main__":
    main()