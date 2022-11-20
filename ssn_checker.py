# social security number checker
from datetime import datetime
def onko_validi(hetu: str):

    paiva = int(hetu[0:2])
    kk = int(hetu[2:4])
    vuosi = int(hetu[4:6])
    merkit = "-+A"
    numero = ""
    test = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if len(hetu) != 11:
        return False
    
    if paiva > 0 and paiva <= 31:     
        if kk > 0 and kk <= 12:  
            if hetu[6] == "A":
                if vuosi >= 0 and vuosi <= 22:
                    eka = True
            elif vuosi > 0 and vuosi <= 99:
                eka = True
            else:
                eka = False
        else:
            eka = False
    else:
        eka = False

    for i in range(len(hetu) - 1):
        alkio = hetu[i]
        if alkio in merkit:
            continue
        numero += alkio
    num = int(numero)
    jako = num % 31

    if test[jako] == hetu[len(hetu) - 1]:
        tarkiste = True
    else:
        tarkiste = False

    if eka is True and tarkiste is True:
        return True
    else:
        return False

if __name__ == "__main__":
    print(onko_validi("112233-0001"))