# Numerar Listas de Nomes

[![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Projeto para formatar e numerar uma lista de nomes masculinos e femininos.

## Introdução

Este projeto consiste em dois scripts Python principais:

1. `formating.py`: Este script é responsável por formatar uma lista de nomes masculinos e femininos. Ele numera os nomes, converte a primeira letra de cada nome e sobrenome para maiúscula e corrige erros de espaçamento.

2. `generate_list.py`: Este script é utilizado para gerar uma lista de nomes masculinos e femininos aleatórios. Foi criado com o objetivo de fornecer dados de teste para o script `formating.py`.

## Estrutura do Projeto

   ```bash
   +--./
   |-- formating.py
   |-- README.md
   |  +--data/
   |   |-- random_names.txt
   |  +--test/
   |   |-- generate_list.py
   ```

- Raiz do Repositório
    - `formating.py`
    - `README.md`
    - Pasta `data`: Contém os arquivos `.txt` de entrada para o script `formating.py`.
    - Pasta `test`
        - `generate_list.py`

## Como Utilizar

### Instalação

Clone este repositório em sua máquina local e navegue até o diretório do projeto.

### Utilizando `formating.py`

1. Coloque o arquivo `.txt` contendo a lista de nomes na pasta `data`.
2. Execute o script `formating.py`:

    ```bash
    python formating.py
    ```

3. Verifique o arquivo `output.txt` no diretório raiz do projeto para ver a lista formatada.

### Utilizando `generate_list.py`

1. Navegue até a pasta `test`:

    ```bash
    cd test
    ```

2. Execute o script `generate_list.py`:

    ```bash
    python generate_list.py
    ```

3. Um novo arquivo `.txt` será gerado na pasta `data`, contendo uma lista de nomes aleatórios.

## Funcionalidades do `formating.py`

- Numeração da lista de nomes.
- Conversão da primeira letra de cada nome e sobrenome para maiúscula.
- Correção de erros de espaçamento antes dos nomes.

## Dependências

- Python 3.x
- Faker (para o script `generate_list.py`)

Para instalar o Faker, execute:

```bash
pip install Faker
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto, fazendo um fork e enviando um pull request.

## Autor

* Thiago da Silveira Gentil
