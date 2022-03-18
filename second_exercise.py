## SE DEFINE ARREGLO DE LETRAS
array = [['A','B','C'],['A','M','Y'],['D','X','C'],['A','B','D']]
n_accep = [] #lista de letras no aceptadas
accep = [] #lista de letras aceptadas

aux = 0 #variable auxiliar

for obj in array:
    for letter in accep:
        aux=0
        if letter not in obj:
            aux=1
    
    if (aux == 0):
        for letter in obj:
            #si la letra esta en las no aceptadas, se rompe ciclo
            if letter in n_accep:
                break
            #si letra esta en las aceptadas, continua
            if letter in accep:
                continue

            answer = input("Tu objeto tiene "+str(letter)+"?") #se captura respuesta

            #se agrega letra aceptada
            if (answer=="y" or answer=="Y"):
                accep.append(letter)
                continue
            #se agrega letra rechazada
            else:
                n_accep.append(letter)
                break

        #si se llegó al ultimo elemento del arreglo y la respuesta
        if (obj.index(letter) == len(obj)-1 and (answer=="y" or answer=="Y")):
            print("Tu objeto es el objeto "+str(array.index(obj)+1))
            break
    else:
        continue

if (answer!="y" and answer !="Y"):
    print("No hubo coincidencias :(")