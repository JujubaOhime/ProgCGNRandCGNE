import math
from random import randint

def geraXAleatorio(n):
  vetor = []
  for i in range(n):
    vetor.append((randint(-10, 10)))
  return vetor

def transformaMatrizEmCNR(A):
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
        soma = soma + abs(vetor)
    
    return soma

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
    def convergiu(self, x, b, iteracao):
        if self.multiplica(x) == b:
          return True
        if iteracao + 1 > len(x):
          raise Exception("Convergencia nao conseguiu ser atingida em " + str(iteracao) + " iteracoes") 
        return False

    # TODO 
    def cgnr(self, xInicial, b):
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
        while (not(self.convergiu(xAtual, b))):
            xAnterior = xAtual
            zAnterior = zAtual

            w = self.multiplicaMatriz(p)
            alfa = (norma(zAnterior) ** 2) / (normaEuclidiana(w) ** 2)
            xAtual = somaVetores(xAnterior, multiplicaoEscalarVetor(p, alfa))
            r = subtracaoVetores(r, multiplicaoEscalarVetor(w, alfa))

            zAtual = transposta.multiplica(r)
            beta = (normaEuclidiana(zAtual) ** 2) / (normaEuclidiana(zAnterior) ** 2)
            p = zsomaVetores(zAtual, multiplicaoEscalarVetor(p, beta))

            i += 1
        
        return xAtual

    # TODO 
    def cgne(self, xInicial, b):
        transposta = self.transposta()

        x = []
        x.append(xInicial)

        r = []
        r.append(subtracaoVetores(b, self.multiplica(x[0])))

        p = []
        p.append(transposta.multiplica(r[0]))
        
        alfa = []
        beta = []

        i = 0
        while (not(self.convergiu(p[i], b))):
            novoAlfa = ( produtoInternoMesmoValor(r[i]) / produtoInternoMesmoValor(p[i]) )
            alfa.append(novoAlfa)

            novoX = x[i] + multiplicaoEscalarVetor(p[i], alfa[i])
            x.append(novoX)

            novoR = r[i] - multiplicaoEscalarVetor(self.multiplica(p[i]), alfa[i])
            r.append(novoR)

            novoBeta = (produtoInternoMesmoValor(r[i+1]) / produtoInternoMesmoValor(r[i]))

            beta.append(novoBeta)

            novoP = self.transposta().multiplica(r[i+1]) + multiplicaoEscalarVetor(p[i], beta[i])
            p.append(novoP)

            i += 1
        
        return p[i]

b = [7, 2.5, 6.002]

vaa = [10, -7, 3, 2.5, 5, 6.002]
vja = [0, 1, 2, 1, 2, 2]
via = [0, 3, 5]

n_linha = 3
n_coluna = 3
matriz = CSR(vaa, vja, via, n_linha, n_coluna)
x0 = [1, 1, 1]
a = CSR([6, 2, 4, 10], [1,2,0,2], [0, 2, 3], 3, 3)
b = CSR([1, 7, 3, 5, 9], [0,2,1,2,1], [0, 2, 4], 3, 3)
"""
print(matriz)
print(matriz.transposta())
print(a.soma(b))
print(a.subtracao(b))
print(b.subtracao(a))
print(a.multiplicaMatriz(b))
"""
"""
print((transformaMatrizEmCNR([
  [11, 12, 0, 0, 0, 0, 0],
  [21, 22, 0, 0, 25, 0, 0],
  [31, 32, 33, 34, 0, 0, 37],
  [0, 0, 0, 44, 45, 0, 0],
  [0, 0, 0, 54, 55, 56, 0],
  [0, 0, 0, 64, 0, 66, 67],
  [0, 0, 0, 74, 0, 76, 77],

])))
"""

#Exemplo da pagina 11 do pdf Matrizes_Esparsas
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
X = geraXAleatorio(10)
b = [9, 17, 21, 15, 20, 18, 22, 28, 26, 28]


ACNR = transformaMatrizEmCNR(A)
print(ACNR[0])
print(ACNR[1])
print(ACNR[2])
print(ACNR[3])
print(ACNR[4])


vetor = [3, 0, 1]
csr = CSR(ACNR[0], ACNR[1], ACNR[2], ACNR[3], ACNR[4])
print(csr)

# RESULTADO ESQUISITO: formato [<numero>, 0, 0, 0, ..., 0]
print(matriz.multiplica(vetor))

csr.cgnr(X, b)