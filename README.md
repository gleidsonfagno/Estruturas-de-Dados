# **Estruturas de Dados**

Praticando a criação das estruturas de dados mais importantes, desde arrays até árvores.

## **Lista de Compras**

Este projeto implementa uma lista de compras em Python. Ele permite que os usuários adicionem e removam itens da lista, além de listar todos os itens adicionados.

### **🚀 Funcionalidades**

- Adicionar item à lista;
- Remover item da lista;
- Listar itens da lista.

### **Estrutura do Projeto**

- `itens`: Uma lista que armazena os nomes dos itens.
- `quantidades`: Uma lista que armazena as quantidades correspondentes de cada item.
- `ListaDeCompras`: Classe que gerencia a adição, remoção e listagem das listas.

---

## **Dia 2: Lista Encadeada**

No desafio de hoje, vamos trabalhar com **listas simplesmente encadeadas**.

### **O que é uma Lista Encadeada?**

Listas simplesmente encadeadas são estruturas de dados dinâmicas compostas por **nós**. Cada nó na lista contém:

- Um **valor** (ou vários valores);
- Um **ponteiro** para o próximo nó da lista.

#### **Estrutura da Lista**

- O primeiro nó da lista é chamado de **head**;
- O último nó é chamado de **tail**.

Em algumas implementações, a lista pode conter apenas o **head**, sem o **tail**, mas para este desafio, vamos considerar ambas as propriedades.

### **Implementação da Classe `Node`**

Abaixo está um exemplo de código para um nó da lista:

```python
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximoNo = None
```

---

## **Desafio do Dia: Sistema de Gerenciamento de Pacientes**

Seu desafio é criar um **sistema de gerenciamento de pacientes em um hospital** utilizando **listas simplesmente encadeadas**.

### **📝 Requisitos**

Cada paciente deve possuir os seguintes atributos:

- **Nome**;
- **Número de identificação**;
- **Estado de saúde** *(ex.: "Estável", "Em tratamento intensivo", "Crítico", etc.)*.

### **🚀 Funcionalidades**

O sistema deve permitir as seguintes operações:

- **Adicionar novos pacientes** à lista;
- **Remover pacientes** da lista;
- **Listar todos os pacientes** em ordem de chegada.

📌 **Observação:** O sistema deve manter a ordem dos pacientes baseada na sequência de entrada.

---

## **Dia 3: Sistema de Controle de Estoque**

O desafio para o dia é implementar um **sistema de controle de estoque** de uma loja usando **listas duplamente encadeadas**.

### **📝 Requisitos**

Cada produto deve ter:

- **Nome**;
- **Código de barras**;
- **Preço**;
- **Quantidade em estoque**.

### **🚀 Funcionalidades**

O sistema deve permitir:

- **Adicionar novos produtos**;
- **Remover produtos**;
- **Atualizar a quantidade em estoque**;
- **Listar todos os produtos**.

## **Dia 4: Fila de Pedidos de Restaurante**

Desafio do Dia: Sistema de Fila de Pedidos
Hoje, vamos trabalhar com filas, uma estrutura de dados que segue o princípio "primeiro a entrar, primeiro a sair" (FIFO). Neste desafio, implementaremos uma fila para gerenciar os pedidos de um restaurante.

### 📝 **Requisitos**
Cada pedido deve ser representado por:

- **Número do pedido;**
- **Nome do cliente;**
- **Nome do prato;**
- **Mesa em que o pedido foi feito.**

### 🚀 **Funcionalidades**
O sistema deve permitir:

- **Adicionar novos pedidos à fila;**
- **Remover pedidos que já foram entregues;**
- **Listar todos os pedidos na ordem em que foram feitos.**

## **Dia 5: Pilha de Livros**

Desafio do Dia: Gerenciamento de Pilha de Livros
Hoje, vamos trabalhar com **pilhas**, uma estrutura de dados que segue o princípio **"último a entrar, primeiro a sair"** (LIFO - *Last In, First Out*). Neste desafio, implementaremos uma pilha para gerenciar os livros da saga **As Crônicas de Gelo e Fogo** (Game of Thrones).

