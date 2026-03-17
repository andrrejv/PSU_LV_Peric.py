#Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. 
# Koristite ugrađenu Python metodu input(). 
# Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran.
#  Na kraju prepravite rješenje na način da ukupni iznos izračunavate 
# u zasebnoj funkciji naziva total_euro.


def total_euro(radni_sati, satnica):
    total_euro = radni_sati * satnica

    return total_euro


radni_sati = int(input("Unesite broj radnih sati :"))
satnica = float(input("Unesite kolika je satnica :"))


placa = radni_sati * satnica

print(f"{placa}")

print(total_euro(radni_sati, satnica))
