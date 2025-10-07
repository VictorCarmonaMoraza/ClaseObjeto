class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self._color = color  # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

        '''Marca: {self.get_marca()}
        Modelo: {self.get_modelo()}
        Color: {self.get_color()}'''  ##Esto es valido pero menos eficiente

    '''def get_marca(self):
        return self._marca'''

    @property  # Definir el metodo get mas pythonica
    def marca(self):
        return self._marca

    '''def set_marca(self, marca):
        self._marca = marca'''

    @marca.setter  # Definir el metodo set mas pythonica
    def marca(self, marca):
        self._marca = marca

    '''def get_modelo(self):
        return self._modelo'''

    @property
    def modelo(self):
        return self._modelo

    '''def set_modelo(self, modelo):
        self._modelo = modelo'''

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    '''def get_color(self):
        return self._color'''

    @property
    def color(self):
        return self._color

    '''def set_color(self, color):
        self._color = color'''

    @color.setter
    def color(self, color):
        self._color = color
