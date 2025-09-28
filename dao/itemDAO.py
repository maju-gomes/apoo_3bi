import sqlite3
from models.item import Item

class ItemDAO:
    def __init__(self, nome_banco="meu_banco.db"):
        self.__nome_banco = nome_banco
        self.__criar_tabela()

    def __conectar(self):
        return sqlite3.connect(self.__nome_banco)

    def __criar_tabela(self):
        conn = self.__conectar()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def adicionar(self, item: Item):
        conn = self.__conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
            (item.get_descricao(), item.get_quantidade())
        )
        conn.commit()
        conn.close()

    def listarTodos(self):
        conn = self.__conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade FROM itens")
        linhas = cursor.fetchall()
        conn.close()

        itens = [Item(id, desc, qtd) for (id, desc, qtd) in linhas]
        return itens
