
# Validador de Dados

Este repositório contém um script em Python que valida os dados inseridos pelo usuário: nome, idade e e-mail. O programa realiza verificações simples para garantir que os dados estão no formato correto.

## Descrição

O programa solicita três entradas do usuário:
- **Nome**: Qualquer valor textual (sem validação de formato).
- **Idade**: Um número inteiro que deve estar entre 0 e 120.
- **E-mail**: Deve conter o caractere "@" e um ponto "." para ser considerado válido.

### Critérios de Validação:

1. A idade deve estar no intervalo entre 0 e 120. Se estiver fora desse intervalo, o programa exibirá a mensagem `"Dados Invalidos: Idade fora do intervalo permitido!"`.
2. O e-mail deve conter os símbolos "@" e ".", caso contrário, será exibida a mensagem `"Dados Invalidos: E-mail no formato incorreto!"`.
3. Se a idade e o e-mail estiverem corretos, o programa retorna a mensagem `"Dados Validados com Sucesso!"`.

## Estrutura do Código

- **validar_dados(nome, idade, email)**: Função que valida os dados inseridos de acordo com as regras descritas acima e retorna uma mensagem indicando se os dados são válidos ou inválidos.
  
- O programa solicita o nome, idade e e-mail do usuário e chama a função `validar_dados` para verificar se os dados estão no formato esperado.

## Como Usar

1. Clone este repositório.
2. Execute o script em um ambiente Python 3.x.
3. Insira os dados solicitados (nome, idade e e-mail).

### Exemplo de Execução

Entrada:

```
João
25
joao@gmail.com
```

Saída:

```
Dados Validados com Sucesso!
```

Entrada inválida (idade fora do intervalo):

```
Maria
130
maria@gmail.com
```

Saída:

```
Dados Invalidos: Idade fora do intervalo permitido!
```

Entrada inválida (e-mail incorreto):

```
Ana
28
anaemail.com
```

Saída:

```
Dados Invalidos: E-mail no formato incorreto!
```
