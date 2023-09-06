""" Numera uma lista de nomes masculinos e femininos."""
import os
import sys

# Adicionando encoding para evitar erros de caracteres
sys.stdout.reconfigure(encoding='utf-8')

# Definindo o caminho do arquivo de entrada e de saída
INPUT_FOLDER = 'data'
OUTPUT_PATH = 'output.txt'

try:
    # Encontrar o primeiro arquivo .txt na pasta de entrada
    input_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.txt')]
    if not input_files:
        raise FileNotFoundError("Nenhum arquivo .txt encontrado na pasta de entrada.")

    INPUT_PATH = os.path.join(INPUT_FOLDER, input_files[0])

    # Ler o arquivo de entrada
    with open(INPUT_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Inicializar listas vazias para nomes masculinos e femininos
    NOMES_MASC = []
    NOMES_FEM = []

    # Flag para determinar qual lista preencher
    MASC = False

    # Preencher as listas
    # Preencher as listas
    for line in lines:
        line = line.strip()
        if line == "MASCULINO":
            MASC = True
        elif line == "FEMININO":
            MASC = False
        elif '-' in line:  # Verifique se há um hífen na linha
            name = line[line.index('-')+1:].strip()  # remove espaçamento depois do hifén
            name = name.title()  # Converte a primeira letra de cada palavra para maiúscula
            if MASC:
                NOMES_MASC.append(name)
            else:
                NOMES_FEM.append(name)

    # Numerar as listas
    NOMES_MASC_NUMERADOS = [f"{str(i+1).zfill(2)}. {name}" for i, name in enumerate(NOMES_MASC)]
    NOMES_FEM_NUMERADOS = [f"{str(i+1).zfill(2)}. {name}" for i, name in enumerate(NOMES_FEM)]


    # Preparar o texto de saída
    OUTPUT_TEXT = (
        "MASCULINO\n" + 
        "\n".join(NOMES_MASC_NUMERADOS) + 
        "\n\nFEMININO\n" + 
        "\n".join(NOMES_FEM_NUMERADOS)
    )

    # Salvar o texto numerado no arquivo de saída
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(OUTPUT_TEXT)

    print("Tarefa finalizada com sucesso! O arquivo de saída foi salvo como 'output.txt'.")

# pylint: disable= W0718
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
