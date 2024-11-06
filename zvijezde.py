n = int(input("Unesi broj"))
brZ = 1
pocetni = int(n/2) + n%2

i = 0
while True:
    print(" "*(pocetni - i) + "*"*brZ+ " "*(pocetni-(i-1)))
    i += 1
    brZ += 2
    if brZ > n:
        break

brZ -= 2
i -= 1
while brZ >= 1:
   print(" "*(pocetni - i) + "*"*brZ+ " "*(pocetni-(i-1)))
   i -= 1
   brZ -= 2
   if brZ < 1:
       break

