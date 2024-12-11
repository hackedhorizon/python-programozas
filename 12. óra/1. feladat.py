# 1. feladat - Indexelés
# Határozzuk meg, hogy az első és az utolsó karakter egyezik-e az alábbi szövegben:
zenekar = "aba"

# Ha igen, írjuk ki, hogy "Az első és az utolsó karakter egyezik!"
# Ha nem, írjuk ki , hogy "Az első és az utolsó karakter nem egyezik!"

# Mire lesz szükségünk: 
# - if
# - indexelés

valtozo1 = zenekar[0]    # eltároltuk az első karaktert
valtozo2 = zenekar[-1]   # eltároltuk az utolsó karaktert

if valtozo1 == valtozo2: # megnéztük, hogy egyeznek-e
  print("Az első és az utolsó karakter egyezik!")
else:
  print("Az első és az utolsó karakter nem egyezik!")
