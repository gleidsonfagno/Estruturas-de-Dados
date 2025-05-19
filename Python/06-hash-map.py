class Jogador:
    def __init__(self, id, nome, pontos):
        self.id = id
        self.nome =  nome
        self.pontos  = pontos

class UsuariosCadastrados:
    def __init__(self):
        self.usuarios_cadastrado = {}

    
    def adicionar_jogador(self, id,  nome, pontos):
        novo_jogador = Jogador(id, nome, pontos)

        self.usuarios_cadastrado[novo_jogador.id] = novo_jogador
        print(f"Novo jogador Nome:  {nome}, pontos {pontos}: id {id}")
        

    def remover_jogador(self, id):
        try:
            if self.usuarios_cadastrado[id].id != id:
                print("erro")
            else:
                print(f"usuário nome {self.usuarios_cadastrado[id].nome}, o seus  pontos: {self.usuarios_cadastrado[id].pontos} foi removido")

                del self.usuarios_cadastrado[id]
        except KeyError:
            print(f"Esse erro eporque você digitou o id errado do usuario")

    def atualizar_pontuacao(self, id, pontos):
        # print(f" {self.usuarios_cadastrado[id].id != id}")
        if self.usuarios_cadastrado[id].id != id:
            print("Usuário nao enccontrado")
        self.usuarios_cadastrado[id].pontos += pontos
        print(f"Pontuaçao de {self.usuarios_cadastrado[id].nome}, atualizado para {self.usuarios_cadastrado[id].pontos}")

    def exibir_jogadores(self):
        for chave, valor in self.usuarios_cadastrado.items():
            print(f"Usuarios: {chave} tem o valor {valor.nome}, Pontos {valor.pontos}")
        return 

    
    def order_jogadore(self):

        ordem_decresente = sorted(self.usuarios_cadastrado.values(), key=lambda jogador: jogador.pontos, reverse=True)

        print("jogadores em ordem decresente")
        for jogador in ordem_decresente:
            print(f"ID: {jogador.id}, Nome: {jogador.nome}, Pontos: {jogador.pontos}")

        vencedor = ordem_decresente[0]
        print(f"\nVencedor: {vencedor.nome}, Pontos: {vencedor.pontos}")


dicionario = UsuariosCadastrados()
print("\n")
dicionario.adicionar_jogador(1, "Tereza", 11)
dicionario.adicionar_jogador(2, "Joâo", 3)
dicionario.adicionar_jogador(3, "Maria", 5)
dicionario.adicionar_jogador(4, "Matiuda", 5)
print("\n")

dicionario.remover_jogador(1)
dicionario.remover_jogador(2)
print("\n")
print("===========Usuarios cadastrados=============")
print("\n")
dicionario.exibir_jogadores()

print("\n")
dicionario.atualizar_pontuacao(3, 22)

print("\n")
dicionario.order_jogadore()

