from models import Autor, Livro

def popular_banco(session):
    autor1 = Autor(nome="Augusto Cury", pais="Brasil")
    autor2 = Autor(nome="Araki", pais="Japão")
    autor3 = Autor(nome="Cleysyvan", pais="Brasil")

    livros = [
        Livro(titulo="Ansiedade, o Mal do século", ano=2026, autor=autor1, disponivel = True),
        Livro(titulo="O vendedor de sonhos", ano=1991, autor=autor1, disponivel = False),
        Livro(titulo="Jojo", ano=2016, autor=autor2, disponivel = False),
        Livro(titulo="A hora da biologia", ano=2010, autor=autor3, disponivel = True),
        Livro(titulo="Biologia", ano=2020, autor=autor3, disponivel = True),
        Livro(titulo="Reprodução assexuada dos homens", ano=2000, autor=autor3, disponivel = False)
    ]

    session.add_all([autor1, autor2, autor3])
    session.add_all(livros)
    session.commit()