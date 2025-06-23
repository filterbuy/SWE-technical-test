# Instruções ao Candidato – Desafio Live de Pedidos (Orders)

**Tempo total do exercício:** 40 minutos

---

## 1. Contexto
Você receberá um projeto **Django 5.0** já configurado com **PostgreSQL** e um app **`products`** contendo o modelo `Product(id, name, price)`.

Seu objetivo é implementar o módulo **`orders`** usando **Django Rest Framework**.

Durante a sessão você poderá — e é incentivado a — utilizar ferramentas de IA (ChatGPT, Copilot, etc.). Esteja preparado para comentar:
- Quais prompts ou comandos usou.
- Como validou a saída gerada.
- Quais ajustes manuais realizou.


## 2. Cronograma sugerido
| Período | Atividades sugeridas |
| --- | --- |
| **0 – 10 min** | • Ler rapidamente o README e o código existente.  <br>• Fazer **perguntas de clarificação** ao entrevistador para resolver qualquer dúvida. |
| **10 – 35 min** | • Definir as entidades (modelos) necessárias para representar um **pedido** e seus **itens**.  <br>• Implementar rotas e lógica básicas no DRF para criar um pedido e consultá-lo. |
| **35 – 40 min** | • Demonstrar o fluxo principal (criação e consulta) usando `curl`, HTTPie ou testes rápidos.  <br>• Explicar decisões, possíveis melhorias e como a IA ajudou. |

> ☝️ O tempo é curto; foque em entregar um fluxo principal funcionando. Boas práticas são bem-vindas, mas evite over-engineering.


## 3. Critérios de avaliação (peso aproximado)
| Critério | Peso |
| --- | --- |
| Clareza ao levantar requisitos e comunicar decisões | **25 %** |
| Código funcional, legível e testável | **30 %** |
| Estrutura de dados / API adequada ao problema | **20 %** |
| Uso consciente e explicado de IA | **15 %** |
| Boas práticas de Git e organização do projeto | **10 %** |


## 4. Ferramentas permitidas
Qualquer editor/IDE, documentação on-line, bibliotecas do PyPI, ChatGPT, Copilot ou similares.  
**Se usar, cite a ferramenta e explique brevemente como auxiliou.**


## 5. Critério mínimo para aprovação
- Fluxo principal de criação e consulta de pedido funciona (retorno **201/200**).  
- Você faz **ao menos duas** perguntas relevantes de clarificação antes de codar.  
- O projeto sobe (`docker compose up --build`) sem intervenção manual.  

Boa sorte! 🚀 