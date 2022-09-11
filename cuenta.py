import contacto
import email
import correo
import correoRec

class Cuenta():
    userName = "mnb"
    direccion = "mnb@hotmail.com"
    dirServidorIn = "imap.secureserver.net"
    dirServidorOut = "smtpout.secureserver.net"
    contactos = []
    enviados = []
    recibidos = []


    def addContact (self):
        newContacto = contacto.Contacto  
        self.contactos.append(newContacto)

    def listContact (self):
        for i in range(len(self.contactos)):
            self.contactos[i].printContact()

    def addReceived (self):
        newReceived = correoRec.CorreoRec()
        self.recibidos.append(newReceived)

    def addSent (self):
        newSent = correo.Correo()
        self.enviados.append(newSent)

    def totalEnv (self):
        print("EL total de enviados son: ", len(self.enviados))

    def totalRec (self):
        print("El total de recibidos son: ", len(self.recibidos))

    def totales (self):
        print("El total de emails es de: " , len(self.enviados) + len(self.recibidos))

    def notRead (self):
        i = 0
        for j in range(len(self.recibidos)):
            if self.recibidos[i].leido == False:
                i += 1
        print("Hay ", i, " Mensajes no leidos")



    


    
    
        

