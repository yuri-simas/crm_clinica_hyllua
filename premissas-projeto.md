# Premissas do Projeto — CRM Clínica Hyllua Husein

> Documento de definição, gerado em 2026-08-27 a partir da conversa do grupo "MAESTRI — Hyllua Husein".
> **Revisado em 2026-08-27** com as respostas do cliente e a análise da planilha de referência `CRM_Clinica_HOF_Odonto.xlsx`.
> Itens marcados com ❓ são **pendências** que ainda precisam de resposta antes do desenvolvimento.

---

## 0. Decisões já fechadas (revisão de 2026-08-27)

| # | Pergunta | Decisão |
|---|---|---|
| 1 | Convivência com o Prontuário Verde | **Somente comercial.** O CRM é um painel externo ao Prontuário Verde (Verdesk). Não é agenda oficial nem prontuário. |
| 2 | Usuários e perfis | **Dois perfis: Gestão e Agente** (quem faz os lançamentos). Sem menção a mais de uma unidade — assumido **unidade única**. |
| 3 | Perfil somente-leitura para a consultoria | **Não entra na v1.** |
| 4 | Regras de cálculo | **Definidas pela planilha de referência** — ver seção 6.4. |
| 6 | Procedimentos e tecnologias | Lista-base recebida na planilha (seção 7.2). **Ainda falta a tabela de preços real.** |
| — | Especialidades | Novidade da planilha: a clínica opera **duas especialidades — HOF e Odontológico** — e toda métrica precisa poder ser filtrada por elas. |
| — | Motivos de perda | Lista fechada já definida (seção 6.3). |

---

## 1. Contexto e origem da demanda

O Ricardo (consultoria Maestri) cobrou da clínica o acompanhamento mensal de um conjunto de indicadores comerciais. Na conversa ficou claro que:

- **Hoje essas métricas não são medidas nem acompanhadas.** Não existe registro estruturado de quantas pessoas entram em contato, por qual canal, e quantas viram agendamento.
- A clínica usa hoje o **Prontuário Verde (Verdesk)**, que tem um CRM embutido. Avaliação do Felipe: *"bom, porém bem limitado"* — é focado em atendimento com IA e distribuiria bem os leads entre os funis, mas como **a Brenda (secretária) faz todo o agendamento manualmente**, a distribuição fica imprecisa e exige muitos ajustes/correções manuais.
- Por isso surgiu a alternativa de um **CRM personalizado**, no mesmo modelo do que já foi feito para o Instituto Hyllua Husein.

**Frase-chave do Ricardo que define o valor do projeto:** um aumento de 3% a 5% em qualquer etapa do funil gera aumento considerável de faturamento — mas só dá para melhorar o que é medido.

---

## 2. Objetivo do sistema

Registrar o **funil comercial da clínica** de ponta a ponta e transformar isso em indicadores mensais confiáveis, respondendo a estas perguntas:

1. Quantas pessoas entraram em contato neste mês, e por qual canal?
2. Quantas viraram consulta agendada?
3. Nas consultas, quantos procedimentos foram **ofertados** e quantos foram **fechados**?
4. Qual o ticket médio dos procedimentos vendidos?
5. Quanto faturamos, detalhado por procedimento, tecnologia e especialidade?
6. Quanto dos agendamentos do mês veio de **paciente novo** e quanto de **paciente antigo**?
7. Como cada indicador evolui **mês a mês**?

---

## 3. O que o sistema **NÃO** é — decidido: somente comercial

| Fica no CRM (novo sistema) | Continua no Prontuário Verde (Verdesk) |
|---|---|
| Lead / contato comercial | Prontuário e evolução clínica |
| Canal de origem e histórico de abordagem | Anamnese e fichas de avaliação |
| Agendamento **apenas como marcação de métrica** | **Agenda oficial da clínica** |
| Oferta de procedimento e fechamento | Fotos, laudos, dados de saúde |
| Valores vendidos e faturamento comercial | Prescrições |

