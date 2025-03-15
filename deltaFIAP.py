# Digite os valores de A, B e C e calcule o delta da equação de segundo grau

a = int(input("Digite o valor de A: \n"))
b = int(input("Digite o valor de B: \n"))
c = int(input("Digite o valor de C: \n"))

delta = (b ** 2) - (4*a*c)
print("O delta é: ", delta)

if delta < 0:
    print("A equação não possui raízes reais")
elif delta == 0:
    x = (-b) / (2*a)
    print("A equação possui uma raiz real: ", x)
else:
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b - delta ** 0.5) / (2*a)
    print("A equação possui duas raízes reais: ", x1, " e ", x2)