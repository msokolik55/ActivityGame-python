# na to, aby sme mohli pouzivat nahodne cisla, musime ho najskor pripojit
import random


def activity():
    # na zaciatku zadame, ze chceme hrat a nastavime 1.kolo
    pokracovanie = "ano"
    kolo = 1

    # jednotlive cinnosti budeme volat v cykle podla ich indexov
    cinnosti = ["kreslenie", "slovny popis", "pantomima", "zvuk", "free style"]

    # zadame pocet hracov, nasledne ich mena na dalsie pouzitie
    pocet_hracov = input("Pocet hracov: ")
    mena_hracov = []
    for i in range(int(pocet_hracov)):
        mena_hracov.append(input("Meno hraca c." + str(i + 1) + ": "))
    print()

    # pokym budeme chciet pokracovat v nasej hre, budu sa generovat aktivity
    while pokracovanie != "nie":

        # vypise sa poradove cislo kola
        print(str(kolo) + ".kolo\n")

        # kazdemu hracovi sa priradi nahodna aktivita
        for i in range(int(pocet_hracov)):
            print("Na rade je hrac " + mena_hracov[i % int(pocet_hracov)])

            # na zaciatku sa vyberie nahodne cislo a potom vypise aktivita
            vyber = random.randrange(len(cinnosti))
            print("* " + cinnosti[vyber] + " *\n")
            input()

        # opytame sa hracov, ci chcu pokracovat a podla toho cyklus pokracuje
        print("Chcete pokracovat dalej? [ano/nie]")
        pokracovanie = input()
        kolo += 1
        print("\n")

    # na konci vratime slovnu formulku
    return "Dakujeme za hru."

print(activity())
