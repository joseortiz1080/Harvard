# Aqui lo que vamos hacer es que las funciones estarán anidadas en otro archivo python, y aqui llamaremos las funciones para ser utilizadas
# para utilizar las variables de otro archivo debemos importarlas de la siguiente manera

from functions import square 

for i in range (10):
    print(f"The square of {i} is {square (i)}")
    
    