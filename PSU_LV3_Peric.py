#Zadatak 1
#Za mtcars skup podataka napišite programski kod koji će odgovoriti na sljedeća pitanja:
#1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
#2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
#3. Kolika je srednja potrošnja automobila sa 6 cilindara?
#4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
#5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
#6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
#7. Kolika je masa svakog automobila u kilogramima?


import pandas as pd
import numpy as np


mtcars = pd.read_csv("mtcars.csv")

print(mtcars)

top5_potrosnja = mtcars.sort_values(by="mpg" , ascending = True).head(5)

print(top5_potrosnja)

cars_8 = mtcars[mtcars.cyl == 8]

top3_potrosnja = cars_8.sort_values(by="mpg" , ascending = False).head(3)

print(top3_potrosnja)

cars_6 = mtcars[mtcars.cyl == 6]

cars_6_potrosnja = cars_6.sort_values(by = "mpg")

print(cars_6_potrosnja)


#4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?


cars_4_wt = mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)]

cars_4_wt_mpg = cars_4_wt.sort_values(by = "mpg")

print(cars_4_wt_mpg)

#5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?

mt_cars_am = mtcars[mtcars.am == True]

print(mt_cars_am)

#6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?


mt_cars_am_hp = mt_cars_am[mtcars.hp > 100]

print(mt_cars_am_hp)

#7. Kolika je masa svakog automobila u kilogramima?
mtcars['Masa_u_kg'] = mtcars.wt *  0.45359237

print(mtcars.Masa_u_kg
