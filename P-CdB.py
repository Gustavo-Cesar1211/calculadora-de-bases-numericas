import os
os.system('cls')

print(' CONVERTER BASES NUMÉRICAS')
print(' Escolha uma das opções do menu abaixo: ')
print('\n [1] - Decimal -> BINÁRIO \n [2] - Decimal -> OCTAL \n [3] - Decimal -> HEXADECIMAL \n [4] - Informações do projeto \n [5] - Sair')
while True:
    opcao = input("Digite a sua opção desejada: ")
    if opcao in ("1", "2", "3"):
        decimal = int(input("Digite o número DECIMAL para conversão: "))
        deci_salvo = decimal
        resultado = ""  
        if opcao == "1":
            while decimal > 0:
                resultado = str(decimal % 2) + resultado
                decimal = decimal // 2
        elif opcao == "2":
            while decimal > 0:
                resultado = str(decimal % 8) + resultado
                decimal = decimal // 8
        elif opcao == "3":
            hexa_valores = "0123456789ABCDEF"
            while decimal > 0:
                resultado = hexa_valores[decimal % 16] + resultado
                decimal = decimal // 16
        print(f"O decimal {deci_salvo} convertido é: {resultado}")
    elif opcao == "4":
        print("\n PROJETO - DADOS: ")
        print("   [Curso] - Técnologo em Análise e Desenvolvimento de Sistemas")

        print("\n INTEGRANTES: " )
        print("   [1º] - Danielle Oliveira Santos - [RGM: 38679825]")
        print("   [2º] - Gustavo Cesar Ferreira Silva - [RGM: 38794055]")
        print("   [3º] - Marcos Vinicius Soares Oliveira - [RGM: 38575990]")
        print("   [4º] - Matheus Cecilio Barros - [RGM: 38641224]")

        print("\n PROFESSORES E DISCIPLINAS: ")
        print("   [Marco Antônio] - Programação de Computadores \n   [Edidio Rubens] - Organização e Arquitetura de Computadores")

        print('Versão do aplicativo: 1.0')
    elif opcao == "5":
        print("Saiu da Calculadora.")
        break
    else:
        print("Tente novamente. Opção inválida! ")
