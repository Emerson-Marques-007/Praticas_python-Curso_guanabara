# 🐍 Projetos de Prática em Python

Repositório criado para registrar minha evolução nos estudos de **Python e lógica de programação**.

Os projetos deste repositório são **projetos de prática**, desenvolvidos para reforçar os conceitos estudados no curso e transformar teoria em código. O foco é construir pequenos programas funcionais, principalmente com menus interativos, funções, condições, laços de repetição, cálculos, validações e, gradualmente, estruturas de dados e módulos.

Além dos projetos práticos, também vou continuar minha formação por meio do **Curso de Python do Gustavo Guanabara (Curso em Vídeo)**, avançando para os **Mundos 2 e 3** conforme consolidar os fundamentos.

---

## 📚 Projetos desenvolvidos

### ✅ 1. Calculadora

Calculadora interativa com menu de operações matemáticas.

#### Funcionalidades implementadas

- Soma
- Subtração
- Multiplicação
- Divisão
- Entrada de dois números pelo usuário
- Menu interativo
- Opção para encerrar o programa
- Uso de função para receber os números
- Formatação dos resultados com `f-string`

#### Conceitos praticados

- `input()`
- `float()`
- Funções
- `return`
- `while True`
- `if / elif / else`
- Operadores matemáticos
- `f-string`

---

### ✅ 2. Conversor de Moedas

Programa para realizar conversões entre Real, Dólar e Euro.

#### Funcionalidades implementadas

- Real → Dólar
- Dólar → Real
- Real → Euro
- Euro → Real
- Menu interativo
- Entrada do valor pelo usuário
- Repetição do programa até escolher sair
- Formatação dos valores monetários
- Validação de opção do menu

#### Conceitos praticados

- Funções
- `return`
- `while True`
- Condições
- `float()` e `int()`
- Operações matemáticas
- `f-string`

---

### ✅ 3. Calculadora de Média

Programa que recebe notas de três bimestres e calcula a média do aluno.

#### Funcionalidades implementadas

- Entrada de três notas
- Soma das notas
- Cálculo da média
- Classificação da situação escolar
- Exibição da média formatada

#### Regras implementadas

- Média menor que 5 → **Reprovado**
- Média entre 5 e 5,99 → **Recuperação**
- Média igual ou superior a 6 → **Aprovado**

#### Conceitos praticados

- Funções
- Funções chamando outras funções
- `return`
- `float()`
- Operações matemáticas
- `if / elif / else`
- `f-string`

---

### ✅ 4. Caixa Eletrônico

Sistema simples de caixa eletrônico desenvolvido para praticar lógica de programação e manipulação de valores durante a execução do programa.

#### Funcionalidades implementadas

- Consultar saldo
- Depositar dinheiro
- Sacar dinheiro
- Exibir saldo atualizado
- Menu interativo
- Limpeza do terminal
- Mensagens de confirmação
- Retorno ao menu após cada operação

#### Validações implementadas

- Impedir saque maior que o saldo disponível
- Impedir valores negativos
- Impedir depósitos inválidos
- Informar opção de menu inválida

#### Conceitos praticados

- `while True`
- Funções
- Parâmetros
- Variáveis mutáveis
- `if / elif / else`
- `os.system()`
- `os.name`
- `float()`
- `f-string`
- Validação de dados

---

### ✅ 5. Conversor de Temperatura

Conversor de temperaturas com diferentes unidades e menu interativo.

#### Funcionalidades implementadas

- Celsius → Fahrenheit
- Fahrenheit → Celsius
- Celsius → Kelvin
- Kelvin → Celsius
- Menu interativo
- Repetição até escolher sair
- Limpeza do terminal
- Formatação dos resultados
- Validação de opção inválida

#### Fórmulas utilizadas

**Celsius → Fahrenheit**

```text
F = (C × 9/5) + 32
```

**Fahrenheit → Celsius**

```text
C = (F - 32) × 5/9
```

**Celsius → Kelvin**

```text
K = C + 273,15
```

**Kelvin → Celsius**

```text
C = K - 273,15
```

#### Conceitos praticados

- Funções
- `while True`
- `if / elif / else`
- `input()`
- `float()` e `int()`
- Operações matemáticas
- `os.system()`
- `f-string`

---

### ✅ 6. Calculadora de Área

