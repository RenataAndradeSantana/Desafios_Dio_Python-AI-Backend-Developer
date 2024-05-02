menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    print(menu)
    opcao = input("Digite a opção desejada: ")
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    """
    if opcao == "d":
        # valor = float(input("Informe o valor do depósito: "))
        # valor = input('Informe o valor do depósito:')
        
        
        while True:
            valor = input('Informe o valor do depósito:')
            valor_valido = True
            for i in valor:
                if i not in '.0123456789': 
                    print("VALOR INFORMADO É INVÁLIDO.")
                    valor_valido = False
            if valor_valido:
                break
        
        valor = float(valor)                

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("VALOR INFORMADO É INVÁLIDO.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

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
    
    elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "q":
        print('OBRIGADA PELA PREFERÊNCIA!')
        break

    else:
        print("COMANDO ERRADO!\nFavor digite:\n[d] para Despositar,\n[s] para Sacar,\n[e] para Extrato e\n[q] caso deseja sair do sistema ")
        menu = ''
        


                