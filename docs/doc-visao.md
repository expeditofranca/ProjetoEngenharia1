# Documento de Visão

Documento construído a partir do **Modelo BSI - Documento de Visão**.

---

## Descrição do Projeto

O projeto consiste no desenvolvimento de um sistema para controle de vendas fiadas, permitindo que comerciantes gerenciem seus clientes, registrem dívidas, acompanhem pagamentos e emitam relatórios.

O sistema tem como objetivo principal facilitar o controle financeiro informal (fiado), oferecendo mais organização, segurança e visibilidade sobre débitos e pagamentos dos clientes.

---

## Equipe e Definição de Papéis

Membro     | Papel                  | E-mail |
-----------|------------------------|--------|
Arthur     | Analista / Desenvolvedor | arthur.dantas.017@ufrn.edu.br |
Expedito   | Desenvolvedor          | francaexpedito11@gmail.com |
Júlia      | Testadora / Revisora   | julia.lilian.706@ufrn.edu.br |
Gean       | Testador               | jose.gean.706@ufrn.edu.br |
Ivyson     | Analista / Desenvolvedor | ivysonwanderson@hotmail.com |

### Matriz de Competências

Membro     | Competências |
-----------|-------------|
Arthur     | Desenvolvimento Web, Python, Django |
Expedito   | Desenvolvimento Backend, Python, Django |
Júlia      | Testes de Software, Python, Django |
Gean       | Testes e Validação, Python, Django |
Ivyson     | Análise de Sistemas, Python, Django |

---

## Perfis dos Usuários

Perfil | Descrição |
-------|----------|
Comerciante | Usuário principal do sistema, responsável por cadastrar clientes, registrar dívidas, controlar pagamentos e gerar relatórios. |
Administrador | Pode gerenciar todo o sistema (mesmas permissões do comerciante, podendo incluir configurações futuras). |

---

## Requisitos Funcionais

### RF01 - Manter Cliente
Um cliente possui nome, CPF, telefone, endereço, profissão e renda familiar.

Requisito | Descrição | Ator |
----------|----------|------|
RF01.01 - Inserir Cliente | Cadastrar cliente informando nome, CPF, telefone, endereço, profissão e renda familiar | Comerciante |
RF01.02 - Listar Clientes | Listar clientes cadastrados com filtros | Comerciante |
RF01.03 - Atualizar Cliente | Editar dados de um cliente informando nome, telefone, endereço, profissão e renda familiar | Comerciante |
RF01.04 - Deletar Cliente | Excluir cliente do sistema informando CPF | Comerciante |

---

### RF02 - Manter Dívida
O sistema deve permitir ao comerciante gerenciar as dívidas dos clientes, possibilitando o cadastro, visualização, atualização e exclusão de dívidas. Cada dívida deve estar associada a um cliente previamente cadastrado e conter informações como valor, data e descrição.

Requisito | Descrição | Ator |
----------|----------|------|
RF02.01 - Inserir Dívida | Cadastrar dívida informando nome do cliente, responsável pela venda, data da dívida, valor total, número do cupom fiscal e status da dívida | Comerciante |
RF02.02 - Listar Dívidas | Listar dívidas cadastradas com filtros | Comerciante |
RF02.03 - Atualizar Dívida | Editar dados de uma dívida informando nome do cliente, responsável pela venda, data da dívida, valor total, número do cupom fiscal e status da dívida | Comerciante |
RF02.04 - Deletar Dívida | Excluir dívida do sistema informando CPF | Comerciante |

---

<!-- REQUISITO RF03??? -->
<!-- Dúvida: Cadê o RF03 aqui??? Por que não tem aqui se tem no Doc DE user stories, no US03?? -->

### RF04 - Gerar Relatório de Pagamento
O sistema deve permitir a geração de relatórios contendo os registros de pagamentos realizados pelos clientes, facilitando o controle financeiro da mercearia.

