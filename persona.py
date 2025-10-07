##Defincion de una clase

class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"""--- Persona ---
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    """)
        print(f"La direcccion de memoria es: {id(self)}")
        print(f"La direccion de memoria es: {hex(id(self))}")
