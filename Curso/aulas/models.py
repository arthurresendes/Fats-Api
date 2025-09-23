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

# executa a criação