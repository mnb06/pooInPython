
class Correo():
    asunto = ""
    texto = ""
    origen = ""
    destino = []

    def __init__(self):
        self.asunto = input("ingrese el asunto: \n")
        self.texto = input("ingrese el texto: \n")
        self.origen = input("ingrese el origen: \n")
        self.destino = input("ingrese el destinatario: \n")
