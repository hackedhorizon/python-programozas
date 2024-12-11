"""
    
    Indexelés 

    Az indexelés segítségével kivehetünk egy szövegből egy megadott karaktert, vagy akár hivatkozhatunk is rá.

"""

# Például, hozzunk létre egy változót
valtozo = "mondat"

# Ha kiíratjuk, megkapjuk, hogy "mondat"
print(valtozo)

# Azonban van lehetőségünk arra is, hogy kiírjuk az első karakterét is.
# A programozásban ha "első" elemről beszélünk, azt mindig 0-val írjuk.
# Tehát valaminek a nulladik eleme az valójában az az elem, amit mi emberi nyelven első elemként értelmezünk.

print(valtozo[0]) # Kapcsos zárójelek között megadhatjuk, hányadik elemet akarjuk kiíratni a változóból -> ez lesz az "m" betű
print(valtozo[1]) # o betű
print(valtozo[2]) # n betű
print(valtozo[3]) # d betű
print(valtozo[4]) # a betű
print(valtozo[5]) # t betű

# Mi van akkor, ha a hatodik helyen lévő karaktert akarjuk kiíratni?
# Hiba üzenetet fogunk kapni!

# print(valtozo[6]) # Hibaüzenet a következő lesz: "index out of range"
# Magyarul ez azt jelenti, hogy az indexünk (a hely amire hivatkozunk), tartományon kívűlre esik
# Tehát, a hatodik helyen gyakorlatilag nincs mit kiíratni, mert nem létezik. 


"""
    Elágazások és indexelés

    Lehetőségünk van összekapcsolni az eddig megtanult elágazást az indexeléssel.

    (Meg úgy bármit, mindent mindennel, amit eddig tanultunk :D)
"""

# Például megvizsgálhatjuk, hogy a "macska" szóból, a harmadik elem az megegyezik-e egy "s" betűvel:

if "macska" == 's':
    print("Igen, ebben a szóban a harmadik karakter egy s betű.")

# De akár egy külön változó létrehozásával is megtehetjük ezt.

allat = "macska"
if allat[3] == 's':
  print("✔")

# Ha szeretnénk például megcserélni egy változó első és utolsó karakterét:
valtozo = "kocsi"
valtozoCserelt = valtozo[4] + valtozo[1] + valtozo[2] + valtozo[3] + valtozo[0]
print(valtozoCserelt)


# Vagy akár közvetlenül is kiírathatjuk:
print(valtozo[4], valtozo[1], valtozo[2], valtozo[3], valtozo[0])

# Kiírathatunk akár 0-3 ig minden egyes karaktert is:
print(valtozo[0:3])
