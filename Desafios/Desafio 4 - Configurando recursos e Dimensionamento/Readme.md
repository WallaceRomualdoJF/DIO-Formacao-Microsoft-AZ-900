# Criar e Configurar uma Máquina Virtual no Azure

Este documento fornece um guia passo a passo para criar e configurar uma Máquina Virtual (VM) no Azure.

## Passo a Passo para Criar Sua VM

### 1. Acesse o Portal do Azure

1. Acesse o [Portal do Azure](https://portal.azure.com).
2. Na página inicial, localize e clique em **"Máquinas Virtuais"**.
3. Clique em **"Criar"** para iniciar o processo de criação de uma nova VM.

### 2. Configure a Máquina Virtual

1. **Nome da VM**: Escolha um nome fácil de lembrar e que identifique a finalidade da VM.
   
   ![image](/Desafios/Desafio%204%20-%20Configurando%20recursos%20e%20Dimensionamento/Imagens/image1.png)

2. **Região**: Selecione a região mais próxima dos seus usuários para garantir a melhor performance e menor latência.
   
   ![image](/Desafios/Desafio%204%20-%20Configurando%20recursos%20e%20Dimensionamento/Imagens/image2.png)

3. **Imagem**: Escolha o sistema operacional desejado (Windows ou Linux).
   
   ![Image](/Desafios/Desafio%204%20-%20Configurando%20recursos%20e%20Dimensionamento/Imagens/image3.png)

4. **Tamanho**: Selecione o tamanho da VM com base nas suas necessidades de CPU e memória.
   
   ![image](/Desafios/Desafio%204%20-%20Configurando%20recursos%20e%20Dimensionamento/Imagens/image4.png)

   **Importante!** 
   - Marque a opção "Excluir com VM" se desejar que o disco da VM seja excluído automaticamente quando a VM for excluída.

### 3. Configure o Dimensionamento da VM

1. **Dimensionamento Manual**: Escolha um tamanho de VM baseado na carga de trabalho que você espera.

    ![image](/Desafios/Desafio%204%20-%20Configurando%20recursos%20e%20Dimensionamento/Imagens/image5.png)

2. **Dimensionamento Automático**: Configure a autoescala para ajustar automaticamente os recursos da VM com base na demanda.
3. **Utilize o Azure Advisor**: O Azure Advisor fornece recomendações de dimensionamento com base no desempenho atual da sua VM.

### 4. Configure a Rede

1. **Rede Virtual**: Crie uma nova rede virtual ou escolha uma existente.
2. **Sub-rede**: Escolha a sub-rede específica na qual a sua VM será colocada.
3. **Grupo de Segurança de Rede (NSG)**: Defina regras para controlar o tráfego de entrada e saída da VM.

### 5. Defina Credenciais

1. **Nome de Usuário e Senha**: Configure um usuário e senha fortes para acessar sua VM.
2. **Chaves SSH (para Linux)**: Se estiver configurando uma VM com Linux, use chaves SSH para se conectar com mais segurança.

### 6. Configurações Adicionais

1. **Monitoramento**: Habilite o monitoramento para acompanhar o desempenho da sua VM.
2. **Tags**: Adicione tags para organizar melhor seus recursos.

### 7. Revise e Crie

1. Revise todas as configurações para garantir que estão corretas.
2. Clique em **"Criar"** e aguarde enquanto o Azure prepara sua VM.

### 8. Conecte-se à Sua VM

1. **Para Windows**: Utilize o Remote Desktop Protocol (RDP) para se conectar à VM.
2. **Para Linux**: Utilize SSH para acessar a VM.

## Recursos Adicionais

- [Documentação do Azure sobre Máquinas Virtuais](https://docs.microsoft.com/azure/virtual-machines/)
- [Tutorial de Configuração de VM](https://docs.microsoft.com/azure/virtual-machines/tutorial-create-vm)