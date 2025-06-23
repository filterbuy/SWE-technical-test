PRD – Projeto Base “E-commerce Skeleton” para Desafio de Pedidos
	1.	Propósito do projeto base
Fornecer ao candidato um repositório Django 5.0 funcional, com PostgreSQL e Django Rest Framework já configurados, contendo apenas um app “products”. O módulo “orders” deverá ficar ausente para que o candidato o crie durante o desafio.
	2.	Escopo
	•	Projeto Django inicializado com estrutura padrão.
	•	Conexão PostgreSQL via psycopg.
	•	DRF instalado e configurado com renderizador JSON e navegação browsable.
	•	App products com endpoints REST completos e documentados.
	•	Documentação automática de API via drf-spectacular.
	•	Script docker-compose.yml para subir DB e aplicação local.
	•	README detalhado com instruções de setup, execução e testes.
	3.	Fora de escopo
	•	Qualquer modelagem ou rota de pedidos.
	•	Autenticação e autorização.
	•	Processamento de pagamentos, estoque ou frete.
	4.	Personas
	•	Candidato Desenvolvedor: clona o repositório, roda localmente e implementa o módulo de pedidos.
	•	Entrevistador: observa e avalia o raciocínio e a codificação em tempo real.
	5.	User stories relevantes
	•	Como candidato, quero ter um projeto que roda em poucos minutos para focar na lógica de pedidos.
	•	Como candidato, quero exemplos claros de modelo, serializer e viewset no app products para seguir o mesmo padrão em orders.
	•	Como entrevistador, quero acessar a lista de produtos via API para testar criação de pedidos.
	6.	Requisitos funcionais
6.1 Configuração
- Variáveis de ambiente em .env.example para DB, debug e porta.
6.2 App products
- Modelo Product com campos id (UUID primário), name (str, até 120), price (decimal 10,2).
- Serializer detalhando validações básicas.
- ViewSet com list, retrieve, create, update, destroy.
- URLs registradas sob /api/products/.
6.3 Docs
- Rota /api/schema/ para schema OpenAPI.
- Rota /api/docs/ usando Swagger UI.
	7.	Requisitos não funcionais
	•	Python 3.12 mínimo.
	•	Padrão de código: Black, isort, flake8.
	•	Testes iniciais com pytest cobrindo ao menos 80 % de products.
	•	Build Docker em menos de 2 minutos em máquina moderna.
	•	Projeto deve subir com docker compose up --build sem intervenção.
	8.	Arquitetura e estrutura de pastas

ecommerce/
  ecommerce/        # settings, urls, asgi, wsgi
  products/
    migrations/
    models.py
    serializers.py
    views.py
    urls.py
    tests/
  manage.py
docker-compose.yml
Dockerfile
requirements.txt
README.md


	9.	Modelo de dados inicial

Product
  id           UUID        PK
  name         Char(120)
  price        Decimal(10,2)
  created_at   DateTime(auto_now_add)
  updated_at   DateTime(auto_now)


	10.	Endpoints já existentes

	•	GET    /api/products/ lista produtos
	•	POST   /api/products/ cria produto
	•	GET    /api/products/{uuid}/ detalhe
	•	PUT    /api/products/{uuid}/ atualiza
	•	DELETE /api/products/{uuid}/ remove
Todas retornam JSON conforme serializer.

	11.	Configuração de ambiente

	•	Usar Poetry ou pip-tools para gerenciar deps.
	•	Variável DATABASE_URL no formato postgres://user:pass@db:5432/ecommerce.
	•	Serviço db no docker compose usa imagem oficial postgres:16-alpine.

	12.	Guia rápido no README

git clone <repo>
cp .env.example .env
docker compose up --build
# acessar http://localhost:8000/api/docs/

	13.	Critério de pronto (Definition of Done) do projeto base

	•	docker compose up sobe a aplicação e exibe rota /api/docs/.
	•	Criar, listar e excluir um produto via Swagger funciona.
	•	pytest executa e retorna cobertura mínima de 80 %.
	•	Nenhum warning crítico em flake8.

