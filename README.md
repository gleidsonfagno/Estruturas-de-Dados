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
