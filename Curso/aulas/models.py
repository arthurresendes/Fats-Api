from sqlalchemy import create_engine, Column, String , Integer, Boolean , Float , ForeignKey
from sqlalchemy.orm import declarative_base

# Cria a conexão com o banco
db = create_engine("sqlite:///banco.db")

# Cria a base do banco de dados
Base = declarative_base()

# Cria as classes/tabelas do banco
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer , primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email" , String, nullable=False)
    senha = Column("senha" , String)
    ativo = Column("ativo" , Boolean)
    admin = Column("admin" , Boolean, default=False)
    
    def __init__(self,nome,email,senha,ativo=True,admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"
    
    id_pedido = Column("id_pedido", Integer,primary_key=True, autoincrement=True)
    status = Column("status", String) # Pendente , cancelado , finalizado
    usuario = Column("usuario",ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self,usuario,status="PENDENTE",preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco

# executa a criação