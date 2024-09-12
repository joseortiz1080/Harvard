import sys

# Para evitar errores de ingreso de texto donde se deberia tener un numero, se debe colocar de la siguiente manera 
# En donde se utiliza la función try, para evaluar la entrada y se agrega la función except para excluir el ingreso de un texto 
# luego al evaluar el resultado del valor ingresado y resultar un texto, imprime el mensaje de error y sale del programa con system.exit(1)

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

# ahora para evitar errores como por ejempo que se se divida por cero y causar un error,  incluimos la función try para poder evaluar la antes
# Luego le damos una exepsión la cual menciona que si se divide por cero, se debe salir del sistema 
# hay que tener en cuenta que para poder salir del error importamos al inicio del codigo  import sys, el cual si adquiere el valor de 1 sale de la ejecución del programa
try: result =x/y

except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
