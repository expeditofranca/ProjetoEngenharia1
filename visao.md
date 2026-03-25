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
Júlia      | Testadora / Revisora   | juliajs.costa@gmail.com |
Gean       | Testador               | jose.gean.706@ufrn.edu.br |
Ivyson     | Analista / Desenvolvedor | ivysonwanderson@hotmail.com |

### Matriz de Competências

Membro     | Competências |
-----------|-------------|
Arthur     | Python, Django, Desenvolvimento Web |
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

## Lista de Requisitos Funcionais

### US01 - Manter Cliente

Requisito | Descrição | Ator |
----------|----------|------|
RF01.01 - Inserir Cliente | Cadastrar cliente com nome, CPF, telefone, endereço, profissão e renda familiar. | Comerciante |
RF01.02 - Listar Clientes | Listar clientes cadastrados com filtros. | Comerciante |
RF01.03 - Atualizar Cliente | Editar dados de um cliente existente. | Comerciante |
RF01.04 - Deletar Cliente | Excluir cliente do sistema. | Comerciante |

---

### US02 - Manter Dívida

Requisito | Descrição | Ator |
----------|----------|------|
RF02.01 - Inserir Dívida | Registrar uma nova dívida com dados do cliente, valor, data e cupom fiscal. | Comerciante |
RF02.02 - Listar Dívidas | Visualizar dívidas cadastradas. | Comerciante |
RF02.03 - Atualizar Dívida | Editar informações da dívida. | Comerciante |
RF02.04 - Deletar Dívida | Remover dívida do sistema. | Comerciante |

---

### US03 - Controlar Pagamento

Requisito | Descrição | Ator |
----------|----------|------|
RF03.01 - Registrar Pagamento | Registrar pagamentos totais ou parciais de uma dívida. | Comerciante |
RF03.02 - Atualizar Saldo | Atualizar automaticamente o valor restante da dívida. | Sistema |

---

### US04 - Gerar Relatórios de Pagamento

Requisito | Descrição | Ator |
----------|----------|------|
RF04.01 - Gerar Relatório Geral | Gerar relatórios com base em filtros. | Comerciante |
RF04.02 - Relatório Semanal | Gerar relatório da última semana. | Comerciante |
RF04.03 - Relatório Mensal | Gerar relatório do último mês. | Comerciante |
RF04.04 - Relatório Semestral | Gerar relatório dos últimos 6 meses. | Comerciante |

---

### US05 - Relatório de Histórico do Cliente

Requisito | Descrição | Ator |
----------|----------|------|
RF05.01 - Gerar Histórico | Gerar relatório detalhado de um cliente. | Comerciante |

---

### US06 - Relatórios Mensais de Dívidas

Requisito | Descrição | Ator |
----------|----------|------|
RF06.01 - Gerar Relatório Mensal | Listar clientes com dívidas em aberto. | Comerciante |

---

### US07 - Alerta de Limite de Dívida

Requisito | Descrição | Ator |
----------|----------|------|
RF07.01 - Verificar Limite | Emitir alerta quando cliente ultrapassar limite de dívida. | Sistema |

---

### US08 - Alerta de Inadimplência

Requisito | Descrição | Ator |
----------|----------|------|
RF08.01 - Detectar Inadimplência | Emitir alerta após 30 dias sem pagamento. | Sistema |

---

### US09 - Consultar Histórico

Requisito | Descrição | Ator |
----------|----------|------|
RF09.01 - Consultar Histórico | Visualizar histórico completo do cliente. | Comerciante |

---

### US10 - Buscar Clientes

Requisito | Descrição | Ator |
----------|----------|------|
RF10.01 - Buscar por Nome | Buscar clientes por nome. | Comerciante |
RF10.02 - Buscar por CPF | Buscar clientes por CPF. | Comerciante |
RF10.03 - Buscar por Status | Buscar clientes por status. | Comerciante |

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

## Referências

- Documento de Backlog do Produto
- Modelo BSI de Documento de Visão