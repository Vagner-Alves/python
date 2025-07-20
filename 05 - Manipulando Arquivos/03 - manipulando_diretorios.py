import os
import shutil
from pathlib import Path

# descobrindo a pasta raiz onde o arquivo está
ROOT_PATH = Path(__file__).parent 
print(ROOT_PATH)

os.mkdir(ROOT_PATH / "nova-pasta")
