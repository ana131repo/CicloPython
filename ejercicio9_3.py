""" Modulo para gestionar usuarios"""

class Usuario:
    """guardar datos de un usuario"""

    def __init__(self, nombre, apellidos, telefono, localidad):
        """ los datos que se guardan"""
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.localidad = localidad

    def describir_usuario(self):
        """_descripción del usuarios  
        """
        print (f"{self.nombre} {self.apellidos} tiene el teléfono {
              self.telefono} y vive en {self.localidad}")

    def saludar_usuario(self):
        """ Saludar a los usuarios"""
        print (f" Bienvenido {self.nombre} {
            self.apellidos}")


usuario1 = Usuario("Ana", "Caballero", "639886187", "Porriño")
usuario1.describir_usuario()

usuario2 = Usuario("Yaiza", "Gonzálves", "657234561", "Porriño")
usuario2.describir_usuario()
