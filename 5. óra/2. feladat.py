# not(valtozo)          # ellenkezőjét írjuk ki -> not utasítás
# valtozo1 and valtozo2 # akkor ad igaz eredményt, ha mindkét változó igaz


megcsinaltamAHazit = False
Kitakaritottame    = True

kimehetunkeJatszani = megcsinaltamAHazit and Kitakaritottame

print(kimehetunkeJatszani)



# or másnéven vagy

A = True
B = True

print(not(A) or not(B))



A = True
B = True
C = A ^ B

print(C)







# megyekAngolra    = True
# vanETanulniValom = True
#
# mehetekEFocizni = not(megyekAngolra and vanETanulniValom)
#
# print(mehetekEFocizni)



# and
A = True
B = True

C = A and B

print(C)

# or
A = False
B = False

C = A or B

print(C)

A = True
C = not(A)


haziKesz      = True
hazimunkaKesz = False

mehetekEBulizni = haziKesz or hazimunkaKesz

print(mehetekEBulizni)