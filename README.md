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


E aí, gleidson fagno da conceicao pinheiro, conseguiu desenvolver o desafio do primeiro dia e já está tudo pronto para o próximo?

Só pra garantir, vou deixar sempre a minha resolução lá no final do e-mail, beleza? Assim você pode comparar com a sua, mas não esqueça de compartilhar comigo as resoluções, quero ver também!

Hoje é o segundo dia do seu desafio #7DaysOfCode de Estruturas de Dados, bora praticar?

No dia de hoje, você vai praticar outra estrutura de dados, a lista encadeada! Sendo mais específica, a lista simplesmente encadeada. Vamos entender o que ela é.

Listas simplesmente encadeadas são estruturas de dados dinâmicas compostas por nós. Cada nó na lista contém um valor (ou valores) e um ponteiro para o próximo nó. Veja uma exemplificação abaixo:

b0f4166c-9a8d-450f-bd4f-4a00333258e9
O primeiro nó da lista é denominado de “head”, enquanto o último nó da lista é chamado de “tail”. Vale lembrar que você pode encontrar listas encadeadas que possuem apenas sua implementação com o “head”, sem o “tail”. Mas para este desafio, vamos considerar “head” e “tail”, tudo bem?

Abaixo, veja um código que especifica uma classe chamada Node, representando um único nó, que recebe um valor como parâmetro. O valor do atributo proximoNo é None, pois é preciso manipular esse valor diretamente na lista encadeada.

class Node:
  def __init__(self, valor):
    self.valor = valor
    self.proximoNo = None

O desafio para o dia de hoje é implementar um sistema de gerenciamento de pacientes em um hospital usando listas simplesmente encadeadas.

Cada paciente deve ter um nome, um número de identificação e o estado de saúde atual do paciente, como “estável”, “em tratamento intensivo”, “em estado crítico”, entre outros.

O sistema deve permitir adicionar novos pacientes, remover pacientes e listar todos os pacientes em ordem de chegada.

Obs: não é necessário criar nenhuma interface do usuário para esse desafio (a não ser que você queira), o objetivo é executar apenas um único arquivo.

Vamos lá?

DICA
Você pode criar uma classe chamada Paciente (representando um único nó) e outra classe chamada ListaDePacientes (representando a lista) para resolver este desafio.


Crie a estrutura do nó: o nó deve ter os campos necessários para armazenar as informações de cada paciente, bem como um ponteiro para o próximo nó (paciente) na lista;

Crie a estrutura da lista de pacientes e escreva funções para adicionar e remover pacientes: estas funções devem criar ou excluir um nó da lista encadeada e ajustar os ponteiros corretamente;

Escreva uma função para listar todos os pacientes: esta função deve percorrer a lista encadeada e exibir as informações de cada paciente;

Considere casos especiais: certifique-se de pensar em casos especiais que possam ocorrer, como adicionar ou remover o primeiro nó da lista, ou tentar remover um paciente que não existe na lista;

Teste o seu código: uma vez que você tenha escrito as funções necessárias, é importante testá-las para garantir que elas funcionem corretamente. Tente adicionar, remover e listar pacientes em diferentes cenários para garantir que tudo funcione corretamente.

Como um desafio extra, você pode tentar refazer este desafio sem a propriedade tail, apenas com a propriedade head.

Para este caso, é necessário percorrer toda a lista para saber qual é o último paciente. Será que você encara? Bora lá!

EXTRA
Se você está com dúvidas sobre este tópico ou algum outro relacionado a estrutura de dados, recomendo ler este artigo da Alura que faz uma introdução às principais estruturas de dados.

RESPOSTA DO EXERCÍCIO DO DIA 1
- Solução do Dia 1

Ah, lembre-se de compartilhar o seu código no seu GitHub e nas suas redes sociais com a hashtag #7DaysOfCode.

Bom desafio, te vejo amanhã nesse mesmo horário!

Giovanna Moeller
Engenheira de Software