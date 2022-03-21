l1 = {'A', 'B', 'C'}
l2 = {'A', 'M', 'Y'}
l3 = {'D', 'X', 'C'}
l4 = {'A', 'B', 'D'}

A = input("Si tienes el elemento A escriba A en mayusculas DE LO CONTRARIO PRESIONE N \n")
if A in l1:
    acum = "A"
    B = input("Si tienes el elemento B escriba B en mayusculas DE LO CONTRARIO PRESIONE N\n")
    if B in l1:
        acum = acum+"B"
        C = input("Si tienes el elemento C escriba C en mayusculas DE LO CONTRARIO PRESIONE N \n")
        if C in l1:
            acum = acum+"C"
            print("tienes la lista 1")
            exit()
        D = input("Si tienes el elemento D escriba D en mayusculas DE LO CONTRARIO PRESIONE N \n")
        if D in l3:
            acum = acum+"D"
            print("tienes la lista 4")
            exit()
    M = input("Si tienes el elemento M escriba M en mayusculas DE LO CONTRARIO PRESIONE N\n")
    if M in l2:
        acum = acum+"M"
        Y = input("Si tienes el elemento Y escriba Y en mayusculas DE LO CONTRARIO PRESIONE N \n")
        if Y in l2:
            acum = acum+"Y"
            print("tienes la lista 2")
            exit()
    print("No hay datos")
    exit()
D = input("Si tienes el elemento D escriba D en mayusculas DE LO CONTRARIO PRESIONE N \n")
if D in l4:
    acum = "D"
    X = input("Si tienes el elemento X escriba X en mayusculas DE LO CONTRARIO PRESIONE N\n")
    if X in l4:
        acum = acum+"X"
        C = input("Si tienes el elemento C escriba C en mayusculas DE LO CONTRARIO PRESIONE N \n")
        if C in l1:
            acum = acum+"C"
            print("tienes la lista 3")
            exit()
    print("No hay datos")
    exit()
print("No hay datos")
exit()
