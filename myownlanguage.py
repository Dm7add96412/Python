# a simple "programming language" with a few simple commands
# returns a list of all the PRINT commands
import string

def suorita(ohjelma):
    tulokset = {}
    lista = []
    kohdat = {}
    i = 0
    n = 0
    
    # first read the PLACES
    while n < len(ohjelma):
        a = ohjelma[n]
        parts = a.split(" ")
        if ":" in parts[0]:
            kohdat[parts[0][0:-1]] = n
        n += 1
  
    # the main program with all the commands
    while i < len(ohjelma):
        alkio = ohjelma[i]
        osat = alkio.split(" ")

        if osat[0] == "END":
            return lista
        elif osat[0] == "MOV":
            if osat[2] in string.ascii_uppercase:
                tulokset[osat[1]] = tulokset[osat[2]]
                i += 1
            else:
                tulokset[osat[1]] = int(osat[2])
                i += 1
        elif osat[0] == "PRINT":
            if len(tulokset) < 1:
                lista.append(0)
                i += 1
            elif len(tulokset) > 0:
                if osat[1] in string.ascii_uppercase:
                    lista.append(tulokset[osat[1]])
                    i += 1
                else:
                    lista.append(int(osat[1]))
                    i += 1
        elif osat[0] == "ADD":
            if osat[1] not in tulokset.keys():
                tulokset[osat[1]] = 0
            if osat[2] in string.ascii_uppercase:
                tulokset[osat[1]] += tulokset[osat[2]]
                i += 1
            else:       
                tulokset[osat[1]] += int(osat[2])
                i += 1
        elif osat[0] == "SUB":
            if osat[2] in string.ascii_uppercase:
                tulokset[osat[1]] -= tulokset[osat[2]]
                i += 1
            else:
                tulokset[osat[1]] -= int(osat[2])
                i += 1
        elif osat[0] == "MUL":
            if osat[2] in string.ascii_uppercase:
                tulokset[osat[1]] *= tulokset[osat[2]]
                i += 1
            else:
                tulokset[osat[1]] *= int(osat[2])
                i += 1
        elif ":" in osat[0]:
            i += 1
        elif osat[0] == "JUMP":
            i = kohdat[osat[1]]
        elif osat[0] == "IF":
            if osat[1] in string.ascii_uppercase:
                eka = tulokset[osat[1]]
            else:
                eka = int(osat[1])
            if osat[3] in string.ascii_uppercase:
                toka = tulokset[osat[3]]
            else:
                toka = int(osat[3])

            if osat[2] == ">":
                if eka > toka:
                    i = kohdat[osat[5]]
                else:
                    i += 1
            elif osat[2] == "<":
                if eka < toka:
                    i = kohdat[osat[5]]
                else:
                    i += 1
            elif osat[2] == ">=":
                if eka >= toka:
                    i = kohdat[osat[5]]
                else:
                    i += 1
            elif osat[2] == "<=":
                if eka <= toka:
                    i = kohdat[osat[5]]
                else:
                    i += 1
            elif osat[2] == "==":
                if eka == toka:
                    i = kohdat[osat[5]]
                else:
                    i += 1
            elif osat[2] == "!=":
                if eka != toka:
                    i = kohdat[osat[5]]
                else:
                    i += 1

    return lista

if __name__ == "__main__":
    ohjelma1 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'alku:', 'MOV B 2', 'MOV Z 0', 'testi:', 'MOV C B', 'uusi:', 'IF C == A JUMP virhe', 'IF C > A JUMP ohi', 'ADD C B', 'JUMP uusi', 'virhe:', 'MOV Z 1', 'JUMP ohi2', 'ohi:', 'ADD B 1', 'IF B < A JUMP testi', 'ohi2:', 'IF Z == 1 JUMP ohi3', 'PRINT A', 'ohi3:', 'ADD A 1', 'IF A <= N JUMP alku']

    tulos = suorita(ohjelma1)
    print(tulos)