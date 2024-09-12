# Con las funciones hay algunas predeterminadas, como por ejemplo input, print, etc, pero nosotros podemos crear una funcion tambien

# vamos a crear una funcion para definir la raiz de los numeros del 1 al 9, para definir funciones utilizamos el parametro def
# Esta función coge un rango de 10, y lo utiliza para hacer 10 iteraciones y en cada iteración ejecuta la función square, la cual 
# remplaza el numero de iteración en la variable i y luego remplaza la variable x de la función y la multiplica por el numero en i

def square (x):
    return x*x

for i in range (10):
    print(f"The square of {i} is {square (i)}")