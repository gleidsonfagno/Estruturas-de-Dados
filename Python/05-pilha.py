class Livro:
    def __init__(self, id, nome, numero_de_pagina):
        self.id = id
        self.nome = nome
        self.numero_de_pagina = numero_de_pagina

class PilhaDeLivros:
    def __init__(self):
        self.pilha_de_livros = []

    def adicionar_livro(self, id, nome, numero_de_pagina):
        novo_livro = Livro(id, nome, numero_de_pagina)
        self.pilha_de_livros.append(novo_livro)
        print(f"Novo livro adicionado a pilha {novo_livro.nome}")
    
    def remover_livro(self):
        if len(self.pilha_de_livros) < 1:
            print("A pillha de livros esta vazia")
            return None
        livro_removido = self.pilha_de_livros.pop() 
        print(f"O livro: {livro_removido.nome}, foi removido")
    
    def exibir_livro_do_topo(self):
        if len(self.pilha_de_livros) == 0:
            print("A pillha de livros esta vazia")
            return
        else:
            livro_do_topo = self.pilha_de_livros[-1]
            print(f"\n O Livro do  topo e: {livro_do_topo.nome}\n")

    def mostrar_todos_livros(self):
        if len(self.pilha_de_livros) == 0:
            print("Sem livros na pilha")
            return
        print("Livros disponiveis\n")
        for i in self.pilha_de_livros:
            print(f"Nome: {i.nome} ")
    

pilha = PilhaDeLivros()
pilha.adicionar_livro(1, "A Guerra dos Tronos ",  592)
pilha.adicionar_livro(2, "A Fúria dos Reis", 656)
pilha.adicionar_livro(3, "A Tormenta de Espadas", 884)
pilha.adicionar_livro(4, "O Festim dos Corvos", 644)

print("==========================")

pilha.exibir_livro_do_topo()

pilha.remover_livro()
pilha.remover_livro()
# pilha.remover_livro()
# pilha.remover_livro()

pilha.exibir_livro_do_topo()

print("==========================\n")
pilha.mostrar_todos_livros()
