import random
import time 
import colorama
import os


def dobierz( uzytekarty, karty,znaki):
        
    kartanastosie = random.choice(list(karty)) + " " + random.choice(znaki)

    while kartanastosie in uzytekarty:
        kartanastosie = random.choice(list(karty)) + " " + random.choice(znaki)

    uzytekarty.append(kartanastosie)
    return kartanastosie


def wartosc(zapas, kartywar):
    war = zapas.split()
    if war[0].isnumeric() == False and war[0] != "A":
        return 10
    elif war[0] == "A":
        if kartywar > 10:
            return 1
        else:
            return 11
    else:
        return int(war[0])


colorama.init()

print("888       888                      888         d8b                      888      ")
print("888       888                      888         Y8P                      888      ")
print("888       888                      888                                  888      ")
print("88888b.   888   8888b.   .d8888b   888  888   8888   8888b.    .d8888b  888  888 ")
print("888 `88b  888      `88b  d88P`     888 .88P   `888      `88b  d88P`     888 .88P ")
print("888  888  888  .d888888  888       888888K     888  .d888888  888       888888K  ")
print("888 d88P  888  888  888  Y88b.     888 `88b    888  888  888  Y88b.     888 `88b ")
print("88888P`   888  `Y888888  `Y8888P   888   888   888  `Y888888   `Y8888P  888  888 ")
print("                                               888                               ")
print("                                              d88P                               ")
print("                                            888P`                                ")

input("wcisnij ENTER aby zaczac")

pieniadze = 2500
while True:
    print("masz: ", pieniadze, " zlotych")
    stawka = int(input("podaj stawke:  "))

    while stawka > pieniadze:
        stawka = int(input("podaj prawidlowa stawke:  "))

    print("stawka wynosi: ", stawka, "\n")

    kartygracz = ""
    kartygraczwar = 0
    kartykomp = ""
    kartykompwar = 0



    karty = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "K": 10,
        "Q": 10,
    }

    znaki = ["trefl", "karo", "pik", "kier"]

    uzytekarty = []


    for i in range(2):
        zapas = dobierz(uzytekarty,karty,znaki)
        kartygraczwar +=  wartosc(zapas,kartygraczwar)
        kartygracz += zapas + " "
       


    zapas = dobierz(uzytekarty,karty,znaki)
    kartykompwar +=  wartosc(zapas,kartykompwar)
    kartykomp += zapas + " "

    print(colorama.Fore.CYAN + "karty komputera to: ", kartykomp)
    print( colorama.Fore.CYAN + "wartosc kart komputera: ", kartykompwar , "\n")
    print(colorama.Fore.MAGENTA + "twoje karty to: ", kartygracz)
    print(colorama.Fore.MAGENTA  +"wartosc twoich kart: ", kartygraczwar , "\n")
    if kartygraczwar != 21:
        hitstand = str(input(colorama.Fore.WHITE + "Hit-ujesz czy Stand-ujesz? H/S \n"))
        while hitstand.upper() != "S":
            zapas = dobierz(uzytekarty,karty,znaki)
            kartygraczwar +=  wartosc(zapas,kartygraczwar)
            kartygracz += zapas + " "

            print(colorama.Fore.MAGENTA + "twoje karty to: ", kartygracz)
            print(colorama.Fore.MAGENTA + "wartosc twoich kart wynosi: ", kartygraczwar)

            if kartygraczwar > 21:
                break
                
            if kartygraczwar == 21:
                break

            hitstand = str(input(colorama.Fore.WHITE + "Hit-ujesz czy Stand-ujesz? H/S \n" ))

    if kartygraczwar > 21:
        print("")
    elif kartygraczwar == 21:
        print("")
    else:

        while kartykompwar < 17 and kartykompwar<kartygraczwar:
            zapas = dobierz(uzytekarty,karty,znaki)
            kartykompwar +=  wartosc(zapas,kartykompwar)
            kartykomp += zapas + " "

            print(colorama.Fore.CYAN +"karty komputera to: ", kartykomp)
            print(colorama.Fore.CYAN +"wartosc kart komputera wynosi: ", kartykompwar)
            time.sleep(2)

            if kartykompwar > 21:
                break

            print(colorama.Fore.MAGENTA +"wartosc twoich kart:" , kartygraczwar)


    if kartykompwar < 17 and kartygraczwar > 21:
        print(colorama.Fore.CYAN +"wartosc kart komputera:" , kartykompwar)
        print(colorama.Fore.MAGENTA +"wartosc twoich kart:" , kartygraczwar)

    if kartykompwar > 21:
        print(colorama.Fore.GREEN + 'Wygrales! Komputer przekroczył 21.')
        pieniadze += stawka
    elif kartygraczwar == 21 and kartykompwar!= 21:
        print(colorama.Fore.GREEN +'Wygrales! Masz Blackjacka!')
        pieniadze += stawka
    elif kartykompwar > kartygraczwar and kartykompwar <21  or kartykompwar <= 21 and kartygraczwar > 21 or kartykompwar == 21 and kartygraczwar<21:
        print(colorama.Fore.RED +'Przegrales. Komputer ma lepsze karty.')
        pieniadze -= stawka  
    elif kartykompwar < kartygraczwar and kartygraczwar <21 or kartygraczwar <= 21 and kartykompwar > 21 or kartygraczwar == 21 and kartykompwar<21:
        print(colorama.Fore.GREEN +'Wygrales! Masz lepsze karty.')
        pieniadze += stawka

    else:
        print(colorama.Fore.YELLOW+'Remis! Oboje macie takie same karty.')

    time.sleep(4)
    os.system('cls')

    print(colorama.Fore.WHITE + "masz: ",pieniadze," zl")

    if pieniadze != 0:
        gracdalej = input("Czy chcesz grac dalel?? T/N ")
        if gracdalej.upper() == "T":
            continue
        else: 
            print("Dziekujemy za gre!!!")
            break
    else:
        print("Nie masz juz pieniedzy")
        break
colorama.deinit()