Calculadora para determinar a área de diferentes figuras geométricas.

#### Funcionalidades implementadas

- Área do quadrado
- Área do retângulo
- Área do triângulo
- Área do círculo
- Menu interativo
- Entrada das medidas pelo usuário
- Exibição dos resultados
- Limpeza do terminal
- Uso de funções separadas para cada cálculo

#### Fórmulas utilizadas

**Quadrado**

```text
Área = lado²
```

**Retângulo**

```text
Área = base × altura
```

**Triângulo**

```text
Área = (base × altura) / 2
```

**Círculo**

```text
Área = π × raio²
```

#### Conceitos praticados

- Funções
- `return`
- Parâmetros e argumentos
- `math`
- `math.pi`
- `math.pow()`
- Operadores matemáticos
- `while True`
- Condições
- `f-string`

---

### ✅ 7. Calculadora de Desconto

Programa simples para calcular o desconto de um produto a partir do preço e de um percentual informado pelo usuário.

#### Funcionalidades implementadas

- Entrada do preço do produto
- Entrada do percentual de desconto
- Cálculo do valor do desconto
- Cálculo do preço final
- Exibição do resultado

#### Fórmula utilizada

```text
Desconto = preço × (percentual / 100)
Preço final = preço - desconto
```

#### Conceitos praticados

- `input()`
- `float()`
- `int()`
- Porcentagem
- Operações matemáticas
- Variáveis
- `print()`

---

## 🧠 Conceitos estudados até agora

Durante o desenvolvimento dos projetos, foram praticados os seguintes fundamentos de Python:

- Variáveis
- Tipos de dados
- `input()` e `print()`
- Conversão de tipos com `int()` e `float()`
- Operadores matemáticos
- Operadores de comparação
- `if / elif / else`
- `while True`
- `break`
- Funções
- Parâmetros
- `return`
- Funções que chamam outras funções
- `f-string`
- Formatação numérica com `:.1f` e `:.2f`
- Módulos com `import`
- Biblioteca `os`
- Biblioteca `math`
- Limpeza do terminal com `cls` / `clear`
- Validação básica de entradas
- Menus interativos

---

## 📈 Evolução dos projetos

```text
Calculadora
    ↓
Conversor de Moedas
    ↓
Calculadora de Média
    ↓
Caixa Eletrônico
    ↓
Conversor de Temperatura
    ↓
Calculadora de Área
    ↓
Calculadora de Desconto
```

Os projetos começaram com exercícios simples de cálculo e foram evoluindo para pequenos sistemas com **menus, funções, controle de fluxo, validações e manipulação de estado**.

---

## 🚀 Próximos projetos

Os próximos desafios planejados para continuar a evolução são:

1. 🔐 Sistema de Login
2. 🛒 Caixa de Supermercado
3. 📚 Sistema de Notas de Alunos
4. 🏠 Simulador de Financiamento
5. 🎯 Jogo de Adivinhação
6. ✊ Pedra, Papel e Tesoura
7. 🔑 Gerador de Senhas
8. 🚗 Sistema de Estacionamento
9. 🏦 Sistema Bancário
10. 📦 Sistema de Estoque
11. 🛍️ Sistema de Vendas

---

## 🎯 Objetivo

O objetivo deste repositório é **praticar lógica de programação com Python**, construindo projetos pequenos e aumentando gradualmente a complexidade.

Estes projetos não têm como objetivo ser sistemas profissionais, mas sim **exercícios práticos para fixação dos conteúdos**. A prioridade é entender o raciocínio por trás de cada solução, escrever o código sozinho, identificar erros e evoluir cada projeto com novas funcionalidades e validações.

### 📚 Trilha de estudos

A evolução dos estudos será dividida em duas frentes: **projetos de prática** e **curso do Gustavo Guanabara**.

- ✅ Projetos práticos para reforçar lógica e fundamentos
- 📖 Continuação dos conteúdos do **Mundo 2** do curso
- 📖 Continuação dos conteúdos do **Mundo 3** do curso
- 🚀 Aplicação dos conteúdos aprendidos em novos projetos

A ideia é aprender um novo conceito no curso e, sempre que possível, utilizá-lo em algum projeto prático deste repositório.


# 🧭 Roadmap de evolução para Back-end

