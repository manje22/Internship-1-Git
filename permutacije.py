'''
Korisnik unosi niz cijelih brojeva. Zadatak je generirati i ispisati sve moguće permutacije tog niza cijelih brojeva korištenjem rekurzije.

	Ulazni podaci:
Korisnik unosi niz cijelih brojeva, odvojenih razmacima.

Izlazni podaci:
Ispisati sve moguće permutacije niza cijelih brojeva.

'''

unos = input("Unesite niz brojeva").split(" ")

def permutacija(unos):
    #bazni slucaj
    if len(unos) == 1:
        return unos
    
    perms = permutacija(unos[1:])
    char = unos[0]
    rez = []
    for perm in perms:
        for i in range(len(perm)+1):
            rez.append(perm[:i] + char + perm[i:])

    return rez

for r in permutacija(unos):
    print(r)
