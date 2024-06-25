# Boas práticas em Python

* o padrão de nomes das variáveis e constantes devem ser snake case
* Escolher nomes sugestivos 
* Nome das constantes devem ser maiúsculas

## Exemplo
ao ínves de escrever "aumentoSalario" ( cammel case) em python o recomendado é escrever "aumento_salario".

não encurtar nomes de variáveis ( algo que fiz bastante no passado) sempre ser o mais explicíto possível!
exemplo, uma varável para armazenar o valor da data de aniversário:
 "data_nasc", "nasci_d", "dt" não são bons nomes o correto é "data_aniversario"!
 essa abordagem ajuda na legibilidade do código, especialmente se for necessário revisita-lo depois de muito tempo.

para indicar ( ao programador) que o valor da variável não deve ser alterado, exemplo, o caminho de um arquivo,
utilizamos nomes com letras maiúsculas.
o caminho de um arquivo ( não deve ser alterado ao decorrer do programa).

CAMINHO_ARQUIVO = '/home/downloads/arquivo.txt" 