class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2


    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1


    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2


    def sumar(self):
        return print(f"{self._operando1 + self._operando2}")

    def restar(self):
        return print(f"{self._operando1 - self._operando2}")

    def multiplicar(self):
        return print(f"{self._operando1 * self._operando2}")

    def dividir(self):
        # Validacion de division por cero
        if self._operando2 == 0:
            return print(f"Error: Division por cero")
        return print({self._operando1 / self._operando2})