Além dos projetos de prática e do curso do Gustavo Guanabara, este repositório também seguirá um **roadmap de desenvolvimento Back-end** inspirado no material de referência enviado. O roadmap inclui fundamentos de Internet, APIs, Python, Git/GitHub, bancos de dados, testes, segurança, Docker, arquitetura, observabilidade e DevOps.

A ordem abaixo é uma **adaptação pessoal de estudo**: alguns temas serão aprendidos em momentos diferentes, e assuntos avançados só serão aprofundados depois que os fundamentos estiverem sólidos.

**Referência do roadmap:** roadmap.sh — trilha de Back-end fornecida como material de estudo.

## 🥇 Fase 1 — Fundamentos de Python e lógica

**Objetivo:** construir uma base forte antes de avançar para frameworks e APIs.

- [x] Variáveis, tipos de dados e operadores
- [x] `input()` e `print()`
- [x] Condições (`if`, `elif`, `else`)
- [x] Laços (`while`, `for`)
- [x] Funções, parâmetros e `return`
- [x] Strings e formatação
- [x] Módulos e bibliotecas padrão
- [ ] Listas e dicionários com mais profundidade
- [ ] Tuplas, conjuntos e compreensão de coleções
- [ ] Tratamento de exceções (`try/except`)
- [ ] Leitura e escrita de arquivos
- [ ] Organização de projetos Python

### 📚 Curso paralelo

- [x] Fundamentos já estudados no curso do Gustavo Guanabara
- [ ] Mundo 2 — continuar e consolidar
- [ ] Mundo 3 — avançar após consolidar o Mundo 2
- [ ] Transformar exercícios do curso em pequenos projetos próprios

## 🥈 Fase 2 — Projetos de prática

**Objetivo:** transformar conhecimento teórico em código e melhorar a capacidade de resolver problemas sem copiar soluções.

### Concluídos

- [x] Calculadora
- [x] Conversor de moedas
- [x] Calculadora de média
- [x] Caixa eletrônico
- [x] Conversor de temperatura
- [x] Calculadora de área
- [x] Calculadora de desconto

### Próximos projetos

- [ ] Sistema de Login
- [ ] Caixa de Supermercado
- [ ] Sistema de Notas de Alunos
- [ ] Simulador de Financiamento
- [ ] Jogo de Adivinhação
- [ ] Pedra, Papel e Tesoura
- [ ] Gerador de Senhas
- [ ] Sistema de Estacionamento
- [ ] Sistema Bancário
- [ ] Sistema de Estoque
- [ ] Sistema de Vendas

**Regra de estudo:** primeiro construir uma versão simples e funcional; depois fazer uma segunda versão com validações, melhor organização, estruturas de dados e tratamento de erros.

## 🥉 Fase 3 — Internet e fundamentos Web

O roadmap de referência destaca o entendimento da Internet antes de aprofundar Back-end, incluindo HTTP, domínio, hospedagem, DNS e funcionamento dos navegadores.

- [ ] Como a Internet funciona
- [ ] Cliente e servidor
- [ ] HTTP e HTTPS
- [ ] Métodos HTTP: GET, POST, PUT/PATCH e DELETE
- [ ] Status codes
- [ ] Headers e body
- [ ] O que é domínio
- [ ] DNS e resolução de nomes
- [ ] Hospedagem
- [ ] Como os navegadores funcionam
- [ ] Conceitos básicos de segurança Web

## 🚀 Fase 4 — Git e GitHub

Git e serviços de hospedagem de repositórios aparecem como parte da base do roadmap.

- [ ] Git: init, add, commit, status, log
- [ ] Branches e merge
- [ ] GitHub
- [ ] Pull request
- [ ] `.gitignore`
- [ ] README e documentação
- [ ] Fluxo básico de versionamento
- [ ] GitHub como portfólio dos projetos

## 🔥 Fase 5 — Back-end com Python

**Objetivo:** sair dos programas de terminal e começar a desenvolver aplicações e APIs.

- [ ] Escolha e consolidação do Python como linguagem principal
- [ ] Estrutura de projetos Back-end
- [ ] Ambientes virtuais e gerenciamento de dependências
- [ ] Framework Back-end em Python
- [ ] Rotas e endpoints
- [ ] Request e response
- [ ] JSON
- [ ] Validação de dados
- [ ] Variáveis de ambiente
- [ ] Configuração de aplicação

