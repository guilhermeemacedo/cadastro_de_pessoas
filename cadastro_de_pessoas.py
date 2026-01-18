import os


# Lista global de pessoas
pessoas = []  # Cada pessoa será armazenada como um dicionário dentro desta lista


# Função para limpar a tela
def limpar_tela():
    """
    Limpa o terminal dependendo do sistema operacional.
    Windows -> cls
    Linux/macOS -> clear
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux / macOS
        os.system('clear')


# Função para cadastrar pessoas
def cadastrar_pessoa():
    """
    Solicita nome, idade e email do usuário.
    Valida cada entrada:
    - Nome: não vazio, apenas letras.
    - Idade: deve ser número.
    - Email: não vazio e não duplicado.
    Permite cancelar a operação a qualquer momento digitando '0'.
    """
    while True:
        nome = input('Digite um nome (ou 0 para voltar ao menu): ').strip()
        if nome == '0':
            print('Cadastro cancelado. Voltando ao menu...')
            return
        if nome == '' or not nome.isalpha():
            print('Digite um nome válido. Apenas letras são permitidas.')
        else:
            break

    while True:
        idade = input('Digite uma idade (ou 0 para voltar ao menu): ').strip()
        if idade == '0':
            print('Cadastro cancelado. Voltando ao menu...')
            return
        if not idade.isdigit():
            print('Idade inválida. Digite apenas números.')
        else:
            idade = int(idade)
            break

    while True:
        email = input('Digite um email (ou 0 para voltar ao menu): ').strip()
        if email == '0':
            print('Cadastro cancelado. Voltando ao menu...')
            return
        if email == '':
            print('Digite um email válido, não pode ser vazio.')
            continue

        # Verifica se o email já está cadastrado
        for pessoa in pessoas:
            if email.lower() == pessoa['email'].lower():
                print('Esse email já está sendo usado, digite outro.')
                break
        else:
            break

    # Cria o dicionário da pessoa e adiciona na lista
    pessoa = {'nome': nome, 'idade': idade, 'email': email}
    pessoas.append(pessoa)

    print('Pessoa cadastrada com sucesso!')
    input('Pressione Enter para voltar ao menu...')


# Função para listar pessoas
def listar_pessoa():
    """
    Lista todas as pessoas cadastradas.
    Se não houver pessoas, avisa o usuário.
    """
    if not pessoas:
        print('Nenhuma pessoa cadastrada.')
    else:
        for pessoa in pessoas:
            print(f'''------------------
Nome: {pessoa['nome']} 
Idade: {pessoa['idade']} 
Email: {pessoa['email']}
''')
    input('Pressione Enter para voltar ao menu...')


# Função para buscar pessoa
def buscar_pessoa():
    """
    Solicita ao usuário nome ou email.
    Permite voltar ao menu digitando '0'.
    Procura na lista de pessoas e exibe os dados.
    Caso não encontre, avisa o usuário.
    """
    busca = input('Digite o nome completo ou o email da pessoa que deseja buscar (ou 0 para voltar): ').lower()
    if busca == '0':
        print('Voltando ao menu...')
        return

    encontrei = False
    for pessoa in pessoas:
        if busca == pessoa['nome'].lower() or busca == pessoa['email'].lower():
            print(f'''----------------
Nome: {pessoa['nome']} 
Idade: {pessoa['idade']} 
Email: {pessoa['email']}
''')
            encontrei = True
            break

    if not encontrei:
        print('Pessoa não registrada.')
    input('Pressione Enter para voltar ao menu...')


# Função para atualizar pessoa
def atualizar_pessoa():
    """
    Permite atualizar nome, idade ou email de uma pessoa.
    - Primeiro busca a pessoa pelo nome ou email.
    - Permite voltar ao menu digitando '0'.
    - Valida cada atualização para garantir entrada correta.
    """
    busca = input('Digite o nome completo ou o email da pessoa que deseja atualizar os dados (ou 0 para voltar): ').lower()
    if busca == '0':
        print('Voltando ao menu...')
        return

    encontrei = False
    for pessoa in pessoas:
        if busca == pessoa['nome'].lower() or busca == pessoa['email'].lower():
            print(f'''----------------
Nome: {pessoa['nome']} 
Idade: {pessoa['idade']} 
Email: {pessoa['email']}
''')
            encontrei = True

            while True:
                try:
                    oque_atualizar = int(input(
                        '\n1. Nome \n2. Idade \n3. Email \n\nDigite o número da informação que deseja alterar (ou 0 para voltar): '))
                except ValueError:
                    print('Digite um número válido.')
                    continue

                if oque_atualizar == 0:
                    print('Atualização cancelada. Voltando ao menu...')
                    return

                if oque_atualizar == 1:
                    while True:
                        atualizar_nome = input('Digite um novo nome (ou 0 para voltar): ').strip()
                        if atualizar_nome == '0':
                            print('Atualização de nome cancelada.')
                            break
                        if atualizar_nome == '' or not atualizar_nome.isalpha():
                            print('Nome inválido. Digite apenas letras e não deixe vazio.')
                        else:
                            pessoa['nome'] = atualizar_nome
                            print('Nome atualizado com sucesso!')
                            break
                    break

                elif oque_atualizar == 2:
                    while True:
                        atualizar_idade = input('Digite uma nova idade (ou 0 para voltar): ').strip()
                        if atualizar_idade == '0':
                            print('Atualização de idade cancelada.')
                            break
                        if not atualizar_idade.isdigit():
                            print('Idade inválida. Digite apenas números.')
                        else:
                            pessoa['idade'] = int(atualizar_idade)
                            print('Idade atualizada com sucesso!')
                            break
                    break

                elif oque_atualizar == 3:
                    while True:
                        atualizar_email = input('Digite um novo email (ou 0 para voltar): ').strip()
                        if atualizar_email == '0':
                            print('Atualização de email cancelada.')
                            break
                        if atualizar_email == '':
                            print('Email inválido. Não pode ser vazio.')
                            continue
                        for p in pessoas:
                            if atualizar_email.lower() == p['email'].lower():
                                print('Esse email já está sendo usado, digite outro.')
                                break
                        else:
                            pessoa['email'] = atualizar_email
                            print('Email atualizado com sucesso!')
                            break
                    break

                else:
                    limpar_tela()
                    print('Opção digitada inválida, digite uma opção válida.')
            break

    if not encontrei:
        print('Pessoa não registrada.')
    input('Pressione Enter para voltar ao menu...')


# Função para deletar pessoa
def deletar_pessoa():
    """
    Permite remover uma pessoa cadastrada.
    - Busca pelo nome ou email.
    - Confirmação antes de remover.
    - Permite voltar ao menu digitando '0'.
    """
    busca = input('Digite o nome completo ou o email da pessoa que deseja deletar (ou 0 para voltar): ').lower()
    if busca == '0':
        print('Operação de remoção cancelada. Voltando ao menu...')
        return

    encontrei = False
    for pessoa in pessoas:
        if busca == pessoa['nome'].lower() or busca == pessoa['email'].lower():
            print(f'''----------------
Nome: {pessoa['nome']} 
Idade: {pessoa['idade']} 
Email: {pessoa['email']}
''')
            encontrei = True

            while True:
                try:
                    opcao_deletar = int(input('Deseja deletar essa pessoa?\n1. SIM\n2. NÃO\nDigite uma opção (ou 0 para voltar): '))
                except ValueError:
                    limpar_tela()
                    print('Digite uma opção válida.')
                    continue

                if opcao_deletar == 0:
                    print('Remoção cancelada. Voltando ao menu...')
                    return
                elif opcao_deletar == 1:
                    pessoas.remove(pessoa)
                    print(f'Pessoa {pessoa["nome"]} removida com sucesso!')
                    break
                elif opcao_deletar == 2:
                    print('Ação cancelada.')
                    break
                else:
                    limpar_tela()
                    print('Opção inválida, digite uma opção válida.')
            break

    if not encontrei:
        print('Pessoa não registrada.')
    input('Pressione Enter para voltar ao menu...')


# Função principal (menu)
def main():
    """
    Menu principal do sistema.
    Exibe as opções e chama as funções correspondentes.
    O loop continua até que o usuário escolha sair (opção 0).
    """
    while True:
        limpar_tela()
        print('𝘾𝙖𝙙𝙖𝙨𝙩𝙧𝙤 𝙙𝙚 𝙋𝙚𝙨𝙨𝙤𝙖𝙨')
        print('''
1 - Cadastrar pessoa
2 - Listar pessoas
3 - Buscar pessoa
4 - Atualizar pessoa
5 - Remover pessoa
0 - Sair
        ''')

        try:
            escolha = int(input('Digite a opção desejada: '))
        except ValueError:
            print('Opção inválida, digite apenas números.')
            input('Pressione Enter para voltar ao menu...')
            continue

        if escolha == 1:
            limpar_tela()
            print('Cadastrando uma pessoa')
            cadastrar_pessoa()
        elif escolha == 2:
            limpar_tela()
            print('Lista de pessoas')
            listar_pessoa()
        elif escolha == 3:
            limpar_tela()
            print('Buscando pessoa')
            buscar_pessoa()
        elif escolha == 4:
            limpar_tela()
            print('Atualizando dados da pessoa')
            atualizar_pessoa()
        elif escolha == 5:
            limpar_tela()
            print('Deletando dados da pessoa')
            deletar_pessoa()
        elif escolha == 0:
            print('Sistema finalizado.')
            break
        else:
            print('Opção inválida, digite uma opção válida.')
            input('Pressione Enter para voltar ao menu...')


# Executa o programa
if __name__ == "__main__":
    main()
