class Shopping():
    def __init__(self, username, date_create):
        self.__username = username
        self.__date_create = date_create

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def date_create(self):
        return self.__date_create

    @date_create.setter
    def date_create(self, date_create):
        self.__date_create = date_create
