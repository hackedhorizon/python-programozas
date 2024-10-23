"""
    1. Feladat:
    Egy gyermek csak akkor játszhat videójátékokkal, ha mind a
    házi feladatát megcsinálta, mind a szobáját kitakarította.

    Írd meg a kódot, amely megvizsgálja, hogy a gyermek játszhat-e
    A változókat így nevezd el:
        - hazifeladatkesz
        - kitakaritottame
"""
hazifeladatkesz = True
kitakaritottame = True
jatszatok = hazifeladatkesz and kitakaritottame
print(jatszatok)


"""
    2. Feladat:
    Egy baráti társaság akkor megy sétálni, ha NEM esik az eső, VAGY van esernyőjük.
    Írj egy programot, amely eldönti, hogy elindulnak-e sétálni,
    ha az esikAzEso és vanEsernyo változók adott értékeket vesznek fel!
"""
esikAzEso = True
vanEsernyo = False
setalas = not esikAzEso or vanEsernyo
print(setalas)


"""
    3. Feladat: Egy diák akkor mehet el kirándulni a hétvégén,
    ha készült a vizsgájára vagy a tanára megengedte neki.
    Készíts egy programot, amely eldönti, hogy elmehet-e a diák kirándulni,
    ha az készultemAVizsgara és megengedteATanar változók adott értékeket kapnak!
"""
készultemAVizsgara = True
megengedteATanar = False
kirandulhat = készultemAVizsgara or megengedteATanar
print(kirandulhat)