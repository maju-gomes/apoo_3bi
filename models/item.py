class Item:
    def __init__(self, id, descricao, quantidade):
        self.__id = id
        self.__descricao = descricao
        self.__quantidade = quantidade

    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_quantidade(self):
        return self.__quantidade

    def __str__(self):
        return f"Item {self.__id} - {self.__descricao} ({self.__quantidade})"
