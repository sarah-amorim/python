todas_as_tarefas = []


def adicionar_tarefa(array_de_tarefas, nome_da_tarefa):
    tarefa = {'tarefa': nome_da_tarefa, 'completada': False}
    array_de_tarefas.append(tarefa)
    print(f'Tarefa "{nome_da_tarefa}" foi adicionada com sucesso!')
    return


def visualizar_tarefas(array_de_tarefas):
    print('\nTodas as tarefas:')
    for indice, tarefa in enumerate(array_de_tarefas, start=1):
        if tarefa['completada']:
            status = '✓'
        else:
            status = ' '
        nome_da_tarefa = tarefa['tarefa']
        print(f'{indice}. [{status}] {nome_da_tarefa}')
    return


def atualizar_tarefas(array_de_tarefas, indice, tarefa_atualizada):
    indice_correto = indice - 1
    if 0 <= indice_correto < (len(array_de_tarefas)):
        array_de_tarefas[indice_correto]['tarefa'] = tarefa_atualizada
        print(f'Tarefa {indice} atualizado para {tarefa_atualizada}')
    else:
        print('A tarefa que voce esta tentando atualizar nao existe.')
    return


def completar_tarefas(array_de_tarefas, indice_da_tarefa):
    indice_ajustado = indice_da_tarefa - 1
    array_de_tarefas[indice_ajustado]['completada'] = True
    print(f'Tarefa {indice_da_tarefa} marcada como completada')
    return


def deletar_tarefas_completadas(array_de_tarefas):
    for tarefa in array_de_tarefas:
        if tarefa['completada']:
            array_de_tarefas.remove(tarefa)
    print('Tarefas completadas foram deletadas')
    return


while True:
    print('\nMenu do Gerenciador de Lista de Tarefas')
    print('1. Adicionar tarefa')
    print('2. Ver todas as tarefas')
    print('3. Atualizar tarefa')
    print('4. Completar tarefa')
    print('5. Deletar todas as tarefas completadas')
    print('6. Sair')

    escolha = int(input('Digite a sua escolha: '))

    if escolha == 1:
        nome = input('Digite o nome da tarefa que deseja adicionar: ')
        adicionar_tarefa(todas_as_tarefas, nome)
    elif escolha == 2:
        visualizar_tarefas(todas_as_tarefas)
    elif escolha == 3:
        visualizar_tarefas(todas_as_tarefas)
        numero_da_tarefa = int(input('Digite o numero da tarefa que deseja atualizar: '))
        atualizacao = input(f'Atualize a tarefa {numero_da_tarefa}: ')
        atualizar_tarefas(todas_as_tarefas, numero_da_tarefa, atualizacao)
    elif escolha == 4:
        visualizar_tarefas(todas_as_tarefas)
        numero_da_tarefa_completada = int(input('Digite o numero da tarefa que deseja marcar como completada: '))
        completar_tarefas(todas_as_tarefas, numero_da_tarefa_completada)
    elif escolha == 5:
        deletar_tarefas_completadas(todas_as_tarefas)
        visualizar_tarefas(todas_as_tarefas)
    elif escolha == 6:
        break

print('Fim do programa!')
