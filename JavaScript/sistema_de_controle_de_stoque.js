class Node {
  constructor(product) {
    this.product = product;
    this.next = null;
    this.prev = null;
  }
}

class Estoque {
  constructor(value) {
    const newNode = new Node(value);

    this.head = newNode;
    this.tail = this.head;
    this.length = 1;
  }

  // função que adiciona no final da lista
  push(value) {
    const node = new Node(value);
    // se nao tiver nada o na lista
    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      // O Proximo no recebe o novo dados
      this.tail.next = node;
      node.prev = this.tail; // o novo no tem o prev apontado paro o anterio
      this.tail = node; // e aponta para o novo que vira
      // | 1 | <--> | 2 | <--> | 3 | <--> | 4 |
    }

    this.length++;
    return this;
  }

  pop() {
    if (!this.length === 0) {
      return undefined;
    }

    let temp = this.tail;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = this.tail.prev;
      this.tail.next = null;
      temp.prev = null;
    }
    this.length--;
    return temp;
  }

  updated(nome, novoPreco, novaQuantidade) {
    let item = this.head;

    if (!this.head) {
      return undefined;
    }

    // equanto tiver dados no item vai percorrer os dados e verificar se o nome passado e igual o do estoque e se tiver algum produto adiciona os novos dados no estoque
    while (item) {
      if (item.product && item.product["nome"] === nome) {
        item.product.preco = novoPreco;
        item.product.quantidade_em_estoque = novaQuantidade;
        return item.product;
      }
      item = item.next;
    }

    return item;
  }

  read() {
    let current = this.head;
    let produtos = [];
    if (!current) {
      return undefined;
    }
    // se current for verdadeiro  vai percorrer e verificar se tem  algum produto e adiciona os dados em produtos e retorna
    while (current) {
      if (current.product) {
        produtos.push(current.product);
      }
      current = current.next;
    }

    return produtos;
  }
}

const sistemaDeEstoque = new Estoque();

sistemaDeEstoque.push({
  nome: "Amortecedor",
  codigo_de_barras: "1234567890",
  preco: 545.99,
  quantidade_em_estoque: 10,
});

console.log(sistemaDeEstoque.read());

sistemaDeEstoque.push({
  nome: "Pastilha de Freio",
  codigo_de_barras: "0987654321",
  preco: 120.5,
  quantidade_em_estoque: 25,
});

// console.log(sistemaDeEstoque.pop());
// console.log(sistemaDeEstoque.pop());
console.log(sistemaDeEstoque.updated("Amortecedor", 286.0, 20));

console.log(sistemaDeEstoque.read());
