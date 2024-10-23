












"""
    Vannak összehasonlító operátoraink is. Lásd 6.sortól.
    Mindig balról jobbra haladunk amikor kiértékelünk valamit

        <   kisebb, mint            Pl: 1 <  2 ? igaz
        >   nagyobb, mint           Pl: 1 >  2 ? hamis
        ==  egyenlő-e               Pl: 1 == 2 ? hamis
        !=  nem egyenlő             Pl: 1 != 2 ? igaz
        >=  nagyobb, vagy egyenlő   Pl: 1 >= 2 ? hamis
                                    Pl: 3 >= 2 ? igaz
        <=  kisebb, vagy egyenlő    Pl: 1 <= 2 ? igaz
                                    Pl: 2 <= 2 ? igaz

    Mivel ezek logikai műveletek, ezért mindig Igaz / Hamis lesz a kapott "válasz" (visszatérési érték).
"""


# Nézzük meg, hogy a szam_1 kisebb-e, mint a szam_2!
print(szam_1 < szam_2)

# Nézzük meg, hogy a szam_2 nagyobb-e, mint a szam_1
print(szam_2 > szam_1)

szam1 = 5
szam2 = 10
print(szam1 < szam2)
print(szam1 > szam2)
print(szam1 == szam2)

szam1 = input("Kérem az elso számot.")
szam2 = input("Kérem a masodik szamot")
print("banán" != "alma")

szam_1 = 5
szam_2 = 6
