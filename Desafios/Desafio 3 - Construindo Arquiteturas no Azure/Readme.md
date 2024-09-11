# Criação da Arquitetura


## 1. Portal do Azure 🌑

Login no [Portal do Azure](https://portal.azure.com).

## 2. Criação do Grupo

1. Acesse o painel, localize por “Grupos de Recursos” ou “Resource Groups” na barra de pesquisa.

2. Clique em **"Criar"** para inicia a criação de um novo grupo de recursos.

   ![s](https://github.com/user-attachments/assets/3d26af1f-5ee7-46f8-8c62-662ead21aa8b)

4. Preencha as seguintes informações:
   - **Nome do Grupo de Recursos**: Dê um nome que identifique facilmente o grupo e seu propósito.
   - **Região**: Selecione a região onde o grupo será criado. É recomendado escolher a mesma região para todos os recursos relacionados para reduzir a latência e os custos.]

5. Clique em **"Revisar + Criar"**.
6. Depois em **"Criar"**.


## 3. Rede Virtual

1. No painel da plataforma, localize pelas “Redes Virtuais” ou “Virtual Networks”.
2. Clique em **"Criar"**.
3. Para iniciar a configuração de uma nova rede virtual desejado na plataforma.


4. Preencha os detalhes:
   - **Nome da Rede Virtual**: Escolha um nome de preferencia para identificação da rede.
   - **Grupo de Recursos**: Selecione o grupo de recursos.
   - **Região**: Escolha a mesma região do grupo.
   - **Endereço IP**: Defina o intervalo de endereços IP.

   
5. Grupo de Recursos:
   - Clique em **"Revisar + Criar"**.
   - Depois em **"Criar"**.

   Atenção: Quando inserir algum detalhe incorreto ou falha pode ser excluído o grupo do serviço.


# Microsoft Azure
## Segurança da Informação

A Microsoft Azure oferece uma série de recursos e práticas para garantir a segurança da informação, protegendo dados, aplicações e infraestrutura. Aqui estão alguns dos principais aspectos:

### 1. Controle de Acesso

- **Autenticação Multifatorial (MFA)**: Adiciona uma camada extra de segurança exigindo múltiplos métodos de verificação para acessar a conta.
- **Gerenciamento de Identidades**: Utiliza o Azure Active Directory para gerenciar e autenticar usuários e grupos, com controle granular de permissões e acessos.
- **Controle de Acesso Baseado em Função (RBAC)**: Permite definir permissões detalhadas para recursos específicos, garantindo que apenas usuários autorizados possam executar ações específicas.

### 2. Proteção de Dados

- **Criptografia**: Dados em trânsito e em repouso são criptografados usando padrões de criptografia avançados. O Azure oferece criptografia automática para dados armazenados e em movimentação.
- **Backup e Recuperação**: Serviços de backup e recuperação garantem que dados possam ser restaurados em caso de perda ou corrupção.

### 3. Segurança de Rede

- **Firewalls e Segurança de Rede**: Firewalls Azure e Grupos de Segurança de Rede (NSGs) protegem recursos de rede contra acessos não autorizados e ataques.
- **Redes Virtuais**: Segmentação de rede para isolar e proteger diferentes partes da infraestrutura.

### 4. Monitoramento e Detecção

- **Monitoramento**: O Azure Monitor e o Azure Security Center fornecem visibilidade em tempo real sobre a saúde e segurança dos recursos.
- **Detecção de Ameaças**: Utiliza ferramentas de detecção para identificar e responder a atividades suspeitas e possíveis ameaças.

### 5. Conformidade e Governança

- **Conformidade**: Alinhamento com regulamentações e padrões de conformidade, incluindo GDPR, HIPAA, e outros.
- **Auditoria e Relatórios**: Ferramentas para auditoria contínua e relatórios sobre segurança e conformidade.

Para mais informações detalhadas, consulte a [documentação oficial da Microsoft Azure sobre segurança](https://docs.microsoft.com/en-us/azure/security/).