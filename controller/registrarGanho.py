from models.conexao import Conexao

class RegistrarGanho:
    def __init__(self, id_usuario, ganho_mensal, ganho_adicional, descricao_adicional, data):
        self.id_usuario = id_usuario
        self.ganho_mensal = ganho_mensal
        self.ganho_adicional = ganho_adicional
        self.descricao_adicional = descricao_adicional
        self.data = data
        self.salvar_no_banco()

    def salvar_no_banco(self):
        sql = f'''
            INSERT INTO ganhos (id_usuario, ganho_mensal, ganho_adicional, descricao_adicional, data)
            VALUES ("{self.id_usuario}","{self.ganho_mensal}","{self.ganho_adicional}", "{self.descricao_adicional}", "{self.data}")
        '''
        Conexao.salvar_no_banco(sql)
        

    @classmethod
    def retornar_todos(cls):
        return Conexao.retornar_todos('SELECT * FROM ganhos')
    
    
    @classmethod
    def retornar_unico_usuario(cls,id_usuario):
        return Conexao.retornar_usuario(f'SELECT * FROM ganhos WHERE id_usuario = {id_usuario};')
        

    @classmethod
    def deletar(cls, id_registro):
        Conexao.deletar('DELETE FROM ganhos WHERE id = ?', (id_registro,))

    @classmethod
    def atualizar(cls, id_registro, id_usuario, ganho_mensal, ganho_adicional, descricao_adicional, data):
        sql = '''
            UPDATE ganhos
            SET id_usuario = ?, ganho_mensal = ?, ganho_adicional = ?, descricao_adicional = ?, data = ?
            WHERE id = ?
        '''
        Conexao.atualizar(sql, (id_usuario, ganho_mensal, ganho_adicional, descricao_adicional, data, id_registro))
   
    @classmethod
    def ganho_total(cls,id_usuario):
        sql = f"SELECT SUM(ganho_mensal + ganho_adicional) FROM ganhos WHERE id_usuario = {id_usuario};"
        return Conexao.retornar_usuario(sql)