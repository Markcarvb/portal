from model.db import conectar
 
class estudante:
   def _init_(self,nome,email,senha):
      self.nome=nome
      self.email=email
      self.senha=senha

   def salvar(self):
      conexao=conectar()
      cursor=conexao.cursor()
      cursor.execute(
         "insert INTO estudantes (nome, email, senha)VALUES (?, ?, ?)"
         (self.nome, self.email, self.senha),
      )
      conexao.commit()
      conexao.close()

   @staticmethod
   def buscar_por_email(email):
      conexao=conectar()
      cursor= conexao.cursor()
      cursor.execute("SELECT * from estudantes WHERE email = ?"(email,))
      estudante= cursor.fetchone()
      conexao.close()
      return estudante

