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

## Requisitos Funcionais

### US01 - Manter Cliente
Um cliente possui nome, CPF, telefone, endereço, profissão e renda familiar.

Requisito | Descrição | Ator |
----------|----------|------|
RF01.01 - Inserir Cliente | Cadastrar cliente informando nome, CPF, telefone, endereço, profissão e renda familiar. | Comerciante |
RF01.02 - Listar Clientes | Listar clientes cadastrados com filtros. | Comerciante |
RF01.03 - Atualizar Cliente | Editar dados de um cliente informando nome, telefone, endereço, profissão e renda familiar. | Comerciante |
RF01.04 - Deletar Cliente | Excluir cliente do sistema informando CPF. | Comerciante |

---

### RF02 - Manter Dívida
O sistema deve permitir ao comerciante gerenciar as dívidas dos clientes, possibilitando o cadastro, visualização, atualização e exclusão de dívidas. Cada dívida deve estar associada a um cliente previamente cadastrado e conter informações como valor, data e descrição.

- RF02.01 - Inserir Dívida  
- RF02.02 - Listar Dívidas  
- RF02.03 - Atualizar Dívida  
- RF02.04 - Deletar Dívida  

---

### RF04 - Gerar Relatório de Pagamento
O sistema deve permitir a geração de relatórios contendo os registros de pagamentos realizados pelos clientes, facilitando o controle financeiro da mercearia.

Requisito | Descrição | Ator |
----------|----------|------|
RF04.01 - Gerar Relatório | Gerar relatórios de pagamentos incluindo nome do cliente, valor pago e data do pagamento. | Comerciante |

---

### US07 - Alerta de Limite de Dívida
Após verificação, o sistema deve emitir um alerta ao comerciante informando o cliente devedor.

Requisito | Descrição | Ator |
----------|----------|------|
RF07.01 - Verificar Limite | Emitir alerta quando cliente ultrapassar limite de dívidas. | Administrador |

---

### RF08 - Emitir Alerta de Inadimplência
O sistema deve permitir identificar clientes inadimplentes com base em dívidas em atraso e emitir alertas para auxiliar o comerciante no acompanhamento desses casos. Os alertas devem considerar critérios como data de vencimento e ausência de pagamento.

- RF08.01 - Identificar Dívidas em Atraso  
- RF08.02 - Gerar Alerta de Inadimplência  
- RF08.03 - Listar Clientes Inadimplentes  

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