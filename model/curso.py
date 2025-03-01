from model.db import conectar

class curso:
    def __init__(self,nome,descricao):
        self.nome=nome
        self.descricao=descricao

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO Cursos (nome, descricao) VALUES (?, ?)",
            (self.nome, self.descricao),
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Cursos")
        cursos = cursor.fetchall()
        conexao.close()
        return cursos        
        