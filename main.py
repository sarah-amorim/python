def adicionar_tarefa(array_de_tarefas, nome_da_tarefa):
    tarefa = {'tarefa': nome_da_tarefa, 'completada': True}
    array_de_tarefas.append(tarefa)
    print(f'Tarefa "{nome_da_tarefa}" foi adicionada com sucesso!')


def visualizar_tarefas(array_de_tarefas):
    print('\nTodas as tarefas:')
    for indice, tarefa in enumerate(array_de_tarefas, start=1):
        if tarefa['completada'] == True:
            status = '✓'
        else:
            status = ''
        nome_da_tarefa = tarefa['tarefa']
        print(f'{indice}. [{status}] {nome_da_tarefa}')

todas_as_tarefas = []

while True:
    print('\nMenu do Gerenciador de Lista de Tarefas')
    print('1. Adicionar tarefa')
    print('2. Ver todas_as_tarefas')
    print('3. Atualizar tarefa')
    print('4. Completar tarefa')
    print('5. Deletar todas_as_tarefas completadas')
    print('6. Sair')

    escolha = int(input('Digite a sua escolha: '))

    if escolha == 1:
        nome = input('Digite o nome da tarefa que deseja adicionar: ')
        adicionar_tarefa(todas_as_tarefas, nome)
    elif escolha == 2:
        visualizar_tarefas(todas_as_tarefas)
    elif escolha == 6:
        break

print('Fim do programa!')
