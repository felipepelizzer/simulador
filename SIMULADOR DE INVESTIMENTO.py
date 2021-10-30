while True:
    print("----------------------------------------")
    print("  Seja bem-vindo(a) ao TESOURO DIRETO ")
    print("    SIMULADOR DE INVESTIMENTO   ")
    print("----------------------------------------")

    print('titulos disponiveis:')
    print('1 - tesouro prefixado 2024')
    print('2 - tesouro prefixado 2026')
    num = int(input("qual titulo você gostaria de fazer uma simulação? 1/2: "))
    investido = int(input("qual o valor que você quer investir?: "))
    mensal = int(input("se você for investir todo mês, qual seria o valor?: "))


    # Definindo a taxa de renda futura dependendo do investimento
    if num == '1':
    renda = 11,49
    meses = 32

    else:
    renda = 11,67
    meses = 50


    # calculando os valores do investimento
    investir = (mensal * meses) + investido
    total = renda * investir
    rentabilidade = investir / investido - 1
    bruto = investir * (rentabilidade/100)
    valor_bruto = bruto + investir
    ir = (15/100)
    b3 = (0,25/100)
    irtotal = total - valor_bruto *ir
    b3total = valor_bruto / b3
    liquido = valor_bruto - (ir + b3)
 

    print("--------------------------------------------------")
    print("   RESULTADO DA SIMULAÇÃO      ")
    print("--------------------------------------------------")
    print("valor inicial investido: ", investido)
    print("apostes de", mensal , "reais por",meses,"meses")
    print("valor total investido: ", investir, "reais")
    print("--------------------------------------------------")
    print("valor bruto: ",valor_bruto)
    print("I.R: ",irtotal)
    print("taxa da B3: ",b3total)
    print("valor liquido: ",liquido)

    print("-----------------------------------------------------")
    opcao = str(input("Deseja realizar outra simulação? s/n: "))

    # se a opção for igual a "n" o programa é encerrado
    if opcao == 'n':
        break

print("Programa encerrado") 