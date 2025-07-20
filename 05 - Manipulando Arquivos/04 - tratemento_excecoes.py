'''
EXCECÕES MAIS COMUNS

FileNotFoundError: lançada quando o arquivo não pode ser encontrado no diretório especificado.

PermissionError: quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.

IOError: quando ocorre um erro geral de E/S ( entrada / saída ) ao trabalhar com o arquivo,como problemas de permissão, falta de espaço
em disco, entre outros.

UnicoDecodeError: quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada. 
'''
from pathlib import Path

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)
except IsADirectoryError as exc:
    print(f"não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

ROOT_PATH = Path(__file__).parent

arquivo = open(ROOT_PATH / "novo-diretorio")