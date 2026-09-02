# CRM Comercial — Clínica Hyllua Husein

Painel comercial externo ao Prontuário Verde (Verdesk), para medir o funil da clínica
de ponta a ponta: do primeiro contato ao procedimento fechado e faturado.

## Links

| Página | Arquivo | O que é |
|---|---|---|
| Protótipo (app) | `index.html` | MVP funcional, com dados de exemplo |
| Apresentação | `deck.html` | Deck de 17 slides na identidade da clínica |
| Documento de definição | `apresentacao.html` | Escopo completo e pontos em aberto |
| Premissas | `premissas-projeto.md` | Documento de trabalho, em markdown |

## Estado

Protótipo para validação de telas e fluxo. Os lançamentos ficam salvos **no navegador
de quem abre** (localStorage) — cada pessoa vê a própria cópia, começando pelos dados
de exemplo. Não serve para operar ainda.

Na versão de produção os dados vão para o Supabase, com login por perfil (Gestão e
Agente) e base única compartilhada.

## Como editar

`index.html` e `deck.html` são **gerados** — não edite direto. Edite os templates e rode:

```bash
python build.py
```

O script embarca as fontes (Scotch Text e Neue Montreal) e os logotipos do branding
book dentro dos arquivos finais, para que funcionem offline.

Os arquivos de marca não ficam neste repositório; o caminho para eles está no topo
do `build.py`.

## Regras de cálculo

- **Abordagem** — todo contato recebido, mesmo o que não vira consulta.
- **Competência** — mês do evento: a abordagem conta no mês do contato, a venda no mês da negociação.
- **Conversão de consultas** — consultas agendadas ÷ abordagens registradas.
- **Conversão de procedimentos** — fechados ÷ (fechados + perdidos). "Em negociação" fica fora.
- **Ticket médio** — soma dos valores fechados ÷ nº de procedimentos vendidos.
- **Faturamento** — pela data do fechamento, não pelas parcelas.
