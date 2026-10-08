### 1.0 PARA QUE SERVE DISPONIVEL 

a coluna disponivel serve para indicar se o status do livro está verdadeiro ou falso, indicando se ele está apto para ser pego ou não, respectivamente 

### 2.0 PORQUE USAR SESSION.COMMIT

o session.commit serve para salvar as alterações ou operações feitas em uma consulta e as enviar para o banco de dados para que ele fique atualizado

### 3.0 ONDE VOCÊ USA O RELACIONAMENTO LIVRO-AUTOR

eu uso o relacionamento entre essas tabelas quando preciso acessar colunas em uma operação que só podem ser acessadas por outra tabela, por exemplo, quando eu quero acessar os livros de um determinado autor pelo nome dele. Eu busco o nome do autor pelo já que as tabelas estão interligadas, permitindo acessar as colunas uma das outras para receber informações específicas com base em filtrações dos livros.

# def listar_todos_livros(session):
#  sele_livro = select(Livro)
# livros = session.scalars(sele_livro).all()
#   print("Autores e seus livros")
#   for livro in livros:
#      print(f"Título: {livro.titulo}, Ano: {livro.ano}, Autor: {livro.autor.nome}, Disponibilidade {livro.disponivel}")


# def listar_livros_disponiveis(session):
#    sele_livro = select(Livro).where(Livro.disponivel.like(True))
#   livros = session.scalars(sele_livro).all()
#  print(" --- Livros disponiveis ---")
# for livro in livros:
#    print(livro.titulo, livro.ano, livro.autor.nome)

# def listar_livros_por_autor(session, nautor):
#    sele_livro = select(Livro).join(Livro.autor).where(Autor.nome.ilike(f"%{nautor}%"))
#   livros = session.scalars(sele_livro).all()
#  print(f"--- Livros do autor '{nautor}' ---")
# for livro in livros:
# print(livro.titulo, livro.ano, livro.autor.nome) 