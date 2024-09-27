
# Calculadora de Salário Líquido

Este repositório contém um script em Python que calcula o salário líquido de um funcionário, considerando o imposto sobre o salário bruto e possíveis benefícios. 

## Descrição

O programa recebe como entrada o salário bruto e o valor dos benefícios, e calcula o imposto sobre o salário bruto conforme a tabela abaixo:

- Salários até R$1100,00: 5% de imposto.
- Salários entre R$1101,00 e R$2500,00: 10% de imposto.
- Salários acima de R$2500,00: 15% de imposto.

Após o cálculo do imposto, o programa retorna o salário líquido, que é calculado subtraindo o valor do imposto e somando os benefícios ao salário bruto.

### Fórmula:

```python
salario_liquido = salario_bruto - imposto + beneficios
```

## Estrutura do Código

- **calcular_imposto(salario)**: Função que recebe o salário bruto e retorna o valor do imposto com base nas faixas salariais.
  
- **calcular_salario_liquido(salario_bruto, beneficios)**: Função que recebe o salário bruto e os benefícios e retorna o salário líquido, aplicando o valor do imposto sobre o salário.

- O programa lê dois valores da entrada: o salário bruto e os benefícios, e então exibe o salário líquido formatado com duas casas decimais.

## Como Usar

1. Clone este repositório.
2. Execute o script em um ambiente Python 3.x.
3. Insira o valor do salário bruto e dos benefícios quando solicitado.

### Exemplo de Execução

Entrada:

```
3000.00
250.00
```

Saída:

```
2825.00
```

O salário bruto é de R$3000,00, e o benefício é de R$250,00. O imposto aplicado será de 15%, resultando em um salário líquido de R$2825,00.

## Requisitos

- Python 3.x
```

Esse `README.md` fornece uma explicação clara de como o script funciona, além de instruções de uso para quem clonar o repositório.
