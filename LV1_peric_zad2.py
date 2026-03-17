#Zadatak 2
#Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i 1.0.
#  Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F


while True:
    try:
        ocjena = float(input("Unesite broj izmedju 0.0 i 1.0: "))
        if 0.0 <= ocjena <=1.0:
            print(f"Unijeli ste: {ocjena}")
            break
        else:
            print("Ocjena mora biti izmedju 0.0 i 1.0")
    except ValueError:  
            print("nije broj")

if  0.9<= ocjena <=1:
     znak = "A"
elif 0.8 <= ocjena < 9 :
     znak = "B"
elif  0.7<= ocjena <8 :
     znak = "C"
elif  0.6<= ocjena < 7:
     znak = "D"
elif   ocjena <6 :
     znak =  "F"

print(f"Oznaka za {ocjena} je : {znak}")
