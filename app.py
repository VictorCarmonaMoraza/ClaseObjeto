from persona import Persona

if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Laiai', 'Acosta')  ## Crea un objeto vacio en memoria
    persona1.mostrar_persona()

    ##Creacin de un segundo objeto
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_persona()

    if hex(id(persona1)) == hex(id(persona2)):
        print("Los objetos son iguales")
    else:
        print("Los objetos son diferentes")
