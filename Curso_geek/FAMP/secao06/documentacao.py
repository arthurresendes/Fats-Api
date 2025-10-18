'''
API(Diretorio) -> Diretorio onde ficara armazendo um subdiretorio v1 que nele tera um arquivo chamado api.py e uma pasta chamada endpoints e no endpoints tem dois arquivos python usuario e artigo , onde tem as rotas como POST, GET ,DELETE e PUT. Entrando em detalhes:
    - api.py: Sempre chamamos o fastapi para pegar o ApiRouter e api.v1.endpoints onde a gente tem acesso aos dois arquivos py , no api.py temos que fazer a inclusão das rotas com incloude_router(artigo.router , prefix="/artigos", tags=["artigos"]) , o artigo.router seria a rota padrão dos endpoints , exemplo :@router.get, @router.post, etc. Já o prefix será o caminho que teremos que utilizar para colocar na url , exemplo: http://127.0.0.1:8000/api/v1/artigos/1 e por fim a tags servem para separar na documentação por meio de "secções"
    - artigo.py
    - usuario.py


CORE ->

MODELS

SCHEMAS
'''