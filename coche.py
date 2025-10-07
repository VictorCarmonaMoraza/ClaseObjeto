class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca  ##Atruibuto publico
        self._modelo = modelo  # Atributo protegido
        self.__color = color  # Atributo privado

    def conducir(self):
        print(f"El coche {self.marca} y {self._modelo} de color {self.__color} esta en movimiento")

    # --- Getter para color (acceso controlado al atributo privado) ---
    def get_color(self):
        return print(self.__color)

    # --- Setter para color (modificar con validación si se desea) ---
    def set_color(self, nuevo_color):
        if isinstance(nuevo_color, str) and nuevo_color.strip():
            self.__color = nuevo_color
        else:
            print("❌ Color no válido. Debe ser un texto no vacío.")

    # --- Getter para color (acceso controlado al atributo privado) ---
    def get_marca(self):
        return print(self.marca)

    # --- Setter para color (modificar con validación si se desea) ---
    def set_marca(self, marca):
        if isinstance(marca, str) and marca.strip():
            self.marca = marca
        else:
            print("❌ Color no válido. Debe ser un texto no vacío.")

    # --- Getter para color (acceso controlado al atributo privado) ---
    def get_modelo(self):
        return print(self._modelo)

    # --- Setter para color (modificar con validación si se desea) ---
    def set_modelo(self, nuevo_modelo):
        if isinstance(nuevo_modelo, str) and nuevo_modelo.strip():
            self._modelo = nuevo_modelo
        else:
            print("❌ Color no válido. Debe ser un texto no vacío.")
