"""
    1. feladat - Páros szám vizsgálata
    
    Kérjünk be egy számot, és döntsük el, hogy páros-e vagy sem.

    Ha van egy számod, ami maradék nélkül osztható kettővel, akkor a szám páros

    Maradékos osztás: % jel. pl 5 % 2 (5 maradékosan osztva 2-vel)

"""


szam = int(input("Adj meg egy számot"))
if szam % 2 == 0:
  print("A szám páros")
else:
  print("A szám páratlan")