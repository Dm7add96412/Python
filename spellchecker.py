# a simple spell checker which will make suggestions on typos based on a wordlist.txt -file
import difflib

def checker(text):
    words = text.split(" ")
    wordlist = []
    sentence = []
    wlist = []

    with open("wordlist.txt") as thefile:
        for row in thefile:
            wordlist.append(row.strip())
        for word in words:
            if word.lower() in wordlist:
                sentence.append(word)
            else:
                wrong = "*" + word + "*"
                sentence.append(wrong)
                wlist.append(word)
    i = " "
    i = i.join(sentence)
    print(i)
    print("korjausehdotukset:")
    for a in wlist:
        closest = difflib.get_close_matches(a, wordlist)
        j = ", "
        j = j.join(closest)
        print(f"{a}: {j}")


def main():
    text = input("Write text: ")
    checker(text)

main()