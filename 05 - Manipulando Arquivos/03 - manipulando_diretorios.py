import os
import shutil
from pathlib import Path

# descobrindo a pasta raiz onde o arquivo está
ROOT_PATH = Path(__file__).parent 
print(ROOT_PATH)

#os.mkdir(ROOT_PATH / "nova-pasta")

# criando arquivo dentro da pasta
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# renomeando
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "nome_alterado.txt")
os.remove(ROOT_PATH / "nome_alterado.txt") # removendo ( necessário comentar outra linha para funcionar)