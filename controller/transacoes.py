import sqlite3
import sys


sys.path.insert(0, './')
sys.path.insert(0, './models')
from models.conexao import Conexao

class Transacao:
    def __init__(self, id_usuario, valor, descricao, categoria, data):
        self.id_usuario = id_usuario
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria
        self.data = data
        self.salvar_no_banco()

    def salvar_no_banco(self):
        Conexao.salvar_no_banco('''
            INSERT INTO transacoes (id_usuario, valor, descricao, categoria, data)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.id_usuario, self.valor, self.descricao, self.categoria, self.data))
   
    @staticmethod
    def retornar_todos():
        usuarios = Conexao.retornar_todos('SELECT * FROM transacoes')
        return usuarios
