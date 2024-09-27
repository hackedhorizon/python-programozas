"""
    1. feladat - Változók létrehozása

    - hozz létre egy "nevem" nevű változót, az értéke legyen a saját neved!
    - hozz létre egy "korom" nevű változót, az értéke legyen az életkorod!
    - írasd ki a változókat a képernyőre!
"""

"""
    2. feladat - Változók módosítása
    
        - hozz létre egy szam nevű változót, értéke legyen 100 (szám adattípus, nem kell macskaköröm "")
        - írasd ki a képernyőre
        - módosítsd a tartalmát 50-re és írasd ki újra!

        A képernyőn futtatás után a következőt kell látnod:

        100
        50
        Process finished with exit code 0
"""

"""
    3. feladat (inkább kis tananyag): Szöveg és változó kiíratása egyszerre a képernyőre
    
    Objektív: ki akarjuk írni a képernyőre, hogy "15 darab almát ettem ma."
    
    Ezt megtehetnénk akár így is:
    print("15 darab almát ettem ma")
    
    Viszont, mi azt szeretnénk, hogy a szám a szövegben változtatható legyen.
    
    Ehhez természetesen először egy változóra van szükségünk:
    darabszam = 15 
    
    Másodszor, valahogy bele kéne rakni a kiírandó szövegbe ennek
    a változónak a tartalmát.
    
    Ezt két módon tehetjük meg:
    - print(str(darabszam) + "darab almát ettem ma")
    - print(f"{darabszam} darab almát ettem ma")

    Mindkettő módszerrel ugyanazt érjük el.
    A legelső módszer fogja a "darabszam" nevű változót, majd kiolvassa az értékét.
    A python minden esetben összeadásként akarja értelmezni a plusz(+) karaktert.
    Mivel ez egy szám, és utána egy plusz(+) karakter van, ezért össze akarja adni
    a mellette lévő szöveggel.
    
    Ez természetesen butaság, hiszen számot nem adhatunk össze szöveggel.
    Ezért ahhoz, hogy a darabszam változóban tárolt értéket szövegként értelmezze
    és ezáltal ne összeadásnak fogja fel a print a "+" karaktert, át kell alakítanunk
    a kiolvasott értéket szöveggé.
    
    Egy változóból kiolvasott szám értéket az str(valtozoNeve)
    utasítással alakíthatunk át szöveg értékké.
"""
# Például:
szamTipusuValtozo = 1
print(szamTipusuValtozo + 6) # ez így teljesen korrekt, veszi az 1-et hozzáad 6-ot és kiírja.

# De mi van akkor, ha a 6 helyett azt akarom odaírni, hogy "darab"?
print(szamTipusuValtozo + "darab") # Nem fog lefutni, mert a + karaktert összeadásként fogja fel.

# Ezért a szamTipusuValtozo-t valahogy át kéne alakítani úgy, hogy a benne lévő 1(mint szám) az "1" (mint szöveg) legyen
# Erre való az str(valtozo) utasítás:
print(str(szamTipusuValtozo) + "darab")

# Ezeknek tudatában oldjuk meg az eredeti feladatot:
# Írjuk ki a képernyőre, hogy "x darab almát ettem ma."
# Az x legyen a változó neve, a kezdőértéke bármennyi lehet:)