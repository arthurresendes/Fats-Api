'''
Endpoints -> Seria o caminho via URL , usamos substantivos nos nomes e não verbos
Api REST -> Temor recursos(resources) podendo sem um model da nossa aplicação

CRUD:
get -> Usado para busca de informações
put -> Atualizar um recurso ,  não usamos em URL em coleção e sim em individual
post -> Mandar dados, não usamos na URL individual e sim em coleção
delete -> Deletar dados

Request -> Requisição é quando colamos uma url no google , podendo passar informações , exemplo api/v1/produtos?order=desc&limit=10, nesse exemplo ordenaria de forma decrescente e mostraria no limite 10 produtos, sendo chamado de query string

Response -> Modo como a resposta ira vir para o usuario, tendo seus tipos de status , começando com 1 seria informacional , 2 sucesso, 3 redirecionamento , 4 client error  e 5 erro de servidor

Segurança -> Devemos limitar as requisições para o servidor não cair

Usamos tokens para autenticação , no caso uma chave publica
'''