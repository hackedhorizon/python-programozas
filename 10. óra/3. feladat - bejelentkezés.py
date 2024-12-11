
"""
    3. feladat - bejelentkezés

    Kérjük be a felhasználónevet és jelszót, majd írjuk ki, hogy sikeres bejelentkezés, 
    ha a felhasználónév az "admin" és a jelszó "123456" lesz. 
    
    Minden más esetben, írjuk ki, hogy "sikertelen" bejelentkezés.

"""

felhasznalonev = input("Kérlek, add meg a felhasználóneved: ")
jelszo = input("Kérlek, add meg a jelszavadat")

if felhasznalonev == "admin" and jelszo == "123456":
  print ("Sikeres bejelentkezés")
else:
  print ("Sikertelen bejelentkezés.")