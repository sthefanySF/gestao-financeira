import sys


sys.path.insert(0, './')
sys.path.insert(0, '.models')
from models.conexao import Conexao


class RegistrarGasto:
    def __init__(self, id_usuario, valor, descricao, categoria, data):
        self.id_usuario = id_usuario
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria
        self.data = data
        self.salvar_no_banco()

    def salvar_no_banco(self):
        sql = f'''
            INSERT INTO gastos (id_usuario, valor, descricao, categoria, data)
            VALUES ("{self.id_usuario}", "{self.valor}", "{self.descricao}", "{self.categoria}", "{self.data}")
        '''
        Conexao.salvar_no_banco(sql)

    @classmethod
    def retornar_todos(cls):
        return Conexao.retornar_todos('SELECT * FROM gastos')

    @classmethod
    def deletar(cls, id_registro):
        Conexao.deletar('DELETE FROM gastos WHERE id = ?', (id_registro,))

    @classmethod
    def atualizar(cls, id_registro, id_usuario, valor, descricao, categoria, data):
        sql = '''
            UPDATE gastos
            SET id_usuario = ?, valor = ?, descricao = ?, categoria = ?, data = ?
            WHERE id = ?
        '''
        Conexao.atualizar(sql, (id_usuario, valor, descricao, categoria, data, id_registro))
    @classmethod
    def retornar_gastos(cls,id_usuario):
        return Conexao.retornar_usuario(f'SELECT * FROM gastos WHERE id_usuario = {id_usuario};')
    
    @classmethod
    def retornar_total_gastos(cls,id_usuario):
        return Conexao.retornar_usuario(f"SELECT SUM(valor)  FROM gastos WHERE id_usuario = {id_usuario};")
