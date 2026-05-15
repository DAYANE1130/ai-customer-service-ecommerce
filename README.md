
# 🤖 AI Customer Support Automation for Ecommerce

Sistema de automação de atendimento ao cliente para ecommerce utilizando IA generativa com Langflow + Gemini integrado a uma aplicação Flask.

O projeto foi desenvolvido como um MVP funcional focado em automação de processos, redução de tempo operacional e melhoria da experiência do cliente.

<p align="center">
  <img src="./static/fluxo_langflow.png" alt="fluxo visual langflow" width="700"/>
</p>

---

# 📌 Objetivo do Projeto

Construir um sistema capaz de automatizar partes do atendimento ao cliente em ecommerce através de IA, permitindo:

- Responder dúvidas frequentes automaticamente
- Recomendar produtos
- Consultar informações de pedidos
- Enviar emails automáticos ao cliente
- Identificar intenções do usuário
- Executar ações no backend com base na resposta da IA

---

# 🚀 Tecnologias Utilizadas

- Python
- Flask
- Langflow
- Gemini
- SMTP / Gmail
- HTML
- TailwindCSS
- Jinja2

---

# 🧠 Arquitetura da Solução

A aplicação foi organizada seguindo princípios de:

- Separação de responsabilidades
- Clareza de fluxo
- Manutenção simplificada
- Escalabilidade futura

---

# 📁 Estrutura do Projeto

```bash
project/
│
├── controllers/
│   └── processamento do fluxo e regras da aplicação
│
├── services/
│   └── integrações externas e lógica de negócio
│
├── database/
│   └── dados simulados de usuários e pedidos
│
├── templates/
│   └── renderização HTML com Jinja
│
├── static/
│   └── arquivos estáticos da interface
│
├── utils/
│   └── funções auxiliares
│
└── app.py
```

---

# 🔄 Fluxo da Aplicação

```text
Usuário
   ↓
Flask (Backend)
   ↓
Langflow + Gemini
   ↓
Resposta estruturada da IA
   ↓
Backend interpreta intenção
   ↓
Execução de ação automática
   ↓
Envio de email / recomendação / resposta
```

---

# ⚙️ Funcionalidades Implementadas

## ✅ Atendimento Automatizado

O sistema utiliza IA para responder dúvidas frequentes relacionadas a:

- Status de pedidos
- Informações de entrega
- Políticas da loja
- Recomendações de produtos

---

## ✅ Recomendação de Produtos

Com base na intenção identificada pelo modelo, o sistema consegue sugerir produtos automaticamente.

---

## ✅ Envio Automático de Emails

A aplicação integra SMTP/Gmail para envio automático de emails contendo:

- Atualização de pedidos
- Informações solicitadas pelo cliente
- Recomendações

---

## ✅ Respostas Estruturadas da IA

O sistema utiliza respostas estruturadas para:

- Identificar intenção do usuário
- Definir ações automaticamente
- Garantir previsibilidade no fluxo
- Conectar IA com execução operacional

---

# 🧩 Integração IA + Backend

A arquitetura foi desenhada para separar claramente:

## IA Responsável Por

- Interpretar mensagens
- Identificar intenções
- Estruturar respostas
- Direcionar o fluxo da aplicação

---

## Backend Responsável Por

- Regras de negócio
- Execução de ações
- Consulta de dados
- Envio de emails
- Renderização da interface

---

# 🛠️ Decisões Técnicas do MVP

## Flask

Escolhido pela simplicidade, velocidade de desenvolvimento e facilidade de integração com serviços externos.

---

## Langflow

Utilizado para organizar visualmente o fluxo da IA e acelerar prototipação e testes.

---

## Respostas Estruturadas

A decisão de utilizar respostas estruturadas foi essencial para transformar respostas da IA em ações reais do backend.

Isso tornou o sistema mais previsível, automatizável e escalável.

---

## Organização em Camadas

A divisão entre:

- controllers
- services
- database
- utils

foi adotada para melhorar:

- organização
- legibilidade
- manutenção
- reutilização de código

---

# 📈 Problemas que o Projeto Resolve

## ⏱️ Redução de Tempo Operacional

Automatiza tarefas repetitivas do atendimento ao cliente.

---

## 💰 Redução de Custos

Diminui a necessidade de intervenção manual em processos simples e recorrentes.

---

## 📦 Escalabilidade no Atendimento

Permite atender múltiplos usuários simultaneamente.

---

## ⭐ Melhor Experiência do Cliente

Entrega respostas rápidas, automatizadas e contextualizadas.

---

# 🔮 Possíveis Evoluções Futuras

- Integração com banco de dados real
- Histórico de conversas
- Dashboard administrativo
- Integração com APIs de ecommerce
- Deploy em cloud
- Observabilidade e monitoramento
- Autenticação de usuários
- Integração com WhatsApp

---

# ▶️ Como Executar o Projeto

## Clone o repositório

```bash
git clone <repo_url>
```

---

## Crie o ambiente virtual

```bash
python -m venv venv
```

---

## Ative o ambiente virtual

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Execute a aplicação

```bash
python app.py
```

---

# 💡 Aprendizados do Projeto

Durante o desenvolvimento deste MVP, os principais aprendizados foram:

- Integração entre IA e backend
- Uso de respostas estruturadas
- Organização arquitetural em aplicações Flask
- Automação de processos com IA
- Construção de fluxos com Langflow
- Separação entre decisão e execução

---

# 📬 Contato

Caso queira trocar ideias sobre:

- IA
- Backend
- Automação
- Arquitetura de software

Fique à vontade para se conectar 🚀

