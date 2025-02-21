class Pedido:
    def __init__(self, id, nome_do_cliente, nome_do_prota, preco, mesa):
        self.id = id
        self.nome_do_cliente = nome_do_cliente
        self.nome_do_prota  = nome_do_prota
        self.preco = preco
        self.mesa = mesa

    def __str__(self):
        return f"Pedido {self.id}: {self.nome_do_cliente} pediu {self.nome_do_prota} - R${self.preco:.2f} na mesa {self.mesa}"

class FilaDePedidos:
    # adicionar
    def __init__(self):
        self.fila  = []
    
    def adicionar(self, id, nome_do_cliente, nome_do_prota, preco, mesa):
        novo_pedido = Pedido(id, nome_do_cliente, nome_do_prota,  preco, mesa)
        self.fila.append(novo_pedido)
        print(f"Novo pedido adicionado: {novo_pedido.nome_do_prota}")

    def remover_pedido(self):
        if not self.fila:
            print("A fila esta vazia")
            return None
        pedido_removido = self.fila.pop(0)
        print(f"O pedido {pedido_removido} foi finalizado")
        return pedido_removido


    def listar_filas(self):
        if not self.fila:
            print("A fila está vazia!")
        else:
            print("\nPedidos na fila:")
            for pedido in self.fila:
                print(pedido)

fila = FilaDePedidos()
print("======== Fila antes de adicionar pedidos========")
fila.listar_filas()

print("========Adicionando Pedidos na fila========\n")
fila.adicionar(1, "João Silva", "Hambúrguer Duplo", 30.99, 8)
fila.adicionar(2, "Maria Oliveira", "Pizza Calabresa", 45.50, 2)
fila.adicionar(3, "Carlos Souza", "Sushi Completo", 60.00, 7)
fila.adicionar(4, "Ana Pereira", "Massa à Carbonara", 35.75, 11)
fila.adicionar(5, "Lucas Mendes", "Salada Caesar", 20.99, 3)
print("======== Fila Depois de adicionar pedidos========")
fila.listar_filas()

print("======== Pedidos Finalizados  ========\n")
fila.remover_pedido()
fila.remover_pedido()

fila.listar_filas()