O roadmap de referência coloca **APIs, Back-end e a escolha de uma linguagem**, incluindo Python, como trilhas centrais.

## 🌐 Fase 6 — APIs REST

O material inclui APIs JSON, REST, GraphQL, OpenAPI, SOAP e gRPC. Para este percurso, a prioridade será dominar **REST + JSON + OpenAPI** antes de estudar alternativas.

- [ ] Conceito de API
- [ ] REST
- [ ] APIs RESTful
- [ ] JSON
- [ ] CRUD
- [ ] Status codes
- [ ] Paginação
- [ ] Filtros e ordenação
- [ ] Validação e tratamento de erros
- [ ] OpenAPI / documentação de API
- [ ] Postman ou ferramenta equivalente para testes manuais
- [ ] Depois: conhecer GraphQL, SOAP e gRPC

## 🗄️ Fase 7 — Bancos de dados

O roadmap aborda bancos relacionais, NoSQL, ORMs, normalização, ACID, transações, índices, replicação, sharding e outras estratégias de escala.

### Primeiro dominar

- [ ] Modelagem de dados
- [ ] SQL
- [ ] Tabelas, registros e relacionamentos
- [ ] `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- [ ] `WHERE`, `ORDER BY`, `GROUP BY`
- [ ] `JOIN`
- [ ] Chaves primárias e estrangeiras
- [ ] Normalização
- [ ] Índices
- [ ] Transações e ACID
- [ ] MySQL ou PostgreSQL
- [ ] ORM com Python
- [ ] Migrations

### Depois aprofundar

- [ ] NoSQL
- [ ] MongoDB
- [ ] Redis
- [ ] Replicação
- [ ] Sharding
- [ ] Estratégias de escalabilidade
- [ ] Problema N+1
- [ ] Profiling de desempenho

## 🧪 Fase 8 — Testes e qualidade

O roadmap inclui testes unitários, de integração, funcionais, desenvolvimento orientado a testes e CI/CD.

- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Testes funcionais
- [ ] Mocks e fixtures
- [ ] Cobertura de testes
- [ ] TDD como prática de estudo
- [ ] Testar APIs
- [ ] Automatizar testes no pipeline

## 🔐 Fase 9 — Autenticação e segurança

O material inclui autenticação por senha/token/cookies, JWT, OAuth, OpenID, SAML, hashing e riscos OWASP. Para começar, a prioridade será entender autenticação, autorização, hashing seguro, JWT e boas práticas de APIs.

- [ ] Autenticação x autorização
- [ ] Hash de senhas
- [ ] bcrypt / scrypt
- [ ] JWT
- [ ] Autenticação por token
- [ ] Cookies e sessão
- [ ] OAuth
- [ ] CORS
- [ ] HTTPS / TLS
- [ ] OWASP e principais riscos Web
- [ ] Boas práticas de segurança de APIs

## 🐳 Fase 10 — Docker, servidores e deploy

Docker e conhecimentos básicos de infraestrutura aparecem no roadmap como parte da evolução para ambientes reais.

- [ ] Docker
- [ ] Dockerfile
- [ ] Imagens e containers
- [ ] Docker Compose
- [ ] Volumes e redes
- [ ] Variáveis de ambiente em containers
- [ ] Deploy de API
- [ ] Servidor Web / reverse proxy
- [ ] Nginx
- [ ] Conhecimentos básicos de Linux para Back-end
- [ ] Noções de infraestrutura

### Depois

- [ ] Kubernetes
- [ ] CI/CD
- [ ] Cloud

## 🏗️ Fase 11 — Arquitetura e boas práticas

O roadmap avançado inclui padrões de design, DDD, CQRS, Event Sourcing, monólitos, serverless, microsserviços, SOA e Twelve-Factor.

**Não estudar tudo de uma vez.** Primeiro dominar aplicações monolíticas bem estruturadas; depois avançar conforme a necessidade.

- [ ] Separação de responsabilidades
- [ ] Camadas da aplicação
- [ ] SOLID
- [ ] Design Patterns essenciais
- [ ] Aplicação monolítica bem estruturada
- [ ] DDD — fundamentos
- [ ] CQRS — conhecer o conceito
- [ ] Event-driven — fundamentos
- [ ] Twelve-Factor App
- [ ] Serverless — conhecer
- [ ] Microsserviços — estudar depois de dominar monólitos

## ⚡ Fase 12 — Mensageria, cache e tempo real

O roadmap aborda RabbitMQ, Kafka, Redis, WebSockets, Server-Sent Events, polling e sistemas em tempo real.

- [ ] Cache
- [ ] Redis
- [ ] Filas e message brokers
- [ ] RabbitMQ
- [ ] Kafka
- [ ] WebSockets
- [ ] Server-Sent Events
- [ ] Polling
- [ ] Comunicação assíncrona

## 📊 Fase 13 — Observabilidade e desempenho

O material destaca métricas, logs, instrumentação, monitoramento e telemetria como ferramentas para entender e depurar aplicações.

- [ ] Logs estruturados
- [ ] Métricas
- [ ] Monitoramento
- [ ] Telemetria
- [ ] Instrumentação
- [ ] Profiling
- [ ] Identificação de gargalos
- [ ] Tratamento de falhas
- [ ] Rate limiting
- [ ] Circuit breaker
- [ ] Backpressure
- [ ] Degradação gradual

## ☁️ Fase 14 — Escalabilidade e sistemas distribuídos

Esta é uma etapa avançada e só entra depois de uma base sólida em APIs, banco de dados, Docker e arquitetura.

- [ ] Escalonamento vertical x horizontal
- [ ] Balanceamento de carga
- [ ] Replicação
- [ ] Sharding
- [ ] Cache distribuído
- [ ] Consistência e disponibilidade
- [ ] Teorema CAP
- [ ] Estratégias de migração
- [ ] Arquitetura distribuída
- [ ] Service Mesh — conhecer

## 🧩 Projetos por etapa

Para evitar estudar teoria sem aplicação, os projetos serão usados como marcos de aprendizado:

| Projeto | Principais conhecimentos |
|---|---|
| Sistema de Login | Strings, condições, funções, validação |
| Caixa de Supermercado | Listas, dicionários, `for`, funções |
| Sistema de Estoque | CRUD, estruturas de dados, validação |
| Sistema Bancário | Regras de negócio, autenticação, histórico |
| API de Estoque | HTTP, REST, JSON, CRUD |
| API de Vendas | Banco de dados, ORM, autenticação |
| API com testes | Unitários, integração e documentação |
| API Dockerizada | Docker, variáveis de ambiente e deploy |
| Projeto final Back-end | API + banco + autenticação + testes + Docker + documentação |

## ✅ Regra de progressão

Não é necessário dominar um assunto avançado antes de começar a próxima etapa. A prioridade é:

```text
Aprender o conceito
        ↓
