from pydantic_settings import BaseSettings # Ele valida e converte os tipos de dados dessas configurações, permitindo a criação de classes de configuração bem definidas e com sugestão de tipo, facilitando o gerenciamento seguro de configurações em diferentes ambientes (desenvolvimento, produção, etc.). 

from sqlalchemy.ext.declarative import declarative_base # é uma função no SQLAlchemy que cria uma classe base para o sistema de mapeamento declarativo, permitindo que você defina modelos de banco de dados como classes Python

from typing import ClassVar #o uso de ClassVar é crucial para indicar ao Pydantic que DBBaseModel é uma variável de classe (metadado da classe Setting) e não um atributo que deve ser validado ou carregado a partir de variáveis de ambiente.

class Setting(BaseSettings):
    """
    Configurações gerais utilizadas na aplicação
    """
    API_V1_STR:str = '/api/v1' # Caminho padrão da api versão1
    DB_URL: str = "sqlite+aiosqlite:///./faculdade.db" # URL do banco de dados + aiosqlite para ser usado juntamento com funções assincronicas //./ indica que sera nesse repositorio
    DBBaseModel: ClassVar = declarative_base() # Modelo base , permitindo a definição de modelos de banco de dados
    
    class Config:
        case_sensitive = True


settings = Setting() # Instanciando um objeto para utilizar ele