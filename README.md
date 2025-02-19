# Estruturas de Dados

Praticando a criação das estruturas de dados mais importantes, desde arrays até árvores

## Lista de Compras

Este projeto implementa uma lista de compras em Python. Ele permite que os usuários adicionem e removam itens da lista, além de listar todos os itens adicionados.

## Funcionalidades

- Adicionar item à lista
- Remover item da lista
- Listar itens da lista

## Estrutura do Projeto

- `itens`: Uma lista que armazena os nomes dos itens.
- `quantidades`: Uma lista que armazena as quantidades correspondentes de cada item.
- `ListaDeCompras`: Classe que gerencia a adição, remoção e listagem das listas.

# Estruturas de Dados

Praticando a criação das estruturas de dados mais importantes, desde arrays até árvores.

## Lista de Compras

Este projeto implementa uma lista de compras em Python. Ele permite que os usuários adicionem e removam itens da lista, além de listar todos os itens adicionados.

### Funcionalidades

- Adicionar item à lista
- Remover item da lista
- Listar itens da lista

### Estrutura do Projeto

- `itens`: Uma lista que armazena os nomes dos itens.
- `quantidades`: Uma lista que armazena as quantidades correspondentes de cada item.
- `ListaDeCompras`: Classe que gerencia a adição, remoção e listagem das listas.

## Dia 2: Lista Encadeada

No desafio de hoje, vamos trabalhar com **listas simplesmente encadeadas**.

### O que é uma Lista Encadeada?

Listas simplesmente encadeadas são estruturas de dados dinâmicas compostas por **nós**. Cada nó na lista contém:

- Um **valor** (ou vários valores);
- Um **ponteiro** para o próximo nó da lista.

#### Estrutura da Lista

- O primeiro nó da lista é chamado de **head**;
- O último nó é chamado de **tail**.

Em algumas implementações, a lista pode conter apenas o **head**, sem o **tail**, mas para este desafio, vamos considerar ambas as propriedades.

### Implementação da Classe `Node`

Abaixo está um exemplo de código para um nó da lista:

```python
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximoNo = None
```

## Desafio do Dia: Sistema de Gerenciamento de Pacientes

Seu desafio é criar um **sistema de gerenciamento de pacientes em um hospital** utilizando listas simplesmente encadeadas.

### Requisitos

Cada paciente deve ter:

- **Nome**;
- **Número de identificação**;
- **Estado de saúde** (ex.: "estável", "em tratamento intensivo", "crítico", etc.).

### Funcionalidades

O sistema deve permitir:

- **Adicionar novos pacientes**;
- **Remover pacientes**;
- **Listar todos os pacientes em ordem de chegada**.
