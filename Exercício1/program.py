from calc import Calculator

# Solicitar ao usuário os dois números
nums = input("Digite os dois últimos dígitos do seu RU:")

num1 = int(nums[0])
num2 = int(nums[1])

# Criar instância da classe Calculator que gerencia os cálculos
calc = Calculator(num1, num2)

# Verificar se algum dos números do RU é zero
calc.verify_nums()

# Exibir menu de escolha de operações
print("Calculadora - Escolha a operação:")
print("1. Soma (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
print("5. Expoente (^)")
print("6. Resto (%)")
print("7. Raiz quadrada da soma (sqrt(Num1 + Num2))")

# Solicitar ao usuário a escolha da operação
opr = input("Digite o número da operação desejada: ")

# Realizar a operação escolhida e exibir o resultado
if opr == "1":
    print(f"Resultado: {calc.sum()}")
elif opr == "2":
    print(f"Resultado: {calc.sub()}")
elif opr == "3":
    print(f"Resultado: {calc.mul()}")
elif opr == "4":
    print(f"Resultado: {calc.div()}")
elif opr == "5":
    print(f"Resultado: {calc.exp()}")
elif opr == "6":
    print(f"Resultado: {calc.rem()}")
elif opr == "7":
    print(f"Resultado: {calc.sqrt_sum()}")
else:
    print("Opção inválida. Por favor, escolha uma opção válida de 1 a 7.")
