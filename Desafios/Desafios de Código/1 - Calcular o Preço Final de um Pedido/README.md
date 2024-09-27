
# Desafio de Validação de Dados para QA

Este desafio de código é destinado a profissionais de QA, com o objetivo de explorar a universalidade dos conceitos de qualidade de software através de diferentes linguagens de programação. A familiaridade com linguagens específicas é valiosa, mas o foco deste desafio é aplicar práticas que garantam a robustez e confiabilidade do código.

## Objetivo

Validar informações de entrada de acordo com regras de negócio, assegurando que o código atenda a requisitos de qualidade, como tratamento de erro e validação adequada.

### Regras de Negócio

1. **Dados Válidos**: Se todas as informações estiverem corretas:
   - Saída: `Dados Validados com Sucesso!`
   
2. **E-mail Inválido**: Se o e-mail não possuir os caracteres `@` e `.`:
   - Saída: `Dados Invalidos: E-mail no formato incorreto!`
   
3. **Idade Inválida**: Se a idade não estiver entre 0 e 120 anos:
   - Saída: `Dados Invalidos: Idade fora do intervalo permitido!`

## Entrada

A entrada consiste em três linhas de texto:

- **Nome** (string)
- **Idade** (inteiro)
- **E-mail** (string)

## Saída

O programa deve validar as informações de entrada de acordo com as regras de negócio especificadas e retornar uma das mensagens apropriadas.

## Exemplo de Entrada

```
João Silva
25
joao.silva@email.com
```

## Exemplo de Saída

```
Dados Validados com Sucesso!
```

## Instruções para Execução

### Pré-requisitos

- Certifique-se de ter [Python 3](https://www.python.org/) instalado no seu sistema.

### Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd seu-repositorio
```

3. Execute o script de validação:

```bash
python validar_dados.py
```

4. Insira as informações de entrada conforme solicitado pelo programa.

## Estrutura do Código

O código foi projetado com foco na validação de dados e segue princípios fundamentais de qualidade de software:

- **Função de Validação de E-mail**: Verifica a presença dos caracteres `@` e `.`.
- **Função de Validação de Idade**: Verifica se a idade está dentro do intervalo permitido de 0 a 120 anos.
- **Função Principal**: Responsável por coordenar a execução e retornar o resultado da validação.

## Dicas Importantes

- **Conceitos Universais de Qualidade**: A qualidade do software transcende as barreiras da linguagem de programação. Concentre-se em aprender os conceitos fundamentais que são aplicáveis em qualquer linguagem.
  
- **Validação de Dados**: Esta é uma parte essencial do trabalho de QA, e este desafio simula essa responsabilidade de forma prática e educativa.

- **Comparação de Linguagens**: Observe como diferentes linguagens alcançam um objetivo comum em termos de qualidade do código. Cada linguagem tem suas peculiaridades, mas os princípios subjacentes de boa programação permanecem os mesmos.
