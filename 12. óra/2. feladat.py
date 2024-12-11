
# 2. feladat:
# Módosítsuk az első feladatot úgy, hogy a felhasználótól kérjük be a feladatot!
valtozo1 = input("Adjon meg egy tetszőleges szót: ")
valtozo2 = valtozo1[0]
valtozo3 = valtozo1[-1]

if valtozo2 == valtozo3: # megnéztük, hogy egyeznek-e
  print("Az első és az utolsó karakter egyezik!")
else:
  print("Az első és az utolsó karakter nem egyezik!")
