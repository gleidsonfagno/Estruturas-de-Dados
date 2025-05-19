from __future__ import  annotations
from typing import Any


# tipo node
EMPYT_NODE_VALUE = "__EMPYT_NODE_VALUE__"

class EmptyQueueError(Exception):
    ...


class Node:
    def __init__(self, value: Any) ->None:
        self.value = value
        self.next: Node

    def __repr__(self) -> str:
        return f"{self.value}"

    def  __bool__(self) -> bool:
        return bool(self.value != EMPYT_NODE_VALUE)

class Queue:
    def __init__(self) -> None:
        self.first: Node = Node(EMPYT_NODE_VALUE) #primerio
        self.last: Node = Node(EMPYT_NODE_VALUE) # ultimo
        self._count = 0

        # nessa funça adicionaremos
    def push(self, node_value: Any) -> None:
        new_node = Node(node_value) #novo node

        # se nao ter valorno primeiro node esse vai ser  primeiro
        if not self.first:
            self.first = new_node

        # se for vazio na primeiravez vai ser  igual o first vazio de pois ele vai para o else para  adicionar  o  proximo no final da fila
        if not self.last:
            self.last = new_node
        else:
            # o proximo node
            self.last.next = new_node
            self.last = new_node 

        self._count +=1
        
    def pop(self) -> Node:
        # se existe no elemento
        if not self.first:
            raise EmptyQueueError("Empty Queue")

        first = self.first

        # se existir o atributo next o firt que vai ser o prximo elemento esse proximo vaiser o primeiro
        if hasattr(self.first, "next"):
            self.first = self.first.next
        else:
            self.first = Node(EMPYT_NODE_VALUE)
        
        self._count -= 1
        return first

    def peek(self) -> Node:
        return self.first

        # tamanho da lista 
    def __len__(self) -> int:
        return self._count
    
    # set em  algum valor na lista 
    def __bool__(self) -> bool:
        return bool(self._count)
    
    # iterar  na lista
    def __iter__(self) -> Queue:
        return self

    # par usar  o iterador
    def __next__(self) -> Any:
        try:
            next_value= self.pop()
            return next_value
        except EmptyQueueError:
            raise StopIteration

    def __repr__(self) -> str:
        if not self.first:
            return 'Queue()'
        return f'Queue({self.first}, {self.last})'

if __name__ == "__main__":
    queue = Queue()
    queue.push('A')
    queue.push('B')
    queue.push('C')

    print('FORA DO FOR', next(queue))

    for item in queue:
        print(item)

    print(queue)