Requisito | Descrição | Ator |
----------|----------|------|
RF04.01 - Gerar Relatório | Gerar relatórios de pagamentos incluindo nome do cliente, valor pago e data do pagamento. | Comerciante |

---

### RF05 - Gerar Relatório de Histórico de Dívidas de Cliente
O sistema deve permitir a geração de relatórios das dívidas de um cliente, contendo informações como data, produtos adquiridos, valor total, valores pagos, status (adimplente/inadimplente), por meio de busca do CPF do cliente.

Requisito | Descrição | Ator |
----------|----------|------|
RF05.01 - Gerar Relatório de Histórico de Dividas| Gerar relatórios de histórico de dívidas por cliente incluindo data, produtos comprados, valor total, valores pagos e status da dívida (adimplente/inadimplente). | Comerciante |

---

### RF06 - Gerar Relatórios Mensais de Dívidas
O sistema deve permitir a geração de relatórios mensais contendo todos os clientes com dívidas em aberto, facilitando o acompanhamento das pendências financeiras.

Requisito | Descrição | Ator |
----------|----------|------|
RF06.01 - Gerar Relatório Mensal | Gerar relatório mensal contendo nome do cliente, valor da dívida e data da dívida | Comerciante |
RF06.02 - Listar Clientes com Dívidas | Listar clientes que possuem dívidas em aberto no período mensal | Comerciante |

### RF07 - Alerta de Limite de Dívida
Após verificação, o sistema deve emitir um alerta ao comerciante informando que o valor total das dívidas inadimplentes de um cliente ultrapassou o valor de um salário mínimo.

Requisito | Descrição | Ator |
----------|----------|------|
RF07.01 - Calcular Total de Dívidas | Realizar somatório total de todos os valores das dívidas inadimplentes de um cliente | Administrador |
RF07.02 - Verificar Limite | Verificar se a soma total dos valores de dívidas inadimplentes de um cliente ultrapassa o limite de um salário mínimo | Administrador |
RF07.03 - Emitir Alerta de Limite | Emitir alerta quando cliente ultrapassar limite de valor de dívidas | Administrador |

---

### RF08 - Emitir Alerta de Inadimplência
O sistema deve permitir identificar clientes inadimplentes com base em dívidas em atraso e emitir alertas para auxiliar o comerciante no acompanhamento desses casos. Os alertas devem considerar critérios como data de vencimento e ausência de pagamento.

Requisito | Descrição | Ator |
----------|----------|------|
RF08.01 - Identificar Dívidas em Atraso | Indetificar divídas de um cliente com status de Inadimplência | Comerciante |
RF08.02 - Gerar Alerta de Inadimplência | Emitir alerta de cliente inadimplente com base em 1 ou mais dívidas que estejam inadimplentes | Comerciante
RF08.03 - Listar Clientes Inadimplentes | Listar todos os clientes que estejam com dívidas inadimplentes | Comerciante |

---

## Lista de Requisitos Não-Funcionais

Requisito | Descrição |
-----------|----------|
RNF001 - Acesso Web | O sistema deve ser acessível via navegador (Chrome, Firefox, Edge). |
RNF002 - Performance | As consultas devem ser rápidas e eficientes. |
RNF003 - Segurança | Os dados dos clientes devem ser protegidos. |
RNF004 - Usabilidade | Interface simples e intuitiva para o comerciante. |
RNF005 - Disponibilidade | O sistema deve estar disponível sempre que necessário. |

---

## Riscos

Data | Risco | Prioridade | Responsável | Status | Solução |
------|------|-----------|-------------|--------|--------|
25/03/2026 | Falta de experiência da equipe | Alta | Equipe | Em andamento | Estudo contínuo e prática |
25/03/2026 | Atrasos no desenvolvimento | Média | Gerente | Em andamento | Planejamento e divisão de tarefas |
25/03/2026 | Problemas técnicos com tecnologias | Média | Equipe | Em andamento | Pesquisa e suporte técnico |

---