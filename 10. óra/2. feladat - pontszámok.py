
"""
  2. feladat:
  Kérjük be a felhasználó nevét és elért pontszámát.
  A pontszám egy 0 és 100 közé eső szám.
  Írjuk ki a nevét és azt, hogy a felhasználó milyen érdemjegyet kapott.

  Pontszámok:
  0-20: 1
  21-40: 2
  41-60: 3
  61-80: 4
  81-100: 5  

"""

nev = input("Add meg a nevedet:")
pontszam = int(input("Add meg a pontszámopdat (0-100):"))
if 0 <= pontszam <= 20:
  print(nev, "erdemjegy = 1")
elif 21 <= pontszam <=40:
  print(nev, "erdemjegy = 2")
elif 41 <= pontszam <=60:
  print(nev, "erdemjegy = 3")
elif 61 <= pontszam <=80:
  print(nev, "erdemjegy = 4")
else :
  print(nev, "erdemjegy = 5")