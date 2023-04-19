from time import sleep
valor_atual = 0
LIMITE_SAQUE = 3
total_depositos = 0

nome = input('\033[34mQuerido cliente, por favor... nos lembre seu nome ->\033[m ')
print(f'Claro, {nome}, Vamos começar')
while True:
    print('=-'*10)
    print('\033[34mBANCO D&G\033[m')
    print('=-'*10)
    print('''\033[35mOperações
    [ 1 ] Depósito
    [ 2 ] Saque
    [ 3 ] Extrato 
    [ 4 ] Sair
    \033[m''')

    try:
        escolha = int(input('Opção -> '))
    except ValueError:
        print('\033[0;31mOpção invalida, por favor, Escolha da maneira correta.\033[m')
        continue

    if escolha == 4:
        break

    elif escolha == 1:
        try:
            Deposito = float(input('Valor a ser depósitado: R$ '))
        except ValueError:
            print('\033[31m OPS... Você deve ter feito algo de errado!\033[m ')
            continue

        valor_atual += Deposito
        total_depositos += 1
        print(f'{nome}, seu saldo atual é de \033[32m{valor_atual:.2f}\033[m')
        sleep(2)
        print('\033[36mCARREGANDO...\033[m')
        sleep(2)

    elif escolha == 3:
        print(f'{nome}, suas informações serão carregadas, aguarde...')
        sleep(2)
        print('\033[36mCARREGANDO...\033[m')
        sleep(2)
        print(f'Seu valor bancario Atual é de \033[32mR${valor_atual:.2f}\033[m')
        print(f'Você fez \033[36m{total_depositos}\033[m depósitos hoje')

        if LIMITE_SAQUE == 0:
            print('Você ja usou todo o seu \033[31mlimite de Saque diario.\033[m')
        else:
            print(f'Saques livres até o momento \033[32m{LIMITE_SAQUE}\033[m')
        sleep(2)
        print('\033[36mCARREGANDO...\033[m')
        sleep(2)
    
    elif escolha == 2:
        try:
            sacando = float(input('Valor do Saque: R$ '))
        except ValueError:
            print('\033[31m OPS... Você deve ter feito algo de errado!\033[m ')
            continue

        if valor_atual == 0:
            print('Você não pode sacar, pois seu saldo está zerado. \033[31mNão aceitamos valores negativos\033[m')

        elif LIMITE_SAQUE == 0:
            print('Você Não pode mais sacar, seu Limite diário de saque \033[31mja foi esgotado hoje\033[m!')
        
        elif sacando > valor_atual:
            print('Você está tentando sacar um valor acima do seu saldo atual. \033[31mNão é permitido\033[m')
        elif valor_atual > 0:
            valor_atual -= sacando
            LIMITE_SAQUE -= 1
            print(f'Você sacou \033[31mR$ {sacando:.2f}\033[m, logo seu saldo é de \033[32mR$ {valor_atual:.2f}\033[m')

            sleep(2)
            print('\033[36mCARREGANDO...\033[m')
            sleep(2)
            
print('\033[36mCARREGANDO...\033[m')
sleep(2)            
print('\033[32mVolte sempre querido cliente.\033[m')

