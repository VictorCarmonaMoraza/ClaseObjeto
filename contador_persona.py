class Persona3:
    # Atributos de clase
    contador_persona = 0

    def __init__(self, nombre, apellido):
        # Atributos de instancia
        Persona3.contador_persona += 1
        self.nombre = nombre
        self.apellido = apellido
        self.id = Persona3.contador_persona

    def mostrar_persona(self):
        print(f"""--- Persona ---
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    ID: {self.id}
    """)


if __name__ == '__main__':
    persona1 = Persona3('Laiai', 'Acosta')
    persona1.mostrar_persona()
    persona2 = Persona3('Ian', 'Sanchez')
    persona2.mostrar_persona()
    persona3 = Persona3('Ana', 'Gomez')
    persona3.mostrar_persona()
