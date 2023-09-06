


class ProdutoLista():
    def __init__(self, lista_id, produto_id, quantidade, lista_id_key, produto_id_key):
        self.__lista_id = lista_id
        self.__produto_id = produto_id
        self.__quantidade = quantidade
        self.__lista_id_key = lista_id_key
        self.__produto_id_key = produto_id_key


    @property
    def lista_id(self):
        return self.__lista_id

    @lista_id.setter
    def lista_id(self, lista_id):
        self.__lista_id = lista_id

    @property
    def produto_id(self):
        return self.__produto_id

    @produto_id.setter
    def produto_id(self, produto_id):
        self.__produto_id = produto_id

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def lista_id_key(self):
        return self.__lista_id_key

    @lista_id_key.setter
    def lista_id_key(self,lista_id_key):
        self.__lista_id_key = lista_id_key

    @property
    def produto_id_key(self):
        return self.__produto_id_key

    @produto_id_key.setter
    def produto_id_key(self,produto_id_key):
        self.__produto_id_key = produto_id_key