import correo
class CorreoRec(correo.Correo):
    leido = False

    def __init__(self):
        super().__init__()

    def read (self):
        self.leido = True
