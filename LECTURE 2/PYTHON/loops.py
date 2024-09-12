# con Loop cuenta los elementos dentro de una lista en especifica para el for y los trae por cada iteracion
for i in [0,1,2,3,4,5]:
    print (i)
    
# ahora para simplificar la escritura podemosutilizar range y un determinado numero para que cuente hasta el y los imprima cada uno 

for i in range (6):
    print(i)

# ahora si tenemos una lista de nombres y qeremos imprimir cada nombre hariamos lo siguiente:

Names = ["Harry", "Ron", "Hermione"]

for name in Names:
    print(name)

# ahora si queremos que se imprima letra por letra de un nombre se haria lo siguiente:

name = "Harry"

for character in name:
    print(character)