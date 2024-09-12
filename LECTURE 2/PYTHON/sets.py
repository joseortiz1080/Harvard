# Create an empy set

s = set()

# Agrego elementos al sets

s.add(1)
s.add(2)
s.add(3)
s.add(4)


# si agrero otro numero al sets, como por ejemplo el 3 que ta esta, no aparece dos veces

s.add(3)

print(s)

# ahora para eliminar un elemento del set, aplicamos el siguiente codigo

s.remove(2)

print(s)

# ahora para poder saber el numero de items dentro de un set utilizamos len

print(f"The set has {len(s)} elements.")

# en el resultado me da que tiene 3 elementos ya que hemos borrado con el comando remove 1 elemento de los 4 que habia inicialmente



