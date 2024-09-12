# con este ejemplo vamos a crear una función que evalue la capacidad de un vuelo y asigne los asientos de pasagueros al incluirlos por nombre

# definimos una Clase

class Flight():
    # definimos que en la funcion de self solo tendremos la capacidad para evaluar  la clase 
    def __init__(self, capacity):
        #ahora vamos a guardar la capidad dentro del argumento capacidad 
        self.capacity = capacity
        # ahora creamos una lista vacia para almacenar los pasajeros que se van agregando
        self.passagers = []

# creamos una función que agregue pasajeros al vuelo por medio de un nuevo metodo
# Este metodo utiliza self debido que esta trabajando con un objeto individual con un keyword llamado name

    def add_passenger(self, name):
        if not self.open_seats(): # con esta condicional revisamos si hay asientos abiertos
            return False 
        self.passagers.append(name) # Con esta función se incluye en pasajeros el nombre por medio del metodo append
        return True 
        
# Creamos una función que nos devuelva los asientos abiertos para evaluar la capacidad disponible del vuelo

    def open_seats(self):
        return self.capacity - len(self.passagers)

# Ahora creamos un vuelo con la capacidad especifica para el vuelo, la cual evaluará al momento de agregar un pasajero

flight = Flight (3)

People = ["Harry", "Ron", "Hermione", "Ginny"] # Abrimos una lista de personas 

# ahora creamos un loop para ingresar los pasajeros 

for person in People:
    
    if flight.add_passenger(person): # agregamos al pasajero al vuelo
        print (f"Added {person} to flight successfully.") # si el resultado es satisfactorio y no sobrepasa la capacidad envia este mensaje
    else:
        print(f"No aviable seats for {person}") # si la capacidad se excede enviama este mensaje

# este metodo se llama programación orientado a objetos