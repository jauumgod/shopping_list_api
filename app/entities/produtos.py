
class Produtos():
    def __init__(self, nome, quantidade):
        self._nome = nome
        self._quantidade = quantidade


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome

    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self,quantidade):
        self._quantidade = quantidade
    