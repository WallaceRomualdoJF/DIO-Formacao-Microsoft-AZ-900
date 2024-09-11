# Configurando Armazenamento

### 1. Acesse o Portal do Azure

1. Entre no [Portal do Azure](https://portal.azure.com).
2. No painel, procure por “Conta de Armazenamento”.
3. Clique em **"Criar"**.

### 2. Configure a Conta de Armazenamento

1. **Nome da Conta**: Escolha um nome único para sua conta de armazenamento.

2. **Região**: Selecione a região mais próxima para melhor performance.

3. **Tipo de Conta**: Escolha "Armazenamento General Purpose v2".
  
4. **Replicação**: Selecione o tipo de replicação desejado.
   
  ![image](/Desafios/Desafio%205%20-%20Dominando%20o%20Armazenamento%20na%20Azure/Imagens/image1.png)
  
  ![image](/Desafios/Desafio%205%20-%20Dominando%20o%20Armazenamento%20na%20Azure/Imagens/image2.png)

5. **Proteção de Dados**: Importante habilitar exclusão temporária para blobs.
  ![image](/Desafios/Desafio%205%20-%20Dominando%20o%20Armazenamento%20na%20Azure/Imagens/image3.png)

6. **Finalização**
  ![image](/Desafios/Desafio%205%20-%20Dominando%20o%20Armazenamento%20na%20Azure/Imagens/image4.png)


### 3. Criar um Compartilhamento de Arquivos

1. **Acesse Sua Conta de Armazenamento**: Acesse o portal, "Recursos" e selecione sua conta de armazenamento.
   
3. **Criar um Compartilhamento de Arquivos**: 
   - No menu de "Serviços", clique em "Compartilhamento de Arquivos".
   - Clique em "Adicionar compartilhamento de arquivos".
   - Nomeie o compartilhamento e defina o tamanho.
   - Clique em "Criar".
   
![image](/Desafios/Desafio%205%20-%20Dominando%20o%20Armazenamento%20na%20Azure/Imagens/image5.png)

### 4. Migrar Dados para o Azure

1. **Criar um projeto**: 
   - Antes de tudo deve criar um projeto de migração para Azure:

3. **Instalar o AzCopy**: 
   - Baixe e instale o AzCopy do site oficial: [AzCopy Download](https://docs.microsoft.com/azure/storage/common/storage-use-azcopy-v10).

4. **Autenticar com o Azure**:
   
   - ```bash
   - azcopy login
   - azcopy copy 'caminho/local/do/arquivo' 'https://<sua-conta>.file.core.windows.net/<compartilhamento>/<pasta>?<SAS-token>' --recursive