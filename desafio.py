menu = """

[1] Criar Usuário
[2] Criar Conta Corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
usuarios = {} 
numero_conta = 0

def depositar(saldo_bancario, /, *, extrato_bancario):

        valor_total = float(input("Informe o valor do depósito: "))

        if valor_total > 0:
            saldo_bancario += valor_total
            extrato_bancario += f"Depósito: R$ {valor_total:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return saldo_bancario, extrato_bancario

def sacar(*, saldo_bancario, extrato_bancario, numero_saques):
        
        limite = 500
        LIMITE_SAQUES = 3
        
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo_bancario:
            print("Operação falhou! Você não tem saldo suficiente.")
            print(saldo, saldo_bancario)

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo_bancario -= valor
            extrato_bancario += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return saldo_bancario, extrato_bancario, numero_saques

def extrato_bancario(saldo, extrato):

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def tratamento_cpf(cpf:str):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    return cpf 

def criar_usuario():
    global usuarios

    nome = str(input('Nome: ')).strip()
    data_nascimento = str(input('Data de nascimento: ')).strip()
    cpf = str(input('CPF: ')).strip()
    logradouro = str(input('Logradouro: ')).strip()
    bairro = str(input('Bairro: ')).strip()
    cidade = str(input('Cidade: ')).strip()
    sigla_UF = str(input('Sigla do estado: ')).strip()
    endereço = logradouro + ' - ' + bairro + ' - ' + cidade + '/' + sigla_UF
    cpf = tratamento_cpf(cpf)
    if usuarios.get(cpf) == None:
        usuarios.setdefault(cpf, [nome, data_nascimento, endereço, []])
        print('Usuário cadastrado!')
    else:
         print('Usuário já existe.')
    
    print(usuarios)
    return usuarios
    

def criar_conta_corrente(cpf):
    global usuarios
    global numero_conta
    AGENCIA = '0001'
    numero_conta += 1
    if usuarios.get(cpf) != None:
        usuarios[cpf][3].append([numero_conta, AGENCIA])

    else:
         print('Usuário inexistente! Realize o cadastro do usuário.')
    print(usuarios)
    return usuarios

while True:

    opcao = input(menu).strip()

    if opcao == '1':
        criar_usuario()

    elif opcao == "2":
        cpf = str(input('Digite o cpf: '))
        criar_conta_corrente(cpf)

    elif opcao == "3":
        saldo, extrato = depositar(saldo, extrato_bancario=extrato)
            
    elif opcao == "4":
        saldo, extrato, numero_saques = sacar(saldo_bancario=saldo, numero_saques=numero_saques, extrato_bancario=extrato)
    
    elif opcao == "5":
        extrato_bancario(saldo, extrato)

    elif opcao == "6":
        break

    else:
        print("Operação inválida! por favor selecione novamente a operação desejada.")
