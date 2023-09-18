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
        Conexao.deletar(f'DELETE FROM gastos WHERE id = {id_registro};')

    @classmethod
    def atualizar(cls, id_registro, valor, descricao, categoria, data):
        sql = f'''
            UPDATE gastos
            SET valor = '{valor}', descricao = '{descricao}', categoria = '{categoria}', data = '{data}'
            WHERE id_usuario = {id_registro};
        '''
        Conexao.atualizar(sql)
    @classmethod
    def retornar_gastos(cls,id_usuario):
        return Conexao.retornar_usuario(f'SELECT * FROM gastos WHERE id_usuario = {id_usuario};')
    
    @classmethod
    def retornar_total_gastos(cls,id_usuario):
        return Conexao.retornar_usuario(f"SELECT SUM(valor)  FROM gastos WHERE id_usuario = {id_usuario};")

    @classmethod
    def retornar_ganhos_por_data(cls, id_usuario, data_selecionada):
        sql = f"SELECT * FROM gastos WHERE id_usuario = {id_usuario} AND data = '{data_selecionada}';"
        ganhos = Conexao.retornar_todos(sql)
        print(ganhos)

        return ganhos