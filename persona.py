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
