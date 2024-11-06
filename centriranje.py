def centriranje(duljina, red):
    prostor = duljina - len(red)
    lijevo_p = prostor // 2
    desno_p = prostor - lijevo_p
    return " "*lijevo_p + red + " "*desno_p



m = int(input("Unestie maksimalan broj znakova po liniji: "))

n = 0
while True:
    n = int(input("Unesite duzinu linije, nesmije biti kraca od m: "))
    if n >= m:
        break
tekst = ""

while True:
    x  = input("Unesite liniju teksta ili prazan string kad ste gotovi: \n")
    if len(x) == 0:
        break
    else:
        if(len(tekst)):
            tekst = tekst + " " + x
        else:
            tekst += x
        

redovi = []
nizTekst = tekst.split()
trenutna_linija = ""

for el in nizTekst:
    if len(trenutna_linija)+len(el) >= m:
        redovi.append(trenutna_linija)
        trenutna_linija = el
    else:
        trenutna_linija += " "
        trenutna_linija += el

if trenutna_linija:
    redovi.append(trenutna_linija)




uredeno = []

for red in redovi:
    uredeno.append(centriranje(n, red))

for u in uredeno:
    print(u)
