# lo decoradores realizan el trabajo de tomar el input de una función y realizar una modificacion al realizar la entreg del resultado 

def announce(f): # Creamos la variable
    def wrapper(): # declaramos la función que realizará la modificación
        print("About to run the funtion...")
        f()
        print("Done whith the funtion,")
    return wrapper
    
@announce
def hello():
    print("Hello Word")

hello()