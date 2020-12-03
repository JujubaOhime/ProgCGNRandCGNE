import math
from random import randint

def geraXAleatorio(n):
  vetor = []
  for i in range(n):
    vetor.append((randint(-10, 10)))
  return vetor

def transformaMatrizEmCSR(A):
  # INDICIES COMECAM EM 0!
  vAA = []
  vJA = []
  vIA = []
  n_linha = len(A)
  n_coluna = len(A[0])
  for i in range(len(A)):
    first = True
    if A[i][i] != 0:
      vAA.append(A[i][i])
      vJA.append(i)
      if first == True:
        firstIndexRow = len(vAA) - 1
        vIA.append(firstIndexRow)
        first = False
    for j in range(len(A[0])):
      if i != j:
        if A[i][j] != 0:
          vAA.append(A[i][j])
          vJA.append(j)
          if first == True:
            firstIndexRow = len(vAA) - 1
            vIA.append(firstIndexRow)
            first = False        

  return vAA, vJA, vIA, n_linha, n_coluna

def norma(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + (vetor[i]) ** 2
    
    return soma ** 0.5

def normaEuclidiana(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + (vetor[i] * vetor[i])
    
    return math.sqrt(soma)

def produtoInternoMesmoValor(vetor):
    res = norma(vetor) * norma(vetor)

    return res

def multiplicaoEscalarVetor(vetor, escalar):
    res = []
    for i in range(len(vetor)):
        res.append(vetor[i]*escalar)
    
    return res

def subtracaoVetores(minuendo, subtraendo):
    res = []
    for i in range(len(minuendo)):
        res.append(minuendo[i] - subtraendo[i])
    
    return res

def somaVetores(parcela, outraParcela):
    res = []
    for i in range(len(parcela)):
        res.append(parcela[i] + outraParcela[i])
    
    return res

    


class CSR:
    def __init__(self, vaa, vja, via, linhas, colunas):
        self.vaa = vaa
        self.vja = vja
        self.via = via
        self.linhas = linhas
        self.colunas = colunas

    def __str__(self):
        return '{{\n\tvaa: {0}\n\tvja: {1}\n\tvia: {2}\n\tlinhas: {3}\n\tcolunas: {4}\n}}'.format(self.vaa, self.vja, self.via, self.linhas, self.colunas)

    def acha_linha_coluna_de_elemento(self, posicao):
        final = []
        linha = 0
        coluna = 0
        for j in range(len(self.via) -1, -1, -1):
            if self.via[j]<=posicao:
                linha = j
                break
        

        coluna = self.vja[posicao]
        final.append(linha)
        final.append(coluna)
        return final

    def transposta(self):
        new_vaa = []
        new_vja = []
        new_via = []
        posicoes = []

        for i in range(len(self.vaa)):
            posicoes.append(self.acha_linha_coluna_de_elemento(i)) 

        somatorio = 0
        for i in range(self.linhas):
            menor = 0
            for j in range(self.colunas):

                if [j, i] in posicoes:
                    new_vaa.append(self.vaa[posicoes.index([j, i])])
                    new_vja.append(j)
                    if (menor == 0):
                        new_via.append(somatorio)
                    somatorio = somatorio + 1
                    menor = menor + 1

        resposta = CSR(new_vaa, new_vja, new_via, self.linhas, self.colunas)
        return(resposta)

    def soma(self, matriz):
        new_vaa = []
        new_vja = []
        new_via = []
        posicoes = []
        posicoes2 = []

        for i in range(len(self.vaa)):
            posicoes.append(self.acha_linha_coluna_de_elemento(i))
        
        for i in range(len(matriz.vaa)):
            posicoes2.append(matriz.acha_linha_coluna_de_elemento(i))

        somatorio = 0
        for i in range(self.linhas):
            menor = 0
            for j in range(self.colunas):

                if ([i, j] in posicoes) or ([i,j] in posicoes2):
                    soma = 0

                    if([i,j] in posicoes):
                        soma = soma + self.vaa[posicoes.index([i, j])]

                    if([i,j] in posicoes2):
                        soma = soma + matriz.vaa[posicoes2.index([i, j])]
                    
                    new_vaa.append(soma)
                    new_vja.append(j)
                    if (menor == 0):
                        new_via.append(somatorio)
                    somatorio = somatorio + 1
                    menor = menor + 1
        
        res = CSR(new_vaa, new_vja, new_via, self.linhas, self.colunas)
        return(res)

    def subtracao(self, matriz):
        new_vaa = []
        new_vja = []
        new_via = []
        posicoes = []
        posicoes2 = []

        for i in range(len(self.vaa)):
            posicoes.append(self.acha_linha_coluna_de_elemento(i))
        
        for i in range(len(matriz.vaa)):
            posicoes2.append(matriz.acha_linha_coluna_de_elemento(i))

        somatorio = 0
        for i in range(self.linhas):
            menor = 0
            for j in range(self.colunas):

                if ([i, j] in posicoes) or ([i,j] in posicoes2):
                    soma = 0

                    if([i,j] in posicoes):
                        soma = soma + self.vaa[posicoes.index([i, j])]

                    if([i,j] in posicoes2):
                        soma = soma - matriz.vaa[posicoes2.index([i, j])]
                    
                    new_vaa.append(soma)
                    new_vja.append(j)
                    if (menor == 0):
                        new_via.append(somatorio)
                    somatorio = somatorio + 1
                    menor = menor + 1
        
        res = CSR(new_vaa, new_vja, new_via, self.linhas, self.colunas)
        return(res)

    def multiplicaMatriz(self, matriz):

        if(self.colunas != matriz.linhas):
            print("Multiplicacao incompativel")
            exit(0)
        
        new_vaa = []
        new_vja = []
        new_via = []
        posicoes = []
        posicoes2 = []

        for i in range(len(self.vaa)):
            posicoes.append(self.acha_linha_coluna_de_elemento(i))
        
        for i in range(len(matriz.vaa)):
            posicoes2.append(matriz.acha_linha_coluna_de_elemento(i))

        somatorio = 0
        for i in range(self.linhas):
            menor = 0
            for j in range(matriz.colunas):
                soma = 0
                for k in range(self.colunas):
                    
                    if ([i,k] in posicoes) and ([k,j] in posicoes2):
                        soma = soma + (matriz.vaa[posicoes2.index([k, j])] * self.vaa[posicoes.index([i, k])]) 

                if (soma != 0):
                    new_vaa.append(soma)
                    new_vja.append(j)
                    if (menor == 0):
                        new_via.append(somatorio)
                    somatorio = somatorio + 1
                    menor = menor + 1

        res = CSR(new_vaa, new_vja, new_via, self.linhas, matriz.colunas)
        return(res)   


    def multiplica(self, vetor):

        if(self.colunas != len(vetor)):
            print("Multiplicacao incompativel")
            exit(0)
        
        res = []
        posicoes = []

        for i in range(len(self.vaa)):
            posicoes.append(self.acha_linha_coluna_de_elemento(i))


        for i in range(self.linhas):
            for j in range(1):
                soma = 0
                for k in range(self.colunas):
                    if ([i,k] in posicoes):
                        soma = soma + (vetor[k] * self.vaa[posicoes.index([i, k])]) 
                res.append(soma)

        return(res)   

    



    # TODO
    def convergiu(self, Ax, b, iteracao, erro):
        for i in range(len(Ax)):
          if not (Ax[i] <= b[i] + erro and Ax[i] >= b[i] - erro):
            return False
        #if iteracao + 1 > len(Ax):
        #  raise Exception("Convergencia nao conseguiu ser atingida em " + str(iteracao) + " iteracoes") 
        print("Ax: ", Ax)
        print("b: ", b)
        print("Feito em {} iterações".format(iteracao))
        return True

    # TODO 
    def cgnr(self, xInicial, b, erro):
        transposta = self.transposta()

        xAtual = xInicial
        xAnterior = []

        r = subtracaoVetores(b, self.multiplica(xAtual))

        zAtual = transposta.multiplica(r)
        zAnterior = []

        p = zAtual

        w = []

        alfa = 0
        beta = 0

        i = 0
        while (not(self.convergiu(self.multiplica(xAtual), b, i, erro))):
            xAnterior = xAtual
            zAnterior = zAtual

            w = self.multiplica(p)
            alfa = (norma(zAnterior) ** 2) / (normaEuclidiana(w) ** 2)
            xAtual = somaVetores(xAnterior, multiplicaoEscalarVetor(p, alfa))
            r = subtracaoVetores(r, multiplicaoEscalarVetor(w, alfa))

            zAtual = transposta.multiplica(r)
            beta = (normaEuclidiana(zAtual) ** 2) / (normaEuclidiana(zAnterior) ** 2)
            p = somaVetores(zAtual, multiplicaoEscalarVetor(p, beta))

            i += 1
        print("X = ", xAtual)
        return xAtual

    # TODO 
    def cgne(self, xInicial, b, erro):
        transposta = self.transposta()

        xAtual = xInicial
        xAnterior = []

        rAtual = subtracaoVetores(b, self.multiplica(xAtual))
        rAnterior = []

        p = transposta.multiplica(rAtual)
        
        alfa = 0
        beta = 0

        i = 0
        while (not(self.convergiu(self.multiplica(xAtual), b, i, erro))):
            xAnterior = xAtual
            rAnterior = rAtual

            alfa = produtoInternoMesmoValor(rAtual) / produtoInternoMesmoValor(p)
            xAtual = somaVetores(xAtual, multiplicaoEscalarVetor(p, alfa))
            rAtual = subtracaoVetores(rAtual, multiplicaoEscalarVetor(self.multiplica(p), alfa))
            beta = produtoInternoMesmoValor(rAtual) / produtoInternoMesmoValor(rAnterior)
            p = somaVetores(transposta.multiplica(rAtual), multiplicaoEscalarVetor(p, beta))

            i += 1
        
        print("X = ", xAtual)
        return xAtual

#Exemplo da pagina 11 do pdf Matrizes_Esparsas
X = geraXAleatorio(10)
A = [
  [10, -1, 0, 0, 0, 0, 0, 0, 0, 0],
  [4, 11, 0, 0, 1, 0, 0, 1, 0, 0],
  [1, 2, 12, 2, 0, 0, 3, 0, 0, 1],
  [0, 0, 0, 13, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 3, 14, 2, 0, -1, 2, 0],
  [0, 0, 0, 1, 0, 15, 2, 0, -2, 2],
  [0, 0, 0, 1, 0, 2, 16, 0, 2, 1],
  [0, 0, 0, 3, 2, 2, 0, 17, 2, 0],
  [0, 0, 0, 1, 0, 3, 2, 0, 18, 2],
  [0, 0, 0, 1, 0, 2, 4, 0, 2, 19],
]
b = [9, 17, 21, 15, 20, 18, 22, 28, 26, 28]
erroTolerável = 0.0000001

ACSR = transformaMatrizEmCSR(A)
csr = CSR(ACSR[0], ACSR[1], ACSR[2], ACSR[3], ACSR[4])

# se preferir set os valores dentro de CSR nesta ordem:
# vAA, vJA, vIA, n_de_linhas_matriz, n_de_colunas_matriz 

print(csr)
print("\n")
print("Com o método CGNR: \n")
csr.cgnr(X, b, erroTolerável)
print("\n")
print("Com o método CGNE: \n")
csr.cgne(X, b, erroTolerável)
