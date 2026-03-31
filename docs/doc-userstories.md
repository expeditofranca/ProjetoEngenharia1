# 📝 Backlog do Produto

# Tabela contendo o planejamento inicial das funcionalidades:

| ID | Título do User Story | Requisitos Funcionais Relacionados | Responsável pelo Detalhamento |
|:---|:---|:---|:---|
| US01 | Manter Cliente | RF01.01, RF01.02, RF01.03, RF01.04 | Expedito |
| US02 | Manter Dívida | RF02.01, RF02.02, RF02.03, RF02.04 | Arthur |

## 📦 RF01 - Manter Cliente
|||
|-|-|
|**Descrição:**|  O sistema deve permitir cadastrar, editar, visualizar e excluir clientes. Será possível cadastrar clientes informando os seguintes dados: nome, CPF, telefone, endereço, profissão e renda familiar. Esse módulo é essencial para o controle de quem pode comprar fiado.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Essencial          |
| Estimativa          | 4h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Arthur             |
| Desenvolvedor       | Expedito           |
| Revisor             | Júlia              |
| Testador            | Gean               |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA01.01    |  O usuário informa, na tela Cadastrar Cliente, todos os dados para o cadastro corretamente, ao clicar em salvar ele é notificado com uma mensagem de sucesso. Mensagem: Cadastro realizado com sucesso.|
| TA01.02    |  O usuário informa, na tela Cadastrar Cliente, os dados para o cadastro incorretamente, ao clicar em salvar ele é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente.|
| TA01.03    |  O usuário informa, na tela Editar Cliente, os dados para identificar o cliente desejado, o cliente existe, o usuário seleciona o cliente, em seguida são mostrados os campos para edição.|
| TA01.04    | O usuário informa, na tela Editar Cliente, os dados para identificar o cliente desejado, o cliente não existe. O usuário é notificado com uma mensagem de erro. Mensagem: Cliente não encontrado|
| TA01.05    | O usuário informa, na tela Editar Cliente corretamente os dados para edição. Ao clicar em salvar ele é notificado com uma mensagem de sucesso. Mensagem: Edição realizada com sucesso.|
| TA01.06    | O usuário informa, na tela Editar Cliente incorretamente os dados para edição. Ao clicar em salvar ele é notificado com uma mensagem de erro. Mensagem: Edição não realizada, o campo “xxxx” não foi informado corretamente.|
| TA01.07    |  O usuário informa, na tela Pesquisar Cliente, os dados para identificar o cliente desejado, o cliente existe, o usuário seleciona o cliente, em seguida são mostradas as informações sobre o cliente.|
| TA01.08    | O usuário informa, na tela Pesquisar Cliente, os dados para identificar o cliente desejado, o cliente não existe. O usuário é notificado com uma mensagem de erro. Mensagem: Cliente não encontrado.|
| TA01.09    |  O usuário informa, na tela Excluir Cliente, os dados para identificar o cliente desejado, o cliente existe, o usuário seleciona o cliente. O usuário é notificado com uma mensagem de aviso. Mensagem: Deseja prosseguir com a ação?. Ao clicar em 'sim' o usuário é notificado com uma mensagem de sucesso. Mensagem: Exclusão realizada com sucesso. Ao clicar em 'não' o usuário é redirecionado para tela Excluir Cliente.|
| TA01.10    | O usuário informa, na tela Excluir Cliente, os dados para identificar o cliente desejado, o cliente não existe. O usuário é notificado com uma mensagem de erro. Mensagem: Cliente não encontrado|

---

## 📦 RF02 - Manter Dívida
|||
|-|-|
|**Descrição:**| O sistema deve permitir cadastrar, editar, visualizar e excluir dívidas associadas a um cliente. Será possível registrar uma dívida informando o cliente, valor, data e descrição (ou cupom fiscal). Esse módulo é essencial para controlar os valores que os clientes devem ao comerciante.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Essencial          |
| Estimativa          | 6h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Arthur             |
| Desenvolvedor       | Arthur             |
| Revisor             | Júlia              |
| Testador            | Gean               |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA02.01    | O usuário informa, na tela Cadastrar Dívida, todos os dados corretamente (cliente válido, valor positivo, data). Ao clicar em salvar ele é notificado com uma mensagem de sucesso. Mensagem: Dívida cadastrada com sucesso.|
| TA02.02    | O usuário informa, na tela Cadastrar Dívida, um cliente inexistente. Ao clicar em salvar ele é notificado com uma mensagem de erro. Mensagem: Cliente não encontrado.|
| TA02.03    | O usuário informa, na tela Cadastrar Dívida, um valor inválido (zero ou negativo). Ao clicar em salvar ele é notificado com uma mensagem de erro. Mensagem: Valor inválido.|
| TA02.04    | O usuário informa, na tela Editar Dívida, os dados para identificar a dívida, a dívida existe, o usuário seleciona a dívida, em seguida são mostrados os campos para edição.|
| TA02.05    | O usuário informa, na tela Editar Dívida corretamente os dados para edição. Ao clicar em salvar ele é notificado com uma mensagem de sucesso. Mensagem: Edição realizada com sucesso.|
| TA02.06    | O usuário informa, na tela Editar Dívida, uma dívida inexistente. O usuário é notificado com uma mensagem de erro. Mensagem: Dívida não encontrada.|
| TA02.07    | O usuário informa, na tela Pesquisar Dívida, os dados para identificar a dívida, a dívida existe, o usuário seleciona a dívida e são exibidas suas informações.|
| TA02.08    | O usuário informa, na tela Pesquisar Dívida, os dados para identificar a dívida, a dívida não existe. O usuário é notificado com uma mensagem de erro. Mensagem: Dívida não encontrada.|
| TA02.09    | O usuário informa, na tela Excluir Dívida, os dados para identificar a dívida, a dívida existe. O usuário é notificado com uma mensagem de aviso. Mensagem: Deseja prosseguir com a ação?. Ao confirmar, a dívida é removida com sucesso.|
| TA02.10    | O usuário informa, na tela Excluir Dívida, uma dívida inexistente. O usuário é notificado com uma mensagem de erro. Mensagem: Dívida não encontrada.|