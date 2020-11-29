def multiplica(vaa, vja, via, outroVetor):
    pass

def acha_linha_coluna_de_elemento(posicao,vaa, vja, via):
    final = []
    linha = 0
    coluna = 0
    for j in range(len(via) -1, -1, -1):

        if via[j]<=posicao:
            linha = j
            break

    coluna = vja[posicao]
    final.append(linha)
    final.append(coluna)
    return final

def transposta(vaa, vja, via, n_linha, n_coluna):
    new_vaa = []
    new_vja = []
    new_via = []
    posicoes = []
    for i in range(len(vaa)):
        posicoes.append(acha_linha_coluna_de_elemento(i,vaa, vja, via)) 

    print(posicoes)
    somatorio = 0
    for i in range(n_linha):
        menor = 0
        for j in range(n_coluna):
            if [j, i] in posicoes:
                print(posicoes.index([j, i]))
                print(vaa[posicoes.index([j, i])])
                new_vaa.append(vaa[posicoes.index([j, i])])
                new_vja.append(j)
                if (menor == 0):
                    new_via.append(somatorio)
                somatorio = somatorio + 1
                menor = menor + 1
    
    res = []
    res.append(new_vaa)
    res.append(new_vja)
    res.append(new_via)
    return(res)

    

b = [7, 2.5, 6.002]

vaa = [10, -7, 2.5, 5, 6.002]
vja = [0, 1, 1, 2, 2]
via = [0, 2, 4]
n_linha = 3
n_coluna = 3
x0 = ['x1', 'x2', 'x3']

print(transposta(vaa, vja, via, n_linha, n_coluna))


