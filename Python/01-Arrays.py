
itens = []
quantidades = []

class  ListaDeCompras:
    def __init__(self, nome, quantidade) -> None:
        self.nome = nome
        self.quantidade = quantidade
    
    def adicionar_item(self):
        itens.append(self.nome)
        quantidades.append(self.quantidade)

    # Um método estático é um método que pode ser chamado sem a instancia da classe.
    @staticmethod
    def remove_item(nome):
        if nome in itens:
            index = nome.index(nome)
            item_removido = itens.pop(index)
            quantidade_removidsa = quantidades.pop(index)
            print(f"O item: {item_removido} foi removido e sua quantidade: {quantidade_removidsa} \n")
        else:
            print(f"{nome} não encontrado na lista.")
        return  

    @staticmethod
    def listar_itens():
        print("============== Sua lista de compras esta aqui =======\n")

        for item, quantidade  in zip(itens, quantidades):
            print(f"Item: {item}, Quantidade: {quantidade}")
            print("=====================================================")

    @staticmethod
    def validar_nome(nome):
        # Caso nao prencha nada retorna false 
        return bool(nome.strip())

    def validar_numero(quantidade):
        # O valor digitado e transformado em int e retorna a validação True se o Valor e maior que 0
        try:
            quantidade_item = int(quantidade)
            return quantidade_item > 0 
        except ValueError:
            return False

def iniciar_progama():
        while True:
            ListaDeCompras.listar_itens()
            
            try:
                print("Digite 1 para Inserir | 2 para Remover | 3 para sair")
                res = int(input())
                # adicionar
                if res == 1:
                    print("Digite o nome do produto para inserir")
                    item = str(input())
                    # Emquanto o usário nao digitar um valor True ano sai do loop
                    while not ListaDeCompras.validar_nome(item):
                        print("Nome inválido! Tente novamente.")
                        item = str(input())

                    print("Digite quantidade desejada")
                    quantidade_item = int(input())
                    # O valor tem queser maior que 0 e tem que ser inteiro 
                    while not ListaDeCompras.validar_numero(quantidade_item):
                        print("Numero inválida! Tente novamente.")
                        quantidade_item = int(input())

                    add = ListaDeCompras(item, quantidade_item)
                    add.adicionar_item()
                    
                # remover
                elif res == 2:
                    print("Digite o nome do produto para remover:")
                    item = str(input())
                    ListaDeCompras.remove_item(item)

                elif res == 3:
                    print("Saindo")
                    break
            except ValueError:
                print("Opção inválida! Tente novamente.\n")
            except KeyboardInterrupt:
                print("Opção inválida! Tente novamente.\n")
            
            
iniciar_progama()
