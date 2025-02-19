class Paciente:
    def __init__(self, nome, numero_de_identificacao, saude):
        self.nome = nome
        self.numero_de_identificacao = numero_de_identificacao
        self.saude = saude
        self.next = None

class ListaDePacientes:
    def __init__(self):
        self.head = None
    
    def inserir_paciente(self, nome, numero_de_identificacao, saude):
        novo_paciente  = Paciente(nome, numero_de_identificacao, saude)
        # Se tiver elementos na lista insere no final
        if self.head:
            node  = self.head
            while node.next:
                node = node.next
            node.next = novo_paciente     
        else:
            # se nao tiver nada vai ser o primero
            self.head = novo_paciente
        
    def remover_paciente(self, nome):
        node = self.head
        if node and node.nome == nome:
            self.head = node.next  # Atualiza o head para o próximo nó
            return
        

    def exibir_detalhes(self):
        node = self.head
        while node:
            print(f"Nome: {node.nome}, Número: {node.numero_de_identificacao}, Saúde: {node.saude}")
            node = node.next  # Mova para o próximo nó
        print("Fim da lista")

        prev = None
        while node:
            if node.nome == nome:
                prev.next = node.next
                return
            prev = node
            node = node.next
        

lista = ListaDePacientes()
lista.inserir_paciente("Ana", 1, "Estável")
lista.inserir_paciente("Carlos", 2, "intensivo")
lista.inserir_paciente("Beatriz", 3, "crítico")
lista.exibir_detalhes()
lista.remover_paciente("Ana")

print("\nLista após remover Ana:")
lista.exibir_detalhes()