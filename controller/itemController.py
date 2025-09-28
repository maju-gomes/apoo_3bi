from models.item import Item
from dao.itemDAO import ItemDAO

class ItemController:
    def __init__(self):
        self.__dao = ItemDAO()

    def criarItem(self, descricao, quantidade):
        item = Item(None, descricao, quantidade)
        self.__dao.adicionar(item)

    def obterTodosOsItens(self):
        return self.__dao.listarTodos()
