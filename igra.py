opcije = [1,2,3,4,5,6,7,8,9]
ploca = [[1,2,3], [4,5,6], [7,8,9]]


def ispisPloce():
    for x in range(3):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(3):
            print("", ploca[x][y], end= " |")
    print("\n+---+---+---+")


def minjajPlocu(num, igrac):
    match num:
        case 1:
            ploca[0][0] = igrac
        case 2:
            ploca[0][1] = igrac
        case 3:
            ploca[0][2] = igrac
        case 4:
            ploca[1][0] = igrac
        case 5:
            ploca[1][1] = igrac
        case 6:
            ploca[1][2] = igrac
        case 7:
            ploca[2][0] = igrac
        case 8:
            ploca[2][1] = igrac
        case 9:
            ploca[2][2] = igrac
        case _:
            print("broj izvan dosega")

def provjeri_pobjedu(ploca, znak):
    for i in range(3):
        if all([ploca[i][j] == znak for j in range(3)]) or all([ploca[j][i] == znak for j in range(3)]):
            return True
    if (ploca[0][0] == znak and ploca[1][1] == znak and ploca[2][2] == znak) or (ploca[0][2] == znak and ploca[1][1] == znak and ploca[2][0] == znak):
        return True
    return False


def Unos(opcije):
    while True:
        odabir = int(input("Unesite opciju: "))
        if(odabir in opcije and odabir >= 1 and odabir <= 9):
            break
    return odabir


turnCounter = 0


while(True):
    if(turnCounter % 2 == 1):
        ispisPloce()
        odabran = Unos(opcije)

        minjajPlocu(odabran, 'O')
        opcije.remove(odabran)

        if(provjeri_pobjedu(ploca, 'O')):
            print("Pobjedio O")
            break
        turnCounter += 1
    else:
        ispisPloce()
        odabran = Unos(opcije)
        minjajPlocu(odabran, 'X')
        opcije.remove(odabran)
        
        if(provjeri_pobjedu(ploca, 'X')):
            print("Pobjedio X")
            break
        turnCounter += 1

    if(len(opcije) == 0):
        print("nema pobjednika")
        break
    
            
        
    
