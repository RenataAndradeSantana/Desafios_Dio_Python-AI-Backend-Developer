def depositar(saldo, extrato): # Recebe argumento poscional
        
    while True:
        valor = input('Informe o valor do depósito:')
        valor_valido = True
        for i in valor:
            if i not in '.0123456789': 
                
                valor_valido = False 
            print("VALOR INFORMADO É INVÁLIDO.")
            break
        if valor_valido:
            break  
    valor = float(valor)                

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("VALOR DESOPITADO COM SUCESSO!!!!")
      
    else:
        print("VALOR INFORMADO É INVÁLIDO.")
        
    
        
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # Recebe argumento nomeado
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nSALDO INSUFICIENTE.")

    elif excedeu_limite:
        print("\nSAQUE EXCEDE LIMITE.")

    elif excedeu_saques:
        print("\nNÚMERO MÁXIMO DE SAQUE EXCEDUDO.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("VALOR INFORMADOO É INVÁLIDO!")

    return saldo, extrato


def extrato_bancario(saldo, /, *, extrato): # Recebe argumento posicional e nomeado
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(cpf):
     
    
    
    if cpf in dados_usuarios:
        print("Usuário cadastrado!!!")
        for cpf1 in dados_usuarios:
            if cpf1 == cpf:
              print("Dados do usuário:", dados_usuarios[cpf])
        
    else:    
        nome = input('Digite o nome completo do usuário:')
        data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
       
        numero_conta = len(contas) + 1
        contas.append(numero_conta)
         
        dados_usuarios[cpf] = {'nome:': nome, 'data_nasc:': data_nasc, 'endereco:': endereco,'agencia': AGENCIA, 'conta:': numero_conta}
        print("Usuário criado com sucesso!!!")
        print({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": nome})
    
        
        
        
def criar_conta(cpf):
    
    usuario = criar_usuario(cpf)

    return usuario

    
    
    
def listar_contas(dados_usuarios):
    for conta in dados_usuarios.values():
        print(conta)
           
      
####   Programa principal ####
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Criar Usuário
[lc] Listar contas
[cc] criar conta

"""
import textwrap
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
dados_usuarios = {} 
contas = []
AGENCIA = "0001"

while True:
    
    print(menu)
    opcao = input("Digite a opção desejada: ")
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        [c] Criar Usuário
        [lc] Listar contas
        [cc] criar conta
      
      
    """
    if opcao == "d":
        #valor = input('Informe o valor do depósito:')      
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, 
                              limite_saques=LIMITE_SAQUES)   
    
    elif opcao == "e":
        extrato_bancario(saldo, extrato=extrato)
        
    elif opcao == "q":
        print('OBRIGADA PELA PREFERÊNCIA!')
        break
    
    elif opcao == 'c':
        cpf = int(input('Digite o CPF, (somente número)'))
        criar_usuario(cpf)
        
        
    elif opcao == "cc":
            numero_conta = len(contas) + 1
            cpf = int(input('Digite o CPF, (somente número)'))
            conta = criar_conta(cpf)
        
            
    elif opcao == "lc":
            listar_contas(dados_usuarios)

    else:
        print('COMANDO ERRADO!\nFavor digite:\n[d] para Despositar,\n[s] para Sacar,\n[e] para Extrato, \n[q] caso deseja sair do sistema, \n[c] Criar Usuário, \n[lc] Listar contas e \n[cc] criar conta ')
        menu = ''
        


                