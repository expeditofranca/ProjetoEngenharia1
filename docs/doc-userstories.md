# 📝 Backlog do Produto

# Tabela contendo o planejamento inicial das funcionalidades:

| ID | Título do User Story | Requisitos Funcionais Relacionados | Responsável pelo Detalhamento |
|:---|:---|:---|:---|
| US01 | Manter Cliente | RF01.01, RF01.02, RF01.03, RF01.04 | Expedito |
| US02 | Manter Dívida | RF02.01, RF02.02, RF02.03, RF02.04 | Arthur |
| US03 | Controlar Pagamento | RF03 | Ivyson 
| US04 | Gerar Relatório de Pagamento | RF04 | Gean |
| US05 | Gerar Relatório de Histórico de Cliente | RF05 | Júlia
| US08 | Emitir Alerta de Inadimplência | RF08.01, RF08.02, RF08.03 | Arthur |


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
| Analista            | Ivyson             |
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

---

## 📦 User Story US03 - Controlar Pagamento

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** |  Deve ser possível registrar pagamentos totais ou parciais de uma dívida, atualizando automaticamente o saldo restante e o status da dívida. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF03          | Controlar Pagamento |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 4 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Gean                                | 
| **Desenvolvedor**         | Ivyson                              | 
| **Revisor**               | Arthur                              | 
| **Testador**              | Expedito                            | 


|**Teste de Aceitação (TA)** |  |
| ----------- | --------- |
| Código | Descrição |
| TA03.01 | O usuário informa, na tela de pagamento, o valor a ser pago (total ou parcial). Ao confirmar a operação, o sistema deve exibir uma mensagem de sucesso e mostrar o valor da dívida antes e após o pagamento. |
| TA03.02 | O sistema deve atualizar automaticamente o valor restante da dívida após o registro de um pagamento parcial. |
| TA03.03 | O sistema deve exibir uma mensagem de erro ao tentar registrar um pagamento com valor inválido (zero ou negativo). |
| TA03.04 | O sistema deve impedir o registro de pagamento com valor superior ao saldo da dívida. |
| TA03.05 | O sistema deve permitir registrar múltiplos pagamentos parciais para a mesma dívida, atualizando corretamente o saldo a cada pagamento. |
| TA03.06 | O sistema deve atualizar o status da dívida para “quitada” quando o valor do pagamento for igual ao saldo restante. |

---

## 📦 US04 - Gerar Relatório de Pagamento

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
|**Descrição:**| O sistema deve permitir que o comerciante gere relatórios contendo exclusivamente os registros de pagamentos realizados pelos clientes. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF04          | Gerar Relatório de Pagamento |

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Essencial          |
| Estimativa          | 3h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Ivyson             |
| Desenvolvedor       | Arthur             |
| Revisor             | Júlia              |
| Testador            | Gean               |

|**Teste de Aceitação (TA)** |  |
| ----------- | --------- |
| Código | Descrição |
|--------|-----------|
| TA04.01 | O usuário acessa a tela de Relatórios, seleciona o filtro de "Pagamentos" e clica em gerar. O sistema exibe a lista com sucesso. |
| TA04.02 | O usuário tenta gerar relatório para um período sem entradas. O sistema exibe: "Nenhum pagamento registrado." |

---

## 📦 US05 - Gerar Relatório de Histórico de Cliente 

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** |  O sistema deve possibilitar a geração de um relatório detalhado do histórico de compras fiadas e pagamentos de um cliente específico. O relatório deve incluir todas as dívidas, datas, produtos comprados, valores totais, pagamentos efetuados e situação atual da dívida do cliente (adimplente/inadimplente).|

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF05          | Gerar Relatório de Histórico de Cliente |

| Campo                     | Informação                          |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Importante                          | 
| **Estimativa**            | 4h                                  | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Arthur                              | 
| **Desenvolvedor**         | Júlia                               | 
| **Revisor**               | Gean                                | 
| **Testador**              | Expedito                            |

|**Teste de Aceitação (TA)** |  |
| ----------- | --------- |
| Código | Descrição |
| TA05.01 | O usuário acessa a tela de Relatórios, seleciona o filtro de "Histórico" e informa o CPF do cliente para o qual deseja gerar relatório de histórico. O sistema deve gerar e exibir com sucesso um relatório contendo todas as dívidas do cliente, com suas respectivas datas, produtos comprados, valores totais, pagamentos efetuados e situação atual da dívida do cliente (adimplente/inadimplente). |
| TA05.02 | Ao exibir o relatório de histórico de um cliente, o sistema deve permitir ao cliente escolher voltar para a tela de Relatórios, através de um botão, caso deseje gerar um novo relatório. |
| TA05.03 | Ao exibir o relatório de histórico de um cliente, o sistema deve permitir ao usuário escolher voltar para a tela principal através de um botão, caso deseje retornar ao menu principal. |
| TA05.04 | Ao informar o número de CPF de um cliente que não tenha dívidas cadastradas, o sistema deve exibir uma mensagem de aviso indicando que o cliente ainda não possui dívidas cadastradas. |

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
| TA07.01    | O usuário, ao cadastrar uma dívida para um cliente, caso este ultrapasse o limite de dívidas, recebe uma mensagem de aviso. Mensagem: Cliente 'xxxxx" ultrapassou o limite de dívidas. Em seguida recebe outra mensagem de aviso. Mensagem: Deseja prosseguir com a ação?. Ao clicar em 'sim', o usuário cadastra a dívida com sucesso. Ao clicar em 'não' o usuário retorna a tela Cadastrar Dívida.|

---

## 📦 RF08 - Emitir Alerta de Inadimplência
|||
|-|-|
|**Descrição:**| O sistema deve permitir identificar clientes inadimplentes com base em dívidas em atraso e emitir alertas para auxiliar o comerciante no acompanhamento desses casos. Os alertas devem considerar a data de vencimento das dívidas e a ausência de pagamento, permitindo visualizar facilmente os clientes com pendências financeiras.|

| Campo               | Informação         |
|---------------------|--------------------|
| Prioridade          | Importante         |
| Estimativa          | 5h                 |
| Tempo Gasto (real)  |                    |
| Tamanho Funcional   |                    |
| Analista            | Ivyson             |
| Desenvolvedor       | Arthur             |
| Revisor             | Júlia              |
| Testador            | Gean               |

|**Teste de Aceitação (TA)**||
|------------|-----------|
| Código     | Descrição |
| TA08.01    | O sistema identifica automaticamente dívidas com data de vencimento inferior à data atual e sem pagamento registrado.|
| TA08.02    | O usuário acessa a tela de alertas e visualiza a lista de clientes inadimplentes.|
| TA08.03    | O sistema exibe corretamente os dados do cliente e da dívida em atraso.|
| TA08.04    | O sistema não exibe clientes que não possuem dívidas em atraso.|
| TA08.05    | O sistema atualiza automaticamente a lista quando uma dívida é quitada.|
| TA08.06    | O sistema exibe mensagem informando que não há inadimplentes quando não houver registros. Mensagem: Nenhum cliente inadimplente encontrado.|
| TA08.07    | O usuário tenta acessar a tela de alertas e o sistema carrega corretamente sem erros.|