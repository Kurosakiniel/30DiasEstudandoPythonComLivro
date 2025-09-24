"""

Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou
não pagar imposto. Considere que pagam imposto pessoas cujo salário é
maior que R$ 1.200,00.


"""

print(f"Digite seu salário:")
salarioPessoa = float(input())

pagaImposto = salarioPessoa > 1200
print(f"{pagaImposto}")