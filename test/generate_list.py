""" Gera uma lista de nomes para teste """

import os
from faker import Faker

fake = Faker('pt_BR')  # Configurar para localização brasileira

# Definindo o caminho do arquivo de saída
OUTPUT_PATH = os.path.join('data', 'random_names.txt')

# Inicializar listas vazias para nomes masculinos e femininos
NOMES_MASC = [fake.first_name_male() + " " + fake.last_name() for _ in range(50)]
NOMES_FEM = [fake.first_name_female() + " " + fake.last_name() for _ in range(50)]

# Preparar o texto de saída
OUTPUT_TEXT = (
    "MASCULINO\n- " + 
    "\n- ".join(NOMES_MASC) + 
    "\n\nFEMININO\n- " + 
    "\n- ".join(NOMES_FEM)
)

# Salvar o texto numerado no arquivo de saída
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(OUTPUT_TEXT)

print(f"Lista de nomes aleatórios gerada e salva como {OUTPUT_PATH}.")
