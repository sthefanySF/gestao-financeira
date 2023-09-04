import sqlite3
import sys


sys.path.insert(0, './')
sys.path.insert(0, './models')
from models.conexao import Conexao 



class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha
        self.salvar_no_banco()
    
    
    def salvar_no_banco(self):
        sql = f'INSERT INTO usuarios  VALUES (NULL,"{self._nome}","{self._email}","{self._senha}")'
        cone = Conexao()
        cone.salvar_no_banco(sql)
    
    @staticmethod
    def retornar_todos():
        usuarios = Conexao.retornar_todos('SELECT * FROM usuarios')
        return usuarios
        
        
    
    
    @staticmethod
    def deletar(id_usuario):
        Conexao.deletar('DELETE FROM usuarios WHERE id = ?', (id_usuario,))


    @staticmethod
    def atualizar(id_usuario, nome, email, senha):
        Conexao.atualizar('''
            UPDATE usuarios
            SET nome = ?, email = ?, senha = ?
            WHERE id = ?
        ''', (nome, email, senha, id_usuario))
   
    @classmethod
    def autenticar(cls, email, senha):
        resposta = Conexao.autenticar(email,senha)
        return resposta
    
    @classmethod
    def obter_usuario_por_id(cls, id_usuario):
        # Consulta SQL para obter um usuário por ID
        sql = "SELECT nome, email, senha FROM usuarios WHERE id = ?"
        conexao = Conexao()
        resultado = conexao.retornar_usuario(sql, (id_usuario,))
        
        if resultado:
            nome, email, senha = resultado
            return cls(nome, email, senha)  # Retorna uma instância de Usuario com os dados encontrados
        else:
            return None  # Retorna None se o usuário não for encontrado