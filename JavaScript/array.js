class ListaDeCompras {
  constructor() {
    this.data = [];
    this.length = 0;
  }
  // Adicionar item à lista; [x]
  push(item) {
    this.data.push(item);
    this.length++;
  }
  //  Remover item da lista;
  removeFirstPosition() {
    this.data.shift();
    this.length--;
  }
  //  Remover item da lista pelo index;
  removeItem(index) {
    const item = this.data[index];

    if (!item) {
      return "Erro Item nao existe";
    }

    console.log(`O item : ${item} foi removido`);
    this.length--;
  }
  // Listar itens da lista.
  showList() {
    console.log("---------Lista de compras-----------");
    for (let i = 0; i < this.data.length; i++) {
      console.log(this.data[i] + " ,");
    }
  }
}

const newList = new ListaDeCompras();
newList.push("frango");
newList.push("Arroz");
newList.push("pasta de amendoin");
newList.showList();

newList.removeFirstPosition();
newList.removeItem(1);

newList.showList();