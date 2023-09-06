
class HistoryChanges():
    def __init__(self, user_id, produto_id, quantidade_id, data_compra, usuario_id,produto_id_key ):
        self.__user_id = user_id
        self.__produto_id = produto_id
        self.__quantidade_id = quantidade_id
        self.__data_compra = data_compra
        self.__usuario_id = usuario_id
        self.__produto_id_key = produto_id_key

    
    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self,user_id):
        self.__user_id = user_id

    @property
    def produto_id(self):
        return self.__produto_id

    @produto_id.setter
    def produto_id(self, produto_id):
        self.__produto_id = produto_id

    @property
    def quantidade_id(self):
        return self.__quantidade_id

    @quantidade_id.setter
    def quantidade_id(self, quantidade_id):
        self.__quantidade_id = quantidade_id
    @property
    def data_compra(self):
        return self.__data_compra
    
    @data_compra.setter
    def data_compra(self, data_compra):
        self.__data_compra = data_compra
    
    @property
    def usuario_id(self):
        return self.__usuario_id

    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self.__usuario_id = usuario_id

    @property
    def produto_id_key(self):
        return self.__produto_id_key

    @produto_id_key.setter
    def produto_id_key(self,produto_id_key):
        self.__produto_id_key = produto_id_key
