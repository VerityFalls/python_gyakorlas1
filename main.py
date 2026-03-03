lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)
del lista[1]
print(lista)
del lista[0]
print(lista)
del lista[-1]
print(lista)
del lista[2:4]
print(lista)

def szamlalo():
    for i in range(3):
        yield i


for szam in szamlalo():
    print(szam)



lista = ["a", "b", "c"]

for index, ertek in enumerate(lista):
    print(index, ertek)


lista = [1, 2, 3]

lista.append(4)
print(lista)
lista.insert(1, 10)
print(lista)
lista.remove(2)
print(lista)
elem = lista.pop()
print("Kivett elem: " + str(elem))
print("Lista: " + str(lista))
lista.sort()
for i in range(5):
    if i == 2:
        continue
    print(i)

# ez egy komment

"""
tobbsoros
komment
"""

s = "Hello"

print(s + " World")
print(s * 2)
print(len(s))
print(s.upper())
print(s.replace("H", "J"))
print("H" in s)



s = "programozas"

s = "programozas, a ram memoria es a processzor hasznalata"

print("ram" in s)  # tagságvizsgálat
print(s.find("ram"))  # első előfordulás indexe
print(s.rfind("ram"))  # utolsó előfordulás indexe
print(s.count("ram"))  # előfordulások száma

print("nincs benne" in s)  # tagságvizsgálat
print(s.find("nincs benne"))  # első előfordulás indexe
print(s.rfind("nincs benne"))  # utolsó előfordulás indexe
print(s.count("nincs benne"))  # előfordulások száma



elemek = ["A", "kedvenc", "ételem", "a", "pizza", "."]
print(elemek)
print(" ".join(elemek))
print("_".join(elemek))
print(",".join(elemek))
print(" amúgy ".join(elemek))


# szeleteléssel
forditott = s[::-1]
print(forditott)

# listává alakítással
lista = list(s)
lista.reverse()
print("".join(lista))
x = 10
print(x)
x = 30
print(x)
y = 1.5456
print(y)
nev  = "Valaki"
print(nev)

print([1,2, 3,4,5])

print("hello" + " world")
print(12)
print("hello" + str(12))
print(f"hello {12} {nev}")

tuple_szamok = (2,4)

print(f"szamok: { (1,2,5,7) }, tuple_szamok: {tuple_szamok}")
print("tuple szamok:" + str(tuple_szamok))

print(range(5))

lista = [1,1,1,1,1,3,3,4]
print(lista)
halmaz = {1,1,1,1,1,3,3,4}
print(halmaz)
szotar = {"név": "Anna", "kor": 20}
print(szotar)
logikai = False
print(logikai)

ertek = None
print(ertek)

szam1 = 11

nev = "Jani"
Nev = "Jozsi"

print(nev + " es " + Nev + " baratok")

PI = 3.14

print(PI)

print( 1.5 + 2 * 3 - 4 / 2 + 0.5)
print( 2 + 2 * 3 - 2 )

x = 5
y = 4

print("x mod y: " + str(x % y))


print ("Három az értéke y-nak? " + str(y) == 3)
print ("Három az értéke y-nak? 3" == 3)
print ("Három az értéke y-nak? 3" == "Három az értéke y-nak? 3")

print ("Három az értéke y-nak? " + str(y == 3))
print ("Nem három az értéke y-nak? " + str(y != 3))
print ("Y kisebb mint 3 " + str(y < 3))
print ("Y kisebb vagy egyenlő mint 3 " + str(y <= 3))

print ("Y kisebb vagy egyenlő mint 3 " + str(y < 3 or y == 3))

if y > 5:
    print("y nagyobb mint 5")
    if y % 2 == 0:
        print("y páros és nagyobb mint 5")
else:
    print("y kisebb vagy egyenlő mint 5")

for i in range(5):
    print(i)

for nev in ["Anna", "Jani", "Jozsi"]:
    print(nev)
    if nev == "Anna":
        print("Szia Anna!")

print ("vege")

while y < 10:
    print("y még kisebb mint 10")
    y = (y + 1)
    print("y értéke: " + str(y))


def fuggveny():
    print("Ez egy függvény")

    return "Alma"

print("kovetkezo sor")

fuggveny()
fuggveny()

eredmeny = fuggveny()
print( " A fuggveny vissszaadott egy " + eredmeny + "-t")

def osszead( a, b):
    osszeg = a + b
    return osszeg


eredmeny = str(osszead( 1, 2))
print("Osszeg v1:" + eredmeny)

print("Osszeg v2:" + str(osszead(3,4)))

