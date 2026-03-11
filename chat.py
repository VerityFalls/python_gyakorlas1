
def feldolgozas(kerdes):
    print("feldolgozas alatt: " + kerdes)

    szamjegyek = dict()
    for betu in kerdes:
        if betu in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if betu in szamjegyek:
                szamjegyek[betu] += 1
            else:
                szamjegyek[betu] = 1

    if kerdes.endswith("?"):
        print("Ez bizony egy kérdés")

    if len(szamjegyek) == 0:
        print("Ebben egy számjegy se volt")

    print(f"A kerdes {kerdes.count('.')} darab pontot tartalmaz")

    return szamjegyek


while True:
    kerdes = input("Kerdes: ")

    if kerdes == "exit" or kerdes == "quit":
        print("Bye!")
        break

    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)

    print("Válasz: " + str(valasz))

print("VEGE.")
