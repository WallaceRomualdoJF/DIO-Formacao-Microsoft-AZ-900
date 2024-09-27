def calcular_imposto(salario):
    if salario <= 1100:
        return salario * 0.05
    elif salario <= 2500:
        return salario * 0.10
    else:
        return salario * 0.15

def calcular_salario_liquido(salario_bruto, beneficios):
    imposto = calcular_imposto(salario_bruto)
    salario_liquido = salario_bruto - imposto + beneficios
    return salario_liquido

# Leitura dos dados
salario_bruto = float(input())
beneficios = float(input())

# Cálculo e impressão do resultado
resultado = calcular_salario_liquido(salario_bruto, beneficios)
print(f'{resultado:.2f}')