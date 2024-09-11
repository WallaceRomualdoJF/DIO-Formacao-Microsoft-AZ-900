
# Ferramentas de Implantação no Microsoft Azure

## Índice

1. [Azure DevOps](#azure-devops)
2. [Azure CLI](#azure-cli)
3. [GitHub Actions](#github-actions)

## Azure DevOps

Azure DevOps é um conjunto de serviços para gerenciar o ciclo de vida de desenvolvimento de software. Ele oferece pipelines de CI/CD, gerenciamento de projetos e controle de versão.

### Passo a Passo para Implantação com Azure DevOps

1. **Criar uma Conta no Azure DevOps**
   - Acesse [Azure DevOps](https://dev.azure.com/).
   - Clique em "Start free" para criar uma nova conta.

2. **Criar um Projeto**
   - Após o login, clique em "New Project".
   - Preencha o nome do projeto e outras configurações, e clique em "Create".

3. **Configurar Repositório**
   - No painel do projeto, vá para "Repos" para configurar um repositório Git.
   - Adicione seu código ao repositório.

4. **Criar um Pipeline de Build**
   - Vá para "Pipelines" e clique em "New Pipeline".
   - Selecione "Azure Repos Git" e configure o pipeline seguindo as instruções.

5. **Criar um Pipeline de Release**
   - Vá para "Pipelines" > "Releases" e clique em "New pipeline".
   - Defina os artefatos e configure os estágios de deployment.

6. **Executar o Pipeline**
   - Inicie o pipeline de build e release para implantar sua aplicação.

Para mais detalhes, consulte a [documentação do Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/).

## Azure CLI

Azure CLI é uma ferramenta de linha de comando para gerenciar recursos do Azure. Ela permite a criação, configuração e gerenciamento de recursos diretamente do terminal.

### Passo a Passo para Implantação com Azure CLI

1. **Instalar Azure CLI**
   - Siga as instruções para instalar o Azure CLI no [site oficial](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

2. **Autenticar**
   - Abra o terminal e execute:
     ```bash
     az login
     ```
   - Siga as instruções para autenticar sua conta.

3. **Criar um Recurso**
   - Para criar um grupo de recursos, execute:
     ```bash
     az group create --name myResourceGroup --location eastus
     ```

4. **Implantar uma Aplicação**
   - Use comandos específicos para criar e configurar recursos, como máquinas virtuais ou aplicativos web. Por exemplo, para criar um aplicativo web:
     ```bash
     az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myWebApp --runtime "NODE|12-lts"
     ```

5. **Gerenciar Recursos**
   - Use comandos como `az vm start`, `az vm stop`, etc., para gerenciar seus recursos.

Para mais detalhes, consulte a [documentação do Azure CLI](https://docs.microsoft.com/en-us/cli/azure/).

## GitHub Actions

GitHub Actions é uma plataforma de integração e entrega contínua que permite automação do fluxo de trabalho diretamente do GitHub.

### Passo a Passo para Implantação com GitHub Actions

1. **Criar um Repositório no GitHub**
   - Acesse [GitHub](https://github.com/) e crie um novo repositório ou use um existente.

2. **Adicionar um Workflow de GitHub Actions**
   - No repositório, vá para a aba "Actions" e clique em "Set up a workflow yourself".
   - Crie um arquivo YAML no diretório `.github/workflows/`. Exemplo básico de workflow:
     ```yaml
     name: Build and Deploy

     on:
       push:
         branches:
           - main

     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v2
           - name: Set up Node.js
             uses: actions/setup-node@v2
             with:
               node-version: '14'
           - run: npm install
           - run: npm run build

       deploy:
         runs-on: ubuntu-latest
         needs: build
         steps:
           - name: Deploy to Azure
             uses: azure/actions@v1
             with:
               azure-subscription: ${{ secrets.AZURE_SUBSCRIPTION }}
               app-name: 'my-web-app'
               package: 'path-to-package.zip'
     ```

3. **Configurar Segredos**
   - No repositório, vá para "Settings" > "Secrets" e adicione segredos necessários, como `AZURE_SUBSCRIPTION`.

4. **Executar o Workflow**
   - Sempre que você fizer um push para a branch especificada, o GitHub Actions executará o workflow.