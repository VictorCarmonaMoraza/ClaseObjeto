from persona import Persona

if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona()  ## Crea un objeto vacio en memoria
    persona1.inicializar_persona('Laiai', 'Acosta')
    persona1.mostrar_persona()

    ##Creacin de un segundo objeto
    persona2 = Persona()
    persona2.inicializar_persona('Ian','Sanchez')
    persona2.mostrar_persona()
