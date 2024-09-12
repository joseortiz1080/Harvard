# Vamos a ver como se pueden representar mejor las funciones 
# creamos una lista y dentro de ella un diccionario con {}
people = [
    {"Name": "Harry", "house": "Gryffindor"},
    {"Name": "Cho", "house": "Ravenclaw"},
    {"Name": "Drako", "house": "Slyderin"}
]

# Utilizamos la función sort() para ordenar los elementos dentro de la lista
# para que la función sort funcione,se debe tener encuenta que al compara dos diccionarios, se deben tener claro la llave a evaluar
# en este caso se hace por medio de Name, para ello creamos una función que almacene la llave Name del diccionario en f

def f (person):
    return person["house"]

people.sort(key=f)

print(people)

# Python permita realizar esta expresiòn de la función de una manera mas facil la cual utiliza la función lambda

people.sort(key=lambda person: person["Name"])

print(people)