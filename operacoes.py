from sqlalchemy import select

from models import Livro, Autor

def emprestar_livro(session, titulo):
    sele_livro = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalar(sele_livro)

    if livro:
        if livro.disponivel:
            livro.disponivel = False
            session.commit()
            print(f"o livro {livro.titulo} foi emprestado e agora sua disponibilidade é {livro.disponivel}")    
        else: print(" livro ja emprestado")
    else: print('não existe esse livro ai')

def devolver_livro(session, titulo):
    sele_livro = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalar(sele_livro)
    if livro:
        if not livro.disponivel:
            livro.disponivel = True
            session.commit()
            print(f"o livro {livro.titulo} foi devolvido e agora sua disponibilidade é {livro.disponivel}")
        else: 
            print("livro disponivel")
    else: 
        print('não existe esse livro ai')


