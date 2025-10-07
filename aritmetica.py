class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        return print(f"{self.operando1 + self.operando2}")

    def restar(self):
        return print(f"{self.operando1 - self.operando2}")

    def multiplicar(self):
        return print(f"{self.operando1 * self.operando2}")

    def dividir(self):
        # Validacion de division por cero
        if self.operando2 == 0:
            return print(f"Error: Division por cero")
        return print({self.operando1 / self.operando2})
