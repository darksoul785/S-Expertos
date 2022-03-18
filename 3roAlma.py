# LISTAS DE OBJETOS
dic = {
    'obj1' : ["A", "B", "C"],
    'obj2' : ["A", "M", "Y"],
    'obj3' : ["A", "B", "D"],
    'obj4' : ["D", "X", "C"]

}

hechos = input("Introduce tus hechos, separados por comas")

hechos_split = hechos.split(",")
print(hechos)

for key,value in dic.items():
    if (set(value) == set(hechos_split)):
        print("Tu objeto es el objeto "+ str(key))

