# 📝 Backlog do Produto

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
|**Descrição:**|  O sistema deve permitir registrar, visualizar, editar e desativar compras fiadas realizadas pelos clientes. Cada registro deve conter o nome do cliente, CPF do cliente, nome do responsável pela venda, data da dívida, valor total, número do cupom fiscal e status da dívida.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Essencial          |
| Estimativa          | 4h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Ivyson             |
| Desenvolvedor       | Arthur             |
| Revisor             | Expedito           |
| Testador            | Júlia              |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA02.01    | O usuário informa, na tela Cadastrar Dívida, todos os dados para o cadastro corretamente, ao clicar em salvar ele é notificado com uma mensagem de sucesso. Mensagem: Cadastro realizado com sucesso.|
| TA02.02    | O usuário informa, na tela Cadastrar Dívida, os dados para o cadastro incorretamente, ao clicar em salvar ele é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente.|
| TA02.03    | O usuário informa, na tela Cadastrar Dívida, todos os dados para o cadastro corretamente, mas o CPF não está cadastrado no sistema. Ao clicar em salvar ele é notificado com uma mensagem de erro. Mensagem: O CPF informado não está cadastrado no sistema.|
| TA02.04    | O usuário informa, na tela Pesquisar Dívida, os dados para identificar a dívida desejada, a dívida existe, o usuário seleciona a dívida, em seguida são mostradas as informações sobre a dívida.|
| TA02.05    | O usuário informa, na tela Pesquisar Dívida, os dados para identificar a dívida desejada, a dívida não existe. O usuário é notificado com uma mensagem de erro. Mensagem: Dívida não encontrada.|
| TA02.06    | O usuário informa, na tela Editar Dívida, os dados para identificar a dívida desejada, a dívida existe, o usuário seleciona a dívida, em seguida são mostrados os campos para edição.|
| TA02.07    | O usuário informa, na tela Editar Dívida, os dados para identificar a dívida desejada, a dívida não existe. O usuário é notificado com uma mensagem de erro. Mensagem: Dívida não encontrada.|
| TA02.08    | O usuário informa, na tela Editar Dívida, corretamente os dados para edição. Ao clicar em salvar ele é notificado com uma mensagem de sucesso. Mensagem: Edição realizada com sucesso.|
| TA02.09    | O usuário informa, na tela Editar Dívida, incorretamente os dados para edição. Ao clicar em salvar ele é notificado com uma mensagem de erro. Mensagem: Edição não realizada, o campo “xxxx” não foi informado corretamente.|
| TA02.10    | O usuário informa, na tela Excluir Dívida, os dados para identificar a dívida desejada, a dívida existe, o usuário seleciona a dívida. O usuário é notificado com uma mensagem de aviso. Mensagem: Deseja prosseguir com a ação?. Ao clicar em 'sim' o usuário é notificado com uma mensagem de sucesso. Mensagem: Exclusão realizada com sucesso. Ao clicar em 'não' o usuário é redirecionado para tela Excluir Dívida.|
| TA02.11    | O usuário informa, na tela Excluir Dívida, os dados para identificar a dívida desejada, a dívida não existe. O usuário é notificado com uma mensagem de erro. Mensagem: Dívida não encontrada|

---

## 📦 RF03 - Controlar Pagamento
|||
|-|-|
|**Descrição:**|  Deve ser possível registrar pagamentos realizados, sejam eles totais ou parciais, atualizando automaticamente o valor da dívida restante do cliente.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Essencial          |
| Estimativa          | 4h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Gean               |
| Desenvolvedor       | Ivyson             |
| Revisor             | Arthur             |
| Testador            | Expedito           |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA03.01    | (DEPOIS)  |
| TA03.02    |           |
| TA03.03    |           |
| TA03.04    |           |
| TA03.05    |           |

---

## 📦 RF04 - Gerar Relatório de Pagamento
|||
|-|-|
|**Descrição:**|  Permite gerar relatórios contendo os registros de pagamentos realizados pelos clientes.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Essencial          |
| Estimativa          | 2h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Júlia              |
| Desenvolvedor       | Gean               |
| Revisor             | Ivyson             |
| Testador            | Arthur             |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA04.01    | (DEPOIS)  |
| TA04.02    |           |
| TA04.03    |           |
| TA04.04    |           |
| TA04.05    |           |

---

## 📦 RF05 - Gerar Relatório de Histórico de Cliente
|||
|-|-|
|**Descrição:**|  Permite gerar um relatório detalhado do histórico de compras fiadas e pagamentos de cada cliente.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Importante         |
| Estimativa          | 2h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Expedito           |
| Desenvolvedor       | Júlia              |
| Revisor             | Gean               |
| Testador            | Ivyson             |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA05.01    | (DEPOIS)  |
| TA05.02    |           |
| TA05.03    |           |
| TA05.04    |           |
| TA05.05    |           |

---

## 📦 RF06 - Gerar Relatórios Mensais
|||
|-|-|
|**Descrição:**|  Gerar relatórios mensais com todos os clientes que estão com dívidas em aberto.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Opcional           |
| Estimativa          | 2h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Expedito           |
| Desenvolvedor       | Júlia              |
| Revisor             | Gean               |
| Testador            | Ivyson             |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA06.01    | (DEPOIS)  |
| TA06.02    |           |
| TA06.03    |           |
| TA06.04    |           |
| TA06.05    |           |

---

## 📦 RF07 - Emitir Alerta por Limite de Dívida
|||
|-|-|
|**Descrição:**| Caso o valor total do fiado de um cliente ultrapasse o valor de um salário mínimo, o sistema deve emitir um alerta para o comerciante.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Importante         |
| Estimativa          | 2h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Arthur             |
| Desenvolvedor       | Expedito           |
| Revisor             | Júlia              |
| Testador            | Gean               |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA07.01    | (DEPOIS)  |
| TA07.02    |           |
| TA07.03    |           |
| TA07.04    |           |
| TA07.05    |           |

---

## 📦 RF08 - Emitir Alerta de Inadimplência
|||
|-|-|
|**Descrição:**| Quando um cliente passar mais de 30 dias sem efetuar pagamento, o sistema deve emitir um alerta automático indicando a inadimplência.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Importante         |
| Estimativa          | 2h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Ivyson             |
| Desenvolvedor       | Arthur             |
| Revisor             | Expedito           |
| Testador            | Júlia              |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA08.01    | (DEPOIS)  |
| TA08.02    |           |
| TA08.03    |           |
| TA08.04    |           |
| TA08.05    |           |

---

## 📦 RF09 - Consultar Histórico de Cliente
|||
|-|-|
|**Descrição:**| Listar o histórico completo de compras e pagamentos de um cliente específico.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Importante         |
| Estimativa          | 2h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Gean               |
| Desenvolvedor       | Ivyson             |
| Revisor             | Arthur             |
| Testador            | Expedito           |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA09.01    | (DEPOIS)  |
| TA09.02    |           |
| TA09.03    |           |
| TA09.04    |           |
| TA09.05    |           |

---

## 📦 RF10 - Buscar Clientes Cadastrados
|||
|-|-|
|**Descrição:**| Permitir buscar clientes cadastrados utilizando nome, CPF ou status (ativo/inativo).|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Importante         |
| Estimativa          | 2h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Júlia              |
| Desenvolvedor       | Gean               |
| Revisor             | Ivyson             |
| Testador            | Arthur             |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA10.01    | (DEPOIS)  |
| TA10.02    |           |
| TA10.03    |           |
| TA10.04    |           |
| TA10.05    |           |