import pyodbc

#conectando o banco sql server
def conectar():
    conexao=pyodbc.connect(
       "DRIVER={SQL Server}"
       "SERVER=DESKTOP-8LE1J9H\SQLEXPRESS;"
       "DATABASE=Portal_Estudantes;"
       "Trusted_Connection=yes;"
    )
    return conexao