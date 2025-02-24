class Produto:
    def __init__(self, id , nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade

class Node:
    def __init__(self, produto):
        self.esquerda = None
        self.direita = None
        self.produto = produto

class ArvoreProduto:
    def __init__(self):
        self.raiz = None

    def inserir(self, id,  nome, quantidade):
        produto = Produto(id, nome, quantidade)
        
        if self.raiz is None:
            self.raiz = Node(produto)
        else:
            self._inserir(produto,  self.raiz)


    def _inserir(self, produto, node):

        if produto.id <  node.produto.id:
            if node.esquerda is None:
                node.esquerda =  Node(produto)
            else:
                self._inserir(produto, node.esquerda)
        elif produto.id > node.produto.id:
            if node.direita is None:
                node.direita  = Node(produto)
            else:
                self._inserir(produto, node.direita)
        else:
            node.produto = produto  # se o ID já existe, atualiza as informações do produto
    
    def buscar(self, id):
        return self._buscar(id, self.raiz)
        
    def _buscar(self, id, node):
        if node is None or node.produto.id == id:
            return node
        elif id < node.produto.id:
            return self._buscar(id, node.esquerda)
        else:
            return self._buscar(id, node.direita)
        
arvore = ArvoreProduto()
arvore.inserir(1, "Mouse", 50)
arvore.inserir(2, "Teclado", 30)
arvore.inserir(3, "Monitor", 15)

produtoBuscado1 = arvore.buscar(2)
print(produtoBuscado1.produto.nome) 
