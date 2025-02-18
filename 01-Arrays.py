
itens = []
quantidades = []

class  ListaDeCompras:
    def __init__(self, nome, quantidade) -> None:
        self.nome = nome
        self.quantidade = quantidade
    
    def adicionar_item(self):
        itens.append(self.nome)
        quantidades.append(self.quantidade)
        return 
        
    @staticmethod
    def remove_item(nome):
        if nome in itens:
            index = nome.index(nome)
            itens.remove(nome)
            quantidades.pop(index)
            rem = quantidades.pop(index)
            print(f"O item: {nome} foi removido\n")
        else:
            print(f"{nome} não encontrado na lista.")
        return  

    @staticmethod
    def listar_itens():
        print("============== Sua lista de compras esta aqui =======\n")

        for item, quantidade  in zip(itens, quantidades):
            print(f"Item: {item}, Quantidade: {quantidade}")

def iniciar_progama():
  
        while True:
            ListaDeCompras.listar_itens()
            
            print("Digite 1 para Inserir | 2 para Remover | 3 para sair")
            res = int(input())

            if res == 1:
                print("Digite o nome do produto para inserir")
                item = input(str())
                print("Digite quantidade desejada")
                quantidade_item = input(int())

                add = ListaDeCompras(item, quantidade_item)
                add.adicionar_item()

            elif res == 2:
                print("Digite o nome do produto para remover")
                item = input(str())
                ListaDeCompras.remove_item(item)

            elif res == 3:
                print("Saindo")
                break
            
iniciar_progama()
