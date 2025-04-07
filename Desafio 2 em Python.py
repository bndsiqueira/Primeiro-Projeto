import re

def triangulo():
    try:
        a = int(input("Digite o primeiro lado: "))
        b = int(input("Digite o segundo lado: "))
        c = int(input("Digite o terceiro lado: "))
        
        if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
            if a == b == c:
                print("Triângulo equilátero.")
            elif a == b or a == c or b == c:
                print("Triângulo isósceles.")
            else:
                print("Triângulo escaleno.")
        else:
            print("Os valores informados não formam um triângulo.")
    except ValueError:
        print("Entrada inválida. Digite números inteiros.")

def segundograu():
    try:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        
        if a == 0:
            print("Não é uma equação de segundo grau.")
            return
        
        delta = (b ** 2) - (4 * a * c)
        
        if delta < 0:
            print("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -b / (2 * a)
            print("A equação possui uma única raiz real: %.2f" % raiz)
        else:
            primeiraraiz = (-b + delta ** 0.5) / (2 * a)
            segundaraiz = (-b - delta ** 0.5) / (2 * a)
            print("As raízes da equação são %.2f e %.2f" % (primeiraraiz, segundaraiz))
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")

def data():
    try:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            valido = 1 <= dia <= 31
        elif mes in [4, 6, 9, 11]:
            valido = 1 <= dia <= 30
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                valido = 1 <= dia <= 29
            else:
                valido = 1 <= dia <= 28
        else:
            valido = False
        
        print("Data válida." if valido else "Data inválida.")
    except ValueError:
        print("Entrada inválida. Digite números inteiros.")

def texto():
    texto = input("Digite um texto: ")
    tamanho = len(texto)
    
    if tamanho < 5:
        print("Texto muito pequeno.")
    elif 5 <= tamanho < 15:
        print("Texto de tamanho médio.")
    elif 15 <= tamanho <= 20:
        print("Texto grande.")
    else:
        print("Texto inválido.")

def cpf():
    cpf = input("Digite seu CPF (apenas números): ")
    
    if not (cpf.isdigit() and len(cpf) == 11):
        print("CPF inválido.")
        return
    
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    peso1 = list(range(10, 1, -1))
    peso2 = list(range(11, 2, -1))
    
    digito1 = calcular_digito(cpf[:9], peso1)
    digito2 = calcular_digito(cpf[:9] + str(digito1), peso2)
    
    if cpf[-2:] == f"{digito1}{digito2}":
        print("CPF válido.")
    else:
        print("CPF inválido.")

def caracteres():
    texto = input("Digite um texto: ")
    vogais = len(re.findall(r'[aeiouAEIOU]', texto))
    espacos = texto.count(" ")
    outros = len(texto) - vogais - espacos
    
    print(f"Vogais: {vogais}, Espaços: {espacos}, Outros caracteres: {outros}")

def fatorial():
    try:
        n = int(input("Digite um número inteiro não negativo: "))
        if n < 0:
            print("Número inválido. O fatorial não é definido para números negativos.")
            return
        
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        
        print(f"O fatorial de {n} é {resultado}.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def palindromo():
    texto = input("Digite um texto: ").replace(" ", "").lower()
    if texto == texto[::-1]:
        print("O texto é um palíndromo.")
    else:
        print("O texto não é um palíndromo.")

def converter_temperatura():
    try:
        print("Escolha a conversão desejada:")
        print("1) Celsius para Fahrenheit")
        print("2) Celsius para Kelvin")
        print("3) Fahrenheit para Celsius")
        print("4) Kelvin para Celsius")
        
        opcao = int(input("Opção: "))
        temperatura = float(input("Digite a temperatura: "))
        
        if opcao == 1:
            resultado = (temperatura * 9/5) + 32
            print(f"{temperatura}°C é igual a {resultado:.2f}°F.")
        elif opcao == 2:
            resultado = temperatura + 273.15
            print(f"{temperatura}°C é igual a {resultado:.2f}K.")
        elif opcao == 3:
            resultado = (temperatura - 32) * 5/9
            print(f"{temperatura}°F é igual a {resultado:.2f}°C.")
        elif opcao == 4:
            resultado = temperatura - 273.15
            print(f"{temperatura}K é igual a {resultado:.2f}°C.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")

def menu():
    while True:  
        print("\nOlá! Digite a opção desejada:")
        print("1) Verificar triângulo")
        print("2) Calcular equação de segundo grau")
        print("3) Conferir data")
        print("4) Verificar tamanho do texto")
        print("5) Analisar CPF")
        print("6) Contar caracteres")
        print("7) Calcular fatorial")
        print("8) Verificar palíndromo")
        print("9) Converter temperaturas")
        print("10) Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            triangulo()
        elif opcao == "2":
            segundograu()
        elif opcao == "3":
            data()
        elif opcao == "4":
            texto()
        elif opcao == "5":
            cpf()
        elif opcao == "6":
            caracteres()
        elif opcao == "7":
            fatorial()
        elif opcao == "8":
            palindromo()
        elif opcao == "9":
            converter_temperatura()
        elif opcao == "10":
            print("Obrigado por utilizar nosso sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()