# Exercício 1 — Catálogo de Cursos

Este diretório contém a resolução completa do **Exercício 1** da lista de exercícios práticos de Web Scraping.

---

## 📁 Estrutura de Arquivos

```text
WS.9-10-26/
└── exercicio_1/
    ├── index.html     # Página HTML da escola fictícia com catálogo de cursos
    ├── scraper.py     # Script Python de web scraping com BeautifulSoup
    ├── raspagem.py    # Espelho idêntico do script de raspagem
    └── README.md      # Instruções de execução e documentação
```

---

## 📋 Requisitos Atendidos

### Parte A — Montagem do HTML (`index.html`)
- Escola fictícia: **TechNova Academy**
- Pelo menos 4 cursos (contém 4 formações completas):
  1. *Desenvolvimento Web Full Stack*
  2. *Ciência de Dados e Inteligência Artificial*
  3. *Cibersegurança e Testes de Intrusão (Pentest)*
  4. *Design de Interface e Experiência do Usuário (UI/UX)*
- Cada curso possui:
  - **Nome** (em tag `<h2>` com classe `curso-nome`)
  - **Área** (com classe `curso-area`)
  - **Carga horária** (com classe `curso-carga`)
  - Lista `<ul>` com **três assuntos estudados** (com classe `curso-assuntos`)
- Design moderno, responsivo e estilizado com visual escuro (dark theme) e efeitos suaves.

### Parte B — Script Python de Raspagem (`scraper.py`)
- Conecta ao servidor HTTP local (`127.0.0.1:8000`)
- Detecta automaticamente se o servidor foi iniciado na raiz do workspace ou dentro de `exercicio_1`
- Extrai todos os cursos
- Extrai o nome, a área e a carga horária de cada curso
- Percorre a lista de 3 assuntos de cada curso e exibe os itens de forma estruturada e organizada no terminal.

---

## 🚀 Como Executar

### 1. Iniciar o servidor HTTP local
Abra um terminal na raiz do projeto (`WS.9-10-26`) ou dentro da pasta `exercicio_1` e execute:

```bash
python -m http.server --bind 127.0.0.1 8000
```

*(Mantenha esse terminal aberto rodando o servidor)*

### 2. Executar o script de raspagem
Em um **segundo terminal**, execute:

```bash
python exercicio_1/scraper.py
```
*(ou se já estiver dentro da pasta `exercicio_1`: `python scraper.py`)*
