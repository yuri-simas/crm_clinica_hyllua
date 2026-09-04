# CRM Clínica Hyllua Husein — Resumo Executivo para Proposta

> Documento de apoio para montagem da proposta comercial.
> Base técnica completa em `premissas-projeto.md`. Protótipo navegável e publicado em
> https://yuri-simas.github.io/crm_clinica_hyllua/
> Atualizado em 2026-09-04.

---

## 1. O problema

A consultoria Maestri cobra da clínica um conjunto de indicadores comerciais mensais. Hoje **nenhum deles é medido**.

O que isso significa na prática:

- Não existe registro de quantas pessoas entram em contato, nem por qual canal
- Não se sabe quantos contatos viram consulta, nem quantas consultas viram venda
- Não se sabe o ticket médio, nem quanto cada procedimento representa do faturamento
- O sistema atual (Prontuário Verde) tem um CRM embutido, avaliado pela própria equipe como **"bom, porém bem limitado"**, e que exige muito ajuste manual

**O argumento de valor, na voz do próprio consultor deles:** um ganho de 3% a 5% em qualquer etapa do funil gera aumento considerável de faturamento. Mas só é possível melhorar o que é medido.

## 2. A solução

Um **painel comercial próprio**, acessível pelo navegador do computador e do celular, que registra o funil de ponta a ponta e transforma isso em indicadores mensais confiáveis — prontos para a reunião com a consultoria.

O sistema é **externo ao Prontuário Verde e não o substitui**: cuida da parte comercial, enquanto o prontuário, a anamnese e a agenda oficial continuam onde estão.

## 3. Situação atual — o que já existe

Este é o principal diferencial desta proposta em relação a um projeto começando do zero: **o protótipo está construído, publicado e navegável**, na identidade visual da clínica.

Já funcionando:

- Painel com os quatro indicadores principais e comparativo mês a mês
- Filtro por período e por especialidade (HOF e Odontológico)
- Lançamento de abordagens e de ofertas de procedimento
- Catálogo de procedimentos, canais de origem, atendentes e motivos de perda
- Login com dois perfis e sessão com expiração por inatividade
- Extração de relatórios em Excel, com cinco abas
- Três formas de visualização dos gráficos, salvas por usuário

**Use isso na apresentação.** O cliente não vai avaliar uma promessa: vai mexer no sistema.

## 4. O que será entregue — escopo da proposta

O protótipo prova o conceito, mas ainda **não é um sistema em operação**. Hoje os dados ficam salvos no navegador de cada pessoa: se a recepção lançar um contato, a gestão não vê. É exatamente essa distância que a proposta cobre.

### 4.1 Base do sistema

| Entrega | O que é |
|---|---|
| **Banco de dados online** | Base única e compartilhada, com backup automático. Todo mundo passa a ver a mesma informação |
| **Autenticação real** | Login por usuário e senha com as regras de acesso validadas no servidor, não apenas na tela |
| **Controle de perfis** | **Gestão** vê tudo; **Operador** só lança abordagens e negociações |
| **Publicação definitiva** | Endereço de acesso fixo, com HTTPS |

### 4.2 Módulo Captação (Funil 1)

- Registro de **toda abordagem recebida**, inclusive a que não vira consulta — é o denominador da conversão
- Canal de origem em lista fechada e configurável
- Classificação de paciente novo × antigo
- Marcação de consulta agendada e de comparecimento (no-show)
- Atendente responsável em cada lançamento
- **Lançamento otimizado para celular**, com poucos campos obrigatórios

### 4.3 Módulo Venda (Funil 2)

- Registro de **cada procedimento ofertado**, mesmo o que não fecha
- Um atendimento gera várias ofertas, cada uma com seu próprio desfecho
- Valor ofertado, valor fechado, status e motivo da perda em lista padronizada
- Alerta de oferta parada em negociação há muito tempo
- Catálogo de procedimentos com tecnologia, especialidade e valor de tabela

### 4.4 Painel de indicadores

Os indicadores exatamente como a consultoria pediu:

| Indicador | Cálculo |
|---|---|
| Conversão de consultas | consultas agendadas ÷ abordagens registradas |
| Conversão de procedimentos | fechados ÷ (fechados + perdidos) |
| Ticket médio | valor total fechado ÷ nº de procedimentos vendidos |
| Faturamento do mês | soma dos valores fechados |
| Paciente novo × antigo | quantidade e percentual sobre o total |
| Detalhamento de faturamento | por procedimento, tecnologia e especialidade |

Com **comparativo mês a mês** de cada um — que é justamente o "mapear para os próximos meses" que a consultoria pediu, e que a planilha atual não faz.

### 4.5 Relatórios em Excel

Arquivo `.xlsx` com cinco abas — resumo mensal, abordagens, negociações, detalhamento e origem — com período e especialidade selecionáveis. Colunas já formatadas como moeda, percentual e data, prontas para tabela dinâmica.

### 4.6 Implantação

- Cadastro do catálogo real de procedimentos, a partir da tabela de preços da clínica
- Cadastro dos canais de origem, atendentes e usuários
- Carga do histórico, se houver
- **Treinamento da equipe** e acompanhamento do primeiro mês de uso

> O treinamento não é formalidade. O maior risco do projeto é o lançamento não acontecer — ver seção 7.

## 5. Fora de escopo — registrar na proposta

Deixar explícito evita ruído depois:

- ❌ **Prontuário, anamnese, fotos e qualquer dado clínico** — continuam no Prontuário Verde
- ❌ **Agenda oficial da clínica** — o CRM só marca se houve agendamento, para fins de métrica
- ❌ **Financeiro completo** — contas a pagar, fluxo de caixa, conciliação
- ❌ **Controle de parcelas e recebimentos** — o faturamento é registrado pela data do fechamento
- ❌ **Perfil de acesso para a consultoria** — decidido ficar fora da primeira versão
- ❌ **Integrações** com Prontuário Verde, Verdesk, WhatsApp ou Ads — ver seção 8
- ❌ **Aplicativo de loja** — é sistema web, abre pelo navegador do celular

## 6. Arquitetura técnica

| Item | Definição |
|---|---|
| **Tipo** | Aplicação web responsiva, com o celular em primeiro lugar |
| **Instalação** | Nenhuma — acesso por link |
| **Banco de dados** | Supabase, em infraestrutura própria da Clínica, separada dos outros sistemas |
| **Hospedagem** | GitHub Pages, mesmo padrão já validado em outro sistema do grupo |
| **Autenticação** | Login com usuário e senha, permissões aplicadas no banco |
| **LGPD** | Sem dado clínico, acesso apenas com login, exportação restrita à Gestão |

**Argumento de custo:** essa arquitetura tem **custo de infraestrutura próximo de zero** no volume previsto. Não há mensalidade de servidor a repassar.

## 7. O risco do projeto — e como a proposta o trata

O próprio time da clínica identificou que o CRM do Prontuário Verde falha porque **o lançamento é manual**. Um sistema novo não muda isso sozinho — muda apenas onde a digitação acontece.

Três coisas fazem o projeto dar certo, e as três estão no escopo:

1. **Lançamento em segundos no celular** — a abordagem tem quatro campos obrigatórios
2. **Dono do dado definido** — o Operador lança, a Gestão confere no fechamento do mês
3. **Medir só o que vai para a reunião** — campo que ninguém olha vira campo que ninguém preenche

**Trate isso como diferencial, não como ressalva.** Mostra que o problema foi entendido de verdade, e não apenas a lista de telas.

## 8. Integrações — fase 2, precificada à parte

A documentação das APIs foi analisada. Situação real:

- São **duas APIs distintas**: a do Prontuário Verde (pacientes, agendas, orçamentos) e a do **Verdesk**, o CRM de WhatsApp deles (contatos, oportunidades, funis)
- Há caminho técnico viável, e a integração poderia automatizar boa parte do lançamento
- **Mas existem travas reais:** não há webhooks; a listagem de oportunidades não devolve telefone; não há filtro por data nem paginação documentada; e o uso exige plano do Prontuário Verde que inclua API

> **Recomendação:** manter fora do escopo principal, como **item opcional precificado à parte**, condicionado a: (a) o cliente confirmar que o plano dele inclui API, (b) o fornecimento das credenciais, e (c) um teste de viabilidade antes de virar compromisso. Isso protege prazo e valor.
>
> O cliente já decidiu **seguir sem integração** nesta fase. Registre na proposta como evolução mapeada — vende visão de futuro sem assumir risco.

## 9. Modelo comercial sugerido

Mesmo modelo dos demais projetos: **implantação (uma vez) + mensalidade**.

| Componente | O que cobre |
|---|---|
| **Implantação** | Banco, autenticação, publicação, os dois módulos, painel, relatórios, carga inicial e treinamento |
| **Mensalidade** | Hospedagem, backup, suporte, correções e pequenos ajustes de uso |
| **Opcional — Integração** | Fase 2, condicionada às travas da seção 8 |
| **Opcional — Evoluções** | Métricas complementares, perfil da consultoria, desempenho por atendente |

**Ao definir os valores, considere que:**

- O protótipo pronto **reduz o risco de execução** e encurta o prazo — é argumento para sustentar o valor, não para descontá-lo
- A infraestrutura custa quase nada, então a mensalidade sustenta **suporte e evolução**, não servidor
- O treinamento e o acompanhamento do primeiro mês são o que faz o sistema pegar. Não trate como brinde

## 10. Fases sugeridas

| Fase | Conteúdo | Depende de |
|---|---|---|
| **1 — Base** | Banco, login, perfis e publicação | Nada — pode começar já |
| **2 — Captação** | Módulo do Funil 1 e painel de conversão de consultas | Lista de canais de origem |
| **3 — Venda** | Módulo do Funil 2, painel completo e relatórios | **Tabela de preços da clínica** |
| **4 — Implantação** | Carga inicial, treinamento e primeiro mês acompanhado | Disponibilidade da equipe |
| **5 — Opcional** | Integrações | Plano com API e credenciais |

## 11. Pendências que impactam prazo e valor

Amarrar antes de fechar o número:

1. **Tabela de preços real e catálogo completo de procedimentos** — bloqueia a fase 3
2. **Lista fechada dos canais de origem**, e se dá para identificar o que leva a pessoa até o WhatsApp
3. **Existe histórico a importar?** Planilha, exportação do sistema atual, ou começa do zero
4. **Quantos usuários** terão acesso, e quantos são Operador
5. **As métricas complementares entram na v1?** Tempo de resposta, recompra, desempenho por atendente
6. **Prazo esperado** — a consultoria pediu para mapear os próximos meses, então provavelmente há data
7. **Endereço de acesso** — domínio próprio da clínica ou endereço nosso
8. **Regras ainda abertas:** prazo de corte da oferta "em negociação"; se a clínica vende pacotes de sessões

## 12. Argumentos de venda

- **O sistema já existe e pode ser usado na reunião.** Não é maquete: abre no celular e funciona
- **Responde exatamente ao que a consultoria cobra**, com as fórmulas que eles mesmos definiram
- **Feito na identidade visual da clínica**, com as cores e as fontes do branding book
- **Mostra domínio do problema:** apontamos cinco falhas na planilha de controle atual — ausência de registro de comparecimento, oferta em negociação sem prazo de corte, canal de origem em texto livre, coluna redundante e pacotes de sessões não previstos — e todas já estão resolvidas no protótipo
- **Vai além da planilha:** entrega o comparativo mês a mês, que é o que foi pedido e que a planilha atual não faz
- **Separa as duas especialidades**, HOF e Odontológico, que têm ticket e ciclo de decisão diferentes
- **Relatório em Excel de verdade**, com abas e colunas formatadas, pronto para a apresentação mensal
- **Custo de infraestrutura próximo de zero**
- **Preparado para crescer:** integrações, perfil da consultoria e novos indicadores já estão mapeados
