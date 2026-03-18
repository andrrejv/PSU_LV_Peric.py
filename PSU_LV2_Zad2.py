U direktoriju PSU_LV/LV2/ nalazi se datoteka mtcars.csv koja sadrži različita mjerenja provedena na 32 automobila (modeli 1973-74).
#  Opis pojedinih varijabli nalazi se u datoteci mtcars_info.txt.
#a) Učitajte datoteku mtcars.csv pomoću:
#data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
#b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp) pomoću naredbe matplotlib.pyplot.scatter.
#c) Na istom grafu prikažite i informaciju o težini pojedinog vozila 
# (npr. veličina točkice neka bude u skladu sa težinom wt).
#d) Izračunajte minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila.
#e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl).

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
mpg = data[:,0]
hp = data[:,3]
wt = data[:,5]
cyl = data[:,1]

#auta sa 6 cyl su na 0,1,3,5,9,10,29

mpg_6_cyl = mpg[cyl==6]


plt.scatter (mpg,hp,s = wt)


plt.xlabel("mpg")
plt.ylabel("hp")
plt.title("ovisnot potrosnje o konjskim snagama")
plt.show()

print(mpg.min())
print(mpg.max())
print(mpg.mean())

print(np.min(mpg_6_cyl))
print(np.max(mpg_6_cyl))
print(np.mean(mpg_6_cyl))
