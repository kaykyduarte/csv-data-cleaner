# CSV Data Cleaner

Projeto simples em Python para praticar limpeza de dados em arquivos CSV sem usar `pandas`.

## O que o projeto faz

O fluxo atual do projeto:

1. Lê um arquivo CSV bruto em `data/raw/dirty_dataset.csv`
2. Padroniza os campos `nome` e `cidade`
3. Remove linhas com valores nulos nas colunas obrigatórias
4. Remove linhas duplicadas com base em `nome`, `idade` e `cidade`
5. Exibe um relatório no terminal
6. Salva o resultado final em `data/processed/clean_dataset.csv`

## Estrutura

```text
csv_data_cleaner/
├── data/
│   ├── raw/
│   │   └── dirty_dataset.csv
│   └── processed/
│       └── clean_dataset.csv
├── src/
│   ├── main.py
│   ├── cleaner.py
│   ├── file_handler.py
│   └── report.py
└── tests/
```

## Componentes

### `main.py`

Arquivo principal que orquestra a execução do projeto:

- lê o dataset original
- chama a limpeza completa
- gera o relatório
- salva o novo arquivo processado

### `cleaner.py`

Responsável pelas regras de limpeza:

- `clean_name()`: remove espaços extras e padroniza nomes
- `clean_city()`: remove espaços extras e padroniza cidades
- `remove_nulls()`: remove linhas com campos obrigatórios vazios
- `remove_duplicates()`: remove linhas duplicadas
- `clean_all()`: executa o fluxo completo e retorna os dados limpos com métricas intermediárias

### `file_handler.py`

Responsável pela leitura e escrita de arquivos CSV:

- `read_file()`: lê o CSV e devolve uma lista de dicionários
- `save_file()`: salva os dados limpos em um novo arquivo CSV

### `report.py`

Responsável por mostrar no terminal:

- total de linhas originais
- quantidade de linhas removidas por nulos
- quantidade de duplicatas removidas
- total de linhas restantes

## Como executar

Na pasta do projeto, rode:

```bash
python src/main.py
```

## Exemplo de saída

```text
========== RELATÓRIO ==========
Linhas originais: 40
Valores nulos removidos: X
Duplicatas removidas: Y
Linhas restantes: Z
===============================
```

## Objetivo do projeto

Este projeto foi feito para praticar conceitos como:

- leitura e escrita de CSV com `csv`
- manipulação de listas e dicionários
- limpeza de dados sem bibliotecas externas
- remoção de nulos e duplicatas
- organização do código em classes
