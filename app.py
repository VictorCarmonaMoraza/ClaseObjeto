from aritmetica import Aritmetica
from coche import Coche
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

    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()

    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
    aritmetica2.dividir()

    aritmetica3 = Aritmetica()
    aritmetica4 = Aritmetica(1)
    aritmetica4.operando2 = 3
    aritmetica4.sumar()

    aritmetica5 = Aritmetica(operando1=10, operando2=5)
    aritmetica5.sumar()

    ##Encapsulamiento
    coche = Coche("Toyota", "Corolla", "Rojo")
    coche.marca = "Mazda"
    coche.conducir()
    print(f'marca coche: {coche.marca}')
    # Intentar agreagr un nuevo atributo
    #Si creamos un nuevo, este no tendra el nuevo atributo
    setattr(coche, 'edad_coche', '42 años')
    print(coche.edad_coche)
    ##Obtener todos los atributos de un objeto
    print(coche.__dict__)
