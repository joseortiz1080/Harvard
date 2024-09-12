# Con las Clases opodemos 

class Point():
# con la fincuón init, podemos llamarla para rear varios puntos
    def __init__(self, input1, input2):
            self.x  = input1
            self.y  = input2

# Ahora creamos un nuevo punto de la siguiente manera 

p = Point(2,8)

# ahora que hemos creado los puntos, podemos imprimilos en la terminal

print(p.x)
print(p.y)

