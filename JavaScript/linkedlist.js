class Node {
    constructor(data){
        this.data = data
        this.next = null
    }
}

class FilaDePacientes {
    constructor () {
        this.head = null
        this.tail = null
        this.count = 0
    }
    // Adicionar novos pacientes
    append(paciente) {
        let novoPaciente = new Node(paciente)
        // se head for null adiciona no inicio
        if(!this.head) {
            this.head = novoPaciente
            this.tail = novoPaciente
        }else { // se não pula para o proximo e adiciona
            this.tail.next = novoPaciente
            this.tail = novoPaciente
        }

        this.count++
        // console.log(this.head )
    }

    // Remover pacientes
    removeAt() {
        let temp = this.head
        
        this.head = this.head.next
        temp.next = null
        this.count--
        if(this.count === 0){
            this.tail = null
        }
        return temp
    }

    read() {

        let paciente = this.head
        while(paciente) {
            console.log(`Nome: ${paciente.data.nome}, CPF: ${paciente.data.cpf}, ${paciente.data.saude}.`)
            paciente = paciente.next
        }
        console.log("Fim da lista")

    }

}

const listPacientes = new FilaDePacientes()

listPacientes.append({
  nome: "Bagal",
  cpf: "123.456.789-00",
  saude: "Critico"
}
)

listPacientes.append({
  nome: "jojota",
  cpf: "123.456.789-00",
  saude: "Estavel"
}
)


listPacientes.append({
  nome: "Joao zinho",
  cpf: "123.456.789-00",
  saude: "Estavel"
}
)

listPacientes.removeAt(0)
// console.log(listPacientes)
listPacientes.read()