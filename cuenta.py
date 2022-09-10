import contacto


class Cuenta():
    userName = "mnb"
    direccion = "mnb@hotmail.com"
    dirServidorIn = "imap.secureserver.net"
    dirServidorOut = "smtpout.secureserver.net"
    contactos = []
    enviados = []
    recibidos = []


    def addContact (self):
        newContacto = contacto.Contacto()   
        self.contactos.append(newContacto)

    def listContact (self):
        for i in range(len(self.contactos)):
            self.contactos[i].printContact()
    
        