Fazer exercícios
        ↓
Construir um projeto pequeno
        ↓
Corrigir erros
        ↓
Refatorar
        ↓
Documentar no GitHub
        ↓
Avançar para o próximo assunto
```

## 🎯 Objetivo final

Construir uma base sólida para atuar como **Desenvolvedor Back-end com Python**, usando os projetos deste repositório como prática e o curso do Gustavo Guanabara como reforço dos fundamentos.

O foco inicial será **Python + lógica + Git/GitHub + Internet + APIs + SQL + banco de dados + framework Back-end + testes + autenticação + Docker**. Assuntos de arquitetura distribuída, microsserviços, mensageria, observabilidade e escalabilidade serão aprofundados posteriormente, conforme a base estiver consolidada.

---

## 🛠️ Tecnologias

### Já utilizadas

- Python 3
- Biblioteca padrão `os`
- Biblioteca padrão `math`

### Planejadas para a evolução

- Git e GitHub
- SQL
- MySQL / PostgreSQL
- ORM para Python
- Framework Back-end em Python
- REST / JSON / OpenAPI
- Testes automatizados
- JWT e conceitos de autenticação
- Docker
- Redis
- Mensageria (RabbitMQ / Kafka)

---

## 📌 Status

**Nível 1 — Fundamentos:** concluído ✅

**Nível 2 — Pequenos sistemas:** em andamento 🚧

**Nível 3 — Jogos e módulos:** próximo passo 📚

**Nível 4 — Projetos maiores:** futuro 🚀

**Curso de Python — Mundo 2:** em andamento 📖

**Curso de Python — Mundo 3:** próxima etapa 📚
