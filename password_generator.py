# password generator
# numero = length of the password
# if valinta1 = True, a number is included in the password
# if valinta2 = True, a special character is included in the password
import string 
from random import *

def luo_hyva_salasana(numero: int, valinta1: bool, valinta2: bool):
    salsasana = ""
    erikoismerkit = "!?=+-()#"
    if valinta1 is True and valinta2 is False:
        i = string.ascii_lowercase + string.digits
        salasana = sample(i, numero)
        if erikoismerkit not in salasana:
            salasana[randint(0, (numero - 1))] = choice(string.digits)
    elif valinta2 is True and valinta1 is False:
        i = string.ascii_lowercase + erikoismerkit
        salasana = sample(i, numero)
        if erikoismerkit not in salasana:
            salasana[randint(0, (numero - 1))] = choice(erikoismerkit)
    elif valinta1 is True and valinta2 is True:
        i = string.ascii_lowercase + string.digits + erikoismerkit
        salasana = sample(i, numero)
        if erikoismerkit not in salasana:
            salasana[randint(0, (numero - 1))] = choice(erikoismerkit)
        if erikoismerkit not in salasana:
            salasana[randint(0, (numero - 1))] = choice(string.digits)
        
    else:
        salasana = sample(string.ascii_lowercase, numero)

    for alkio in salasana:
        salsasana += alkio

    return salsasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_hyva_salasana(5, True, True))