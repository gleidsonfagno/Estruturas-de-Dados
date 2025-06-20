// Resolução sando objetos segundo o livro Estruturas_de_dados_e_algoritmos_com_JavaScript_Groner,_Loiane_

class Stack {
  constructor() {
    this.items = {};
    this.length = 0;
  }

  push(element) {
    this.items[this.length] = element;
    this.length++;
  }

  pop() {
    if (this.length === 0) {
      return undefined;
    }
    this.length--;
    const result = this.items[this.length];
    delete this.items[this.length];
    return result;
  }

  peek() {
    if (this.length === 0) {
      return undefined;
    }

    return this.items[this.length - 1];
  }

  red() {
    console.log(this.items);
  }
}

let theStack = new Stack();
theStack.push({ nome: "A Guerra dos Tronos", pagina: 592 });
theStack.push({ nome: "A Fúria dos Reis", pagina: 656 });
theStack.push({ nome: "A Tormenta de Espadas", pagina: 884 });
theStack.push({ nome: "O Festim dos Corvos", pagina: 644 });

console.log(theStack.pop());
console.log(theStack.red());
console.log(theStack.peek());

// 

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class newStack {
  constructor(value) {
    const newNode = new Node(value);
    this.first = newNode;
    this.length = 1;
  }

  push(value) {
    const newItem = new Node(value);

    if (this.length === 0) {
      this.first = newItem;
    } else {
      newItem.next = this.first;
      this.first = newItem;
      this.length++;
    }
  }

  pop() {
    if (this.length === 0) {
      return undefined;
    } else {
      let temp = this.first;
      this.first = this.first.next;
      temp.next = null;
      this.length--;
      return temp;
    }
  }

  read() {
    let current = this.first;
    let pedidos = [];
    if (!current) {
      return undefined;
    }

    while (current) {
      pedidos.push(current.value);
      current = current.next;
    }

    for(let i = 0 ;  i   < pedidos.length; i++){
        console.log(pedidos[i])
    }
  }
}

let myStack = new newStack({ nome: "A Guerra dos Tronos", pagina: 592 })

myStack.push({ nome: "A Fúria dos Reis", pagina: 656 });
myStack.push({ nome: "A Tormenta de Espadas", pagina: 884 });
myStack.push({ nome: "O Festim dos Corvos", pagina: 644 });

myStack.read()
console.log(myStack.pop())