### 📝 **Requisitos**
Cada livro deve ser representado por:

- **Título do livro;**
- **Número de páginas.**

### 🚀 **Funcionalidades**
O sistema deve permitir:

- **Adicionar novos livros à pilha (push);**
- **Remover livros do topo da pilha (pop);**
- **Exibir o livro que está no topo (peek);**
- **Listar todos os livros na pilha.**

### 🔎 **O que é uma Pilha?**
Uma **pilha** funciona como uma pilha de pratos: você sempre coloca um novo prato no topo, e quando precisa remover, tira o prato que está no topo primeiro. Assim, a ordem de remoção é **o inverso da ordem de inserção**.

### 📌 Operações principais:
- **Push**: Adiciona um novo livro ao topo da pilha.
- **Pop**: Remove o livro do topo da pilha.
- **Peek**: Apenas visualiza o livro do topo, sem removê-lo.

## **Dia 6: Sistema de Pontuação de Jogos Online**

**Desafio do Dia:** Sistema de Pontuação de Jogos Online  
Hoje, vamos trabalhar com **hashmaps** para implementar um sistema de pontuação para jogos online.

### 📝 **Requisitos**
Cada jogador deve ser representado por:

- **Nome de usuário**;
- **Número de pontos**.

### 🚀 **Funcionalidades**

O sistema deve permitir:

- **Adicionar novos jogadores ao sistema**;
- **Atualizar a pontuação de jogadores existentes**;
- **Remover jogadores**;
- **Listar todos os jogadores em ordem decrescente de pontos**;
- **Determinar o jogador vencedor**, ou seja, o que tem mais pontos.

### 🔎 **O que é um HashMap?**

Um **HashMap** é uma estrutura de dados que armazena valores associados a chaves, permitindo o acesso eficiente aos valores por meio dessas chaves.

### 📌 **Operações principais:**

- **Adicionar/Atualizar**: Adiciona ou atualiza um jogador no sistema.
- **Remover**: Remove um jogador do sistema.
- **Listar**: Exibe todos os jogadores em ordem de pontos.
- **Vencedor**: Exibe o jogador com a maior pontuação.

## **Dia 7: Sistema de Gerenciamento de Estoque com Árvore Binária**

O desafio do dia é implementar um **sistema de gerenciamento de estoque** para uma loja online usando **árvores binárias**.

### **📝 Requisitos**

Cada produto deve ter:

- **ID do produto** (um número inteiro único);
- **Nome do produto**;
- **Quantidade em estoque**.

### **🚀 Funcionalidades**

O sistema deve permitir:

- **Adicionar novos produtos à árvore**;
- **Atualizar as informações de um produto existente** caso o ID já esteja na árvore;
- **Buscar um produto pelo ID e exibir suas informações** (opcional).

- [binarytree](https://pypi.org/project/binarytree/)
- [arvore](https://mange.ifrn.edu.br/python/aprenda-com-py3/capitulo_20.html)
- [Artigo sobre arvore](https://empresas.alura.com.br/e3t/Ctc/I8+113/d2z6gD04/VVxP406FchPLW75ZbsM9lZfRTW6wcfC_5snq9yN3rtP7-3qgyTW95jsWP6lZ3kyW629Dp82Vj3KyVxm6fZ4LnJBCN1KDf1LssWBwW8dGNWT39jPbTW59mNTh5sN16xW567QTQ7h6Y5pW7n6VnC5GgVvbW3xHN2w2XM0n1W2cGsnt6w9cT_N2qLPPYDHxmDW6mwTf63_QjJfW289CjH2YPV2sW6Wv5f37Q21TxVZL5jX3vC1zHW4FftbJ2QllbPW3LLQ2N9bNp72W3JLR0x8fv1vfW8ngT4q8b3jpJW5YFv5J6fKBQbW6n1nq81k_h1kN4hqlR9YcdNfW7h3brc7nl6hLW2YfdBB2FTF9wW4fC9Lp5hfK2mW18HP2M1Yt2YRN1_6KY35SgTVN2bTPqXRCMMwW432Rz62d4QbMW6QJqyN6sHqdwW2KfCmw4LBCzyf955H3K04)