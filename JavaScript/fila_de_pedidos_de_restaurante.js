class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor(value) {
    const newNode = new Node(value);
    this.first = newNode;
    this.last = newNode;
    this.length = 1;
  }

  push(value) {
    const newItem = new Node(value);

    if (this.length === 0) {
      this.first = newItem;
      this.last = newItem;
    }

    this.last.next = newItem;
    this.last = newItem;
    this.length++;

    return this;
  }

  pop() {
    let temp = this.first;

    if (this.length === 0) {
      return undefined;
    }

    if (this.length === 1) {
      this.first = null;
      this.last = null;
    }

    this.first = this.first.next;
    temp.next = null;
    this.length--;
    return temp;
  }

  read() {
    let current = this.first;
    let pedidos = [];

    if (!current) {
      return undefined;
    }

    while (current) {
      if (current.value) {
        pedidos.push(current.value);
      }
      current = current.next;
    }
    return pedidos;
  }
}

const theQueue = new Queue({
  numero_do_pedido: 1232,
  nome: "fagno",
  prato: "Pizza 4 queijo",
  mesa: 1,
});

theQueue.push({
  numero_do_pedido: 4567,
  nome: "Leyde",
  prato: "Pizza 4 queijo",
  mesa: 2,
});

theQueue.push({
  numero_do_pedido: 8910,
  nome: "Rafael",
  prato: "Pizza frango",
  mesa: 3,
});


console.log(theQueue.pop());

console.log(theQueue.read());
