def principal():
    print('executando função principal')

    def funcao_interna():
        print('executando função interna')
    
    def funcao_2():
        print('executando segunda função interna')
    
    funcao_interna()
    funcao_2()

principal()