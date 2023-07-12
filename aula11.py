

""" lista de tarefas """

tarefas = []
while True:
    print("\n1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Deletar Tarefa")
    print("4. Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    elif opcao == 2:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")
    elif opcao == 3:
        num_tarefa = int(input("Digite o número da tarefa a ser deletada: ")) - 1
        if 0 <= num_tarefa < len(tarefas):
            del tarefas[num_tarefa]
            print("Tarefa deletada!")
        else:
            print("Número inválido!")
    elif opcao == 4:
        print("Até mais!")
        break
    else:
        print("Opção inválida!")