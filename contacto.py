
class Contacto():
    name = ""
    dir = ""

    def __init__(self):
        self.name = input("Ingrese el nombre del contacto: \n")
        self.dir = input("Ingrese el email del contacto: \n")

    def printContact(self):
        print("Nombre: " , self.name)
        print("Direccion: " , self.dir)
