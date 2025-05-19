class Produto:
    def __init__(self, nome, codigo_de_barra, preco, quantidade):
        self.nome = nome
        self.codigo_de_barra = codigo_de_barra
        self.preco = preco
        self.quantidade = quantidade

        self.anterio = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar(self, nome, codigo_de_barra, preco, quantidade):
        novo_produto = Produto(nome, codigo_de_barra, preco, quantidade)
        # se a lista estiver  vazi vai ser adicionadona cabe e na cauda
        if self.head is None:
            self.head = novo_produto
            self.tail = novo_produto
        else:
            # caso contrario e adicionado no final
            self.tail.proximo = novo_produto
            novo_produto.anterio = self.tail
            self.tail = novo_produto
        
        # remover peça pelo codigo  de barra
    def remover_peca(self, codigo_de_barra):
        peca_atual = self.head
        # esse loop pra percorre a lista até achar 
        while peca_atual:
            if peca_atual.codigo_de_barra == codigo_de_barra:
                # remove oprimeiro no head
                if peca_atual == self.head:
                    self.head = peca_atual.proximo
                    # senao  tiver nada no head remove do tail 
                    if self.head:
                        self.head.anterio = None
                    else:
                        self.tail = None

                # remover o utimo no tail
                elif peca_atual == self.tail:
                    self.tail = peca_atual.anterio
                    if self.tail:
                        self.tail.proximo = None
                # remove o no do meio 
                else:
                    # O anterior aponta para o próximo
                    peca_atual.anterio.proximo = peca_atual.proximo
                    # O próximo aponta para o anterio
                    peca_atual.proximo.anterio = peca_atual.anterio 
                
                print(f"Peça com código {codigo_de_barra} removida.\n")
                return

            peca_atual = peca_atual.proximo
        print(f"Peça com código {codigo_de_barra} não encontrada.")


    def atualizar_estoque(self, codigo_de_barra, quantidade):
        produto_atualizado = self.head
        quantidade_atualizada = quantidade

        while produto_atualizado:
            
            if produto_atualizado.codigo_de_barra == codigo_de_barra:
                if quantidade_atualizada > 0:
                    print(f"Nova quantidade adiconada aou produto com codigo: {codigo_de_barra}\n")
                    produto_atualizado.quantidade += quantidade_atualizada

                elif quantidade_atualizada < 0:
                    if produto_atualizado.quantidade < abs(quantidade_atualizada):
                        print(f"Nao podemos subtrair esse  valor: {quantidade} e maior que temos  em estoque\n")
                    else:
                        print(f"Nova quantidade {quantidade_atualizada} removida aou produto com codigo: {codigo_de_barra}")
                        produto_atualizado.quantidade += quantidade_atualizada

                return
            produto_atualizado = produto_atualizado.proximo

        print(f"Peça com código {codigo_de_barra} não encontrada.\n")
            

    def Listar_pecas(self):
        if self.head is None:
             print("Nao há nehuma peça no estoque")
        else:
            peca_atual= self.head
            while peca_atual is not  None:
                print(f"Nome: {peca_atual.nome},\n Codigo de barra: {peca_atual.codigo_de_barra},\n Preço: {peca_atual.preco},\n Quantidade: {peca_atual.quantidade}\n ")
                # a  peca atual gurada  o valor da proxima 
                peca_atual = peca_atual.proximo

lista = ListaDuplamenteEncadeada()
lista.Listar_pecas()
print("======= Produtos adicionados =======\n")
lista.adicionar("Cabo de freio", 1234, 23.99, 12)
lista.adicionar("Penel Levorin", 456, 390, 22)
lista.adicionar("Rolamento XTZ", 789, 390, 22)

lista.Listar_pecas()
print("======= Produtos removidos!=======\n")

# lista.remover_peca(789)
# lista.remover_peca(456)
lista.remover_peca(1234)

lista.Listar_pecas()
print("======= Produtos atualizados=======\n")
lista.atualizar_estoque(789, -19)
lista.atualizar_estoque(789, -30)
lista.atualizar_estoque(789, 100)
lista.atualizar_estoque(456,  20)

lista.atualizar_estoque(902222,  20)
lista.Listar_pecas()