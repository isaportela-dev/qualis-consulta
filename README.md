⚠️ Work in Progress

Este projeto está em desenvolvimento como parte de um teste técnico para uma vaga de estágio em Back-end e Data Engineering.

O repositório está sendo atualizado gradualmente conforme o progresso da implementação, incluindo melhorias no código, organização da estrutura do projeto e documentação.

Algumas funcionalidades podem estar incompletas durante o processo de desenvolvimento.

## Qualis Consulta

API e interface web para consulta de periódicos do Qualis CAPES.

Permite buscar periódicos por:

- ISSN
- Área de avaliação
- Estrato
- Filtro combinado (área + estrato)

Os dados são carregados a partir de um arquivo Excel utilizando pandas.

A aplicação foi construída com:

- FastAPI
- Pandas
- Jinja2
- HTML + JavaScript

## Tecnologias utilizadas

- Python
- FastAPI
- Pandas
- HTML

## Estrutura do projeto

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
