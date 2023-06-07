import random
import matplotlib.pyplot as plt

from calc import Calculator

# Obter os valores de a, b e c
ru = input("Digite os três primeiros números do seu RU: ")
a = int(ru[0]) if ru[0] != '0' else 5
b = int(ru[1]) if ru[1] != '0' else 5
c = int(ru[2]) if ru[2] != '0' else 5

# Criar vetor aleatório de tamanho 10 para x
x = [random.random() for _ in range(10)]

# Criar instância da classe Calculator que gerencia os cálculos
calc = Calculator(a,b,c,x)

# Calcular os valores de y para cada valor de x
y = calc.linear_eq_calc()

# Criar o gráfico
plt.scatter(x, y, c='red', label='Pontos da Equação Linear')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.show()
