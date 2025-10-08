from aritmetica import Aritmetica
from atributos_clase_instancia import Persona2
from coche import Coche
from contador_persona import Persona3
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
    # Si creamos un nuevo, este no tendra el nuevo atributo
    setattr(coche, 'edad_coche', '42 años')
    print(coche.edad_coche)
    ##Obtener todos los atributos de un objeto
    print(coche.__dict__)

    print(f'*** Atributos de clase ***')
    print(f'Atributos de Clase Aritmetica: {Persona2.atributo_clase}')
    # Modificamos el atributo de clase
    Persona2.atributo_clase = 42
    print(f'Atributos de Clase Aritmetica: {Persona2.atributo_clase}')

    # Creamos el primer objeto
    persona1 = Persona2(15)
    print(f'Atributo de clase desde persona1: {persona1.atributo_clase}')
    print(f'Atributo de clase desde persona1: {persona1.contador_persona}')
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')

    # Creamos el segundo objeto
    persona2 = Persona2(23)
    print(f'Atributo de clase desde persona2: {persona2.atributo_clase}')
    print(f'Atributo de clase desde persona1: {persona2.contador_persona}')
    print(f'Atributo de instancia desde persona2: {persona2.atributo_instancia}')

    print(f'*** Contador de personas ***')
    ##Contador personas
    # Creamos el primer objeto
    persona3 = Persona3('victor', 'gomez')
    print(f'Atributo de clase desde persona3: {persona3.mostrar_persona()}')

    # Creamos el segundo objeto
    persona4 = Persona3('Ana', 'Lopez')
    print(f'Atributo de clase desde persona4: {persona4.mostrar_persona()}')
