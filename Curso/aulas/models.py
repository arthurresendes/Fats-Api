from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Cria a conexão com o banco
db = create_engine("sqlite:///banco.db")

# Cria a base do banco de dados
Base = declarative_base()

# Cria as classes/tabelas do banco


# executa a criação