- O CRM **não substitui o Prontuário Verde** e **não armazena dado clínico/de saúde**. Isso mantém o sistema fora da categoria de "dado pessoal sensível" da LGPD.
- **Consequência aceita:** a consulta será marcada nos dois lugares (agenda no Verdesk, registro de métrica no CRM). Para reduzir o atrito, o campo no CRM é mínimo — apenas "consulta agendada: sim/não" e a data.

---

## 4. Usuários e perfis de acesso — decidido

| Perfil | Quem | O que faz |
|---|---|---|
| **Gestão** | Elisa e direção | Tudo: dashboards, catálogo de procedimentos, canais, usuários, exportação |
| **Agente** | Recepção e consultores (ex.: Brenda, e as "Camila/Bruna" da planilha) | Lança abordagens, agendamentos, ofertas e fechamentos |

- **Unidade única** (não foi mencionada outra).
- Perfil somente-leitura para a consultoria **fica para depois**.
- Mesmo com só dois perfis, **cada lançamento guarda o atendente responsável** — a planilha já faz isso. Isso permite, sem custo nenhum, ver conversão e ticket por atendente mais adiante.

---

## 5. Modelo conceitual — os dois funis

```
FUNIL 1 — CAPTAÇÃO (dono: agente/recepção)

  Abordagem/contato ──> Consulta agendada
   (todo contato,              │
    mesmo sem virar            └─> Não agendou
    consulta)


FUNIL 2 — VENDA (dono: agente/consultor)

  Procedimento ofertado ──> Fechado ──> Faturado
            │
            ├─> Perdido (com motivo)
            └─> Em negociação (ainda sem desfecho)
```

**Consequência prática:** um mesmo paciente pode receber **várias ofertas de procedimento**, e cada oferta é uma linha com seu próprio desfecho. É assim que a planilha faz e é assim que o CRM tem que fazer — senão a conversão de procedimentos não fecha.

**Toda métrica precisa poder ser filtrada por especialidade: HOF ou Odontológico.**

### 5.1 Status

- **Abordagem:** consulta agendada — Sim / Não
- **Oferta:** Fechado · Perdido · Em negociação
- **Tipo de paciente:** Novo · Antigo

---

## 6. Métricas e indicadores

### 6.1 Painel principal (espelha o Dashboard da planilha)

| Indicador | Fórmula |
|---|---|
| **% Conversão de consultas** | consultas agendadas ÷ abordagens registradas no mês |
| **% Conversão de procedimentos** | fechados ÷ (fechados + perdidos) — **"em negociação" fica fora do denominador** |
| **Ticket médio** | soma dos valores fechados ÷ nº de procedimentos fechados |
| **Faturamento total do mês** | soma dos valores fechados no mês |
| **Pacientes novos × antigos** | contagem e % sobre o total de abordagens do mês |
| **Detalhamento de faturamento** | por procedimento × tecnologia: quantidade, faturamento, ticket médio e % do total |

**Além da planilha, o CRM entrega:** o comparativo **mês a mês** de cada indicador. Hoje o Dashboard mostra um mês por vez, e foi exatamente "mapear para os próximos meses" o que a consultoria pediu.

### 6.2 Definições que a planilha fixou

- **Abordagem** = **todo contato feito, mesmo que não vire consulta**. É a base da conversão de consultas.
- **Mês de competência** = **mês do evento**. A abordagem conta no mês do contato; a venda conta no mês da negociação.
- **Faturamento** = **regime de competência pela data do fechamento**, não pela data de recebimento das parcelas.
- **Paciente novo × antigo** = classificação manual do agente no momento da abordagem.
- **Valor fechado** só é preenchido quando o status é "Fechado".

### 6.3 Motivos de perda — lista fechada já definida

Preço · Sem retorno · Escolheu concorrente · Adiou decisão · Medo/insegurança · Indisponibilidade de agenda · Outro

### 6.4 Ajustes que recomendo sobre o modelo da planilha

Cinco pontos que a planilha deixa em aberto e que o CRM deveria resolver:

1. **Não existe registro de comparecimento (no-show).** O funil para em "consulta agendada: sim". Sem marcar se o paciente apareceu, não dá para separar "não vendeu" de "nem chegou a ser atendido" — e a conversão de procedimentos fica injustamente baixa. *Sugestão: um campo a mais na consulta — compareceu sim/não.*
2. **"Em negociação" precisa de prazo de validade.** Está corretamente fora do denominador, mas sem uma regra de corte uma oferta fica "em negociação" para sempre e nunca entra em nenhuma conta. *Sugestão: após X dias sem movimento, vira "Perdido — sem retorno". Definir o X com a clínica.*
3. **Origem do contato é texto livre na planilha.** "Instagram", "instagram" e "IG" viram três canais diferentes e o relatório de origem se perde. *No CRM tem que ser lista fechada.*
4. **A coluna "Abordagem Registrada" é redundante** — é sempre "Sim". No CRM, todo registro de lead já é uma abordagem, então o campo desaparece.
5. **Pacote de sessões.** A planilha trata cada oferta como uma venda de valor único. Se a clínica vende pacotes, confirmar que o pacote entra como **uma venda com o valor cheio**, e as sessões executadas são acompanhadas à parte, sem somar faturamento de novo.

### 6.5 Métricas complementares ❓

Continuam valendo como sugestão, e agora com o dado de atendente que a planilha já traz: taxa de comparecimento, tempo de resposta ao lead, ticket médio por paciente, taxa de recompra e desempenho por atendente. ❓ **Confirmar se entram na v1.**

---

## 7. Estrutura de dados

### 7.1 Entidades

- **Abordagem** — data, especialidade (HOF/Odontológico), nome do paciente, tipo de paciente (novo/antigo), origem do contato, consulta agendada (sim/não), data da consulta, atendente responsável, observações.
- **Oferta / Negociação** — data, especialidade, paciente, procedimento ofertado, tecnologia/técnica, valor ofertado, status, valor fechado, motivo da perda, atendente/consultor.
- **Catálogo de procedimentos** — nome, tecnologia/técnica, especialidade, valor de tabela, ativo/inativo.
- **Canais de origem** — lista configurável.
- **Usuários** — nome, login, perfil (Gestão/Agente).

### 7.2 Catálogo-base de procedimentos (recebido na planilha)

| Procedimento | Tecnologia/Técnica | Especialidade |
|---|---|---|
| Preenchimento Labial | Ácido Hialurônico | HOF |
| Toxina Botulínica | Botox | HOF |
| Bioestimulador | Sculptra / Radiesse | HOF |
| Fios de Sustentação | PDO | HOF |
| Clareamento Dental | Laser | Odontológico |
| Implante Dentário | Implante | Odontológico |
| Facetas / Lentes de Contato | Cerâmica | Odontológico |

❓ Esta é a lista genérica de exemplo da planilha, **sem preços**. Ainda precisamos da **tabela de preços real da clínica** e da confirmação de que a lista está completa.

### 7.3 Canais de origem

Aparecem na planilha, como texto livre: **Instagram, Indicação, Google**.

❓ Falta a lista real e fechada. E permanece a pergunta mais importante: como o WhatsApp concentra cerca de 90% dos contatos, **dá para o agente perguntar o que levou a pessoa até o WhatsApp** (anúncio, story, indicação)? Sem isso, a maior parte do funil vira uma caixa-preta chamada "WhatsApp".

---

## 8. Telas do sistema

1. **Dashboard** — os indicadores da seção 6.1, com seletor de mês, filtro por especialidade e **comparativo com os meses anteriores**.
2. **Abordagens** — lista e lançamento rápido do Funil 1.
3. **Negociações** — lista e lançamento do Funil 2, com o desfecho de cada oferta.
4. **Ficha do paciente** — abordagens e ofertas da mesma pessoa reunidas.
5. **Relatórios** — detalhamento de faturamento e exportação em Excel/CSV para a reunião mensal.
6. **Configurações** — catálogo de procedimentos, canais de origem, motivos de perda e usuários.

---

## 9. Requisitos técnicos

- **Aplicação web responsiva, com o celular em primeiro lugar.** O agente lança no meio do atendimento — se não for rápido no telefone, o sistema não é alimentado e as métricas morrem. Abre pelo navegador, sem instalar nada.
- **Mesma arquitetura já validada:** página única + **Supabase** (banco, autenticação e permissão por perfil), publicada no **GitHub Pages**.
- **Base de dados própria da Clínica**, separada do CRM do Instituto e do Gestão Hyllua.
- **Reaproveitamento** do CRM do Instituto: login, usuários, listas, ficha, exportação. O que é novo é o Funil 2, o dashboard de indicadores e o filtro por especialidade.
- **LGPD:** sem dado clínico, acesso só com login, exportação restrita à Gestão.
- ❓ Domínio de acesso.

---

## 10. Integrações futuras (não bloqueiam a v1)

| Integração | Valor | Situação |
|---|---|---|
| **Prontuário Verde / Verdesk** | Evitaria marcar a consulta duas vezes | ❓ Depende de API aberta no plano contratado — perguntar ao fornecedor |
| **WhatsApp oficial** | Criaria a abordagem sozinho no primeiro contato — resolveria o maior gargalo | Custo e aprovação Meta; fase 2 |
| **Meta / Google Ads** | Atribuir faturamento à campanha que gerou o contato | Fase 2 |

Todas são **aditivas**: só preenchem automaticamente campos que já existem. O projeto anda 100% com lançamento manual e ganha integração depois, sem retrabalho.

---

## 11. Risco principal

O Felipe apontou que o CRM do Prontuário Verde falha porque **o lançamento é manual**. Um CRM novo não resolve isso sozinho — só muda o lugar da digitação. E agora, com a decisão de manter a agenda no Verdesk, **a consulta será marcada nos dois sistemas**. Isso é aceitável, mas exige:

1. **Lançamento de poucos segundos no celular** — abordagem com quatro campos: paciente, especialidade, origem e se agendou.
2. **Dono do dado definido:** o Agente lança, a Gestão confere no fechamento do mês.
3. **Medir só o que vai para a reunião mensal.** Campo que ninguém olha vira campo que ninguém preenche.

---

## 12. Fases de entrega

**Fase 1 — Funil de captação**
Abordagens, canais de origem, tipo de paciente, consulta agendada, especialidade. Dashboard com conversão de consultas e origem novo × antigo.

**Fase 2 — Funil de venda**
Catálogo de procedimentos com tecnologia, oferta, status, valor fechado, motivo da perda. Dashboard com conversão de procedimentos, ticket médio, faturamento e detalhamento por procedimento/tecnologia.

**Fase 3 — Refino**
Comparativo mês a mês, exportação do fechamento, desempenho por atendente, no-show e as demais complementares aprovadas.

**Fase 4 — Integrações**, se fizerem sentido.

---

## 13. Pendências que continuam em aberto

1. **Tabela de preços real** da clínica e confirmação de que o catálogo de procedimentos está completo. *(seção 7.2)*
2. **Lista fechada de canais de origem** — e se dá para sub-classificar a origem dentro do WhatsApp. *(seção 7.3)*
3. **As métricas complementares entram na v1?** *(seção 6.5)*
4. **CPF e dados cadastrais completos** são necessários no CRM, ou basta o nome? *(a planilha só usa o nome)*
5. **Existe histórico a importar** — planilha em uso ou exportação do Verdesk — ou começa do zero?
6. **Prazo esperado.** A consultoria cobrou "mapear para os próximos meses", então provavelmente há data.
7. **Domínio / endereço de acesso.**
8. **Prazo de corte do "em negociação"** — depois de quantos dias sem movimento a oferta vira perdida? *(seção 6.4)*
9. **Registro de comparecimento (no-show)** entra no escopo? *(seção 6.4)*
10. **A clínica vende pacotes de sessões?** Se sim, confirmar a regra de contagem. *(seção 6.4)*
