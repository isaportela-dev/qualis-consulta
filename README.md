# Qualis Consulta

Aplicação para consulta de periódicos do **Qualis CAPES** desenvolvida como parte de um teste técnico para uma vaga de estágio em **Back-end / Data Engineering**.

A aplicação permite consultar periódicos a partir de um dataset em Excel, oferecendo uma **API em FastAPI** e uma **interface web simples** para realizar buscas e filtros.

---

# Visão geral

A aplicação permite buscar periódicos utilizando diferentes critérios:

- ISSN
- Área de avaliação
- Estrato
- Filtro combinado (área + estrato)

Os dados são carregados a partir de um arquivo Excel utilizando **pandas** e processados através de uma API construída com **FastAPI**.

A interface web permite interagir com a API e visualizar os resultados em formato de tabela.

---

# Tecnologias utilizadas

- Python
- FastAPI
- Pandas
- Jinja2
- HTML
- JavaScript

---

# Estrutura do projeto

```
qualis-consulta
│
├── app
│   ├── main.py
│   ├── services.py
│   ├── data_loader.py
│   └── templates
│       └── index.html
│
├── data
│   └── qualis.xlsx
│
├── requirements.txt
└── README.md
```

---

# Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/isaportela-dev/qualis-consulta.git
cd qualis-consulta
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```
http://127.0.0.1:8000
```

---

# Endpoints da API

### Buscar periódico por ISSN

```
GET /journal/{issn}
```

Exemplo:

```
/journal/1413-6090
```

---

### Listar áreas disponíveis

```
GET /areas
```

---

### Buscar periódicos por área

```
GET /journals/by-area/{area}
```

Exemplo:

```
/journals/by-area/economia
```

---

### Buscar periódicos por estrato

```
GET /journals/by-stratum/{stratum}
```

Exemplo:

```
/journals/by-stratum/B1
```

---

### Filtro combinado

```
GET /journals/filter?area={area}&stratum={stratum}
```

Exemplo:

```
/journals/filter?area=economia&stratum=B1
```

---

# Decisões técnicas

- **FastAPI** foi utilizado para construção da API por ser leve, rápido e possuir documentação automática.
- **Pandas** foi escolhido para leitura e manipulação do dataset em Excel, permitindo filtros eficientes.
- O código foi organizado em módulos (`data_loader`, `services`, `main`) para separar responsabilidades e facilitar manutenção.
- A lógica de filtragem foi centralizada no módulo `services`, mantendo os endpoints da API mais simples.
- Foi criada uma **interface web simples em HTML e JavaScript** para permitir interação direta com a API sem necessidade de ferramentas externas.

---

# O que faria com mais tempo

Caso houvesse mais tempo para desenvolvimento, algumas melhorias que poderiam ser implementadas:

- Implementação de **paginação** para lidar com grandes volumes de resultados.
- Criação de **testes automatizados** para os serviços e endpoints da API.
- Adicionar **ordenação dinâmica** na tabela de resultados.
- Criar **visualizações de distribuição de periódicos por estrato**.
- Melhorar a interface com um framework frontend moderno.
- Permitir **upload de novos datasets**.

---

# Autor

Desenvolvido por **Isabella Portela** como parte de um teste técnico.