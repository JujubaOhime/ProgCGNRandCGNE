import math
from random import randint
from time import sleep

def gera_x_aleatorio(n):
  vetor = []
  for i in range(n):
    vetor.append((randint(-10, 10)))
  
  return vetor

def transforma_matriz_em_csr(A):
  vAA = []
  vJA = []
  vIA = []
  n_linha = len(A)
  n_coluna = len(A[0])
  for i in range(len(A)):
    primeira_execucao = True
    if A[i][i] != 0:
      vAA.append(A[i][i])
      vJA.append(i)
      if primeira_execucao == True:
        primeiro_indicie_linha = len(vAA) - 1
        vIA.append(primeiro_indicie_linha)
        primeira_execucao = False
    for j in range(len(A[0])):
      if i != j:
        if A[i][j] != 0:
          vAA.append(A[i][j])
          vJA.append(j)
          if primeira_execucao == True:
            primeiro_indicie_linha = len(vAA) - 1
            vIA.append(primeiro_indicie_linha)
            primeira_execucao = False   

  return CSR(vAA, vJA, vIA, n_linha, n_coluna)

def norma(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + (vetor[i]) ** 2
    
    return soma ** 0.5

def norma_euclidiana(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + (vetor[i] * vetor[i])
    
    return math.sqrt(soma)

def produto_interno_mesmo_vetor(vetor):

    return norma(vetor) ** 2

def multiplica_vetor_escalar(vetor, escalar):
    res = []
    for i in range(len(vetor)):
        res.append(vetor[i] * escalar)
    
    return res

def subtrai_vetores(minuendo, subtraendo):
    res = []
    for i in range(len(minuendo)):
        res.append(minuendo[i] - subtraendo[i])
    
    return res

def soma_vetores(parcela, outra_parcela):
    res = []
    for i in range(len(parcela)):
        res.append(parcela[i] + outra_parcela[i])
    
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
            if self.via[j] <= posicao:
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

    def multiplica_matriz(self, matriz):

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

    def convergiu(self, Ax, b, iteracao, erro):
        for i in range(len(Ax)):
          if not (Ax[i] <= b[i] + erro and Ax[i] >= b[i] - erro):
            return False
        return True

    def cgnr(self, xInicial, b, erro):
        transposta = self.transposta()

        xAtual = xInicial
        xAnterior = []

        r = subtrai_vetores(b, self.multiplica(xAtual))

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
            alfa = (norma(zAnterior) ** 2) / (norma_euclidiana(w) ** 2)
            xAtual = soma_vetores(xAnterior, multiplica_vetor_escalar(p, alfa))
            r = subtrai_vetores(r, multiplica_vetor_escalar(w, alfa))

            zAtual = transposta.multiplica(r)
            beta = (norma_euclidiana(zAtual) ** 2) / (norma_euclidiana(zAnterior) ** 2)
            p = soma_vetores(zAtual, multiplica_vetor_escalar(p, beta))

            i += 1
        print("x apos " + str(i) + " iteracoes:")
        print(xAtual)
        print("\nAx:")
        print(self.multiplica(xAtual))
        print("\nb:")
        print(b)

        return xAtual

    def cgne(self, xInicial, b, erro):
        transposta = self.transposta()

        xAtual = xInicial
        xAnterior = []

        rAtual = subtrai_vetores(b, self.multiplica(xAtual))
        rAnterior = []

        p = transposta.multiplica(rAtual)
        
        alfa = 0
        beta = 0

        i = 0
        while (not(self.convergiu(self.multiplica(xAtual), b, i, erro))):
            xAnterior = xAtual
            rAnterior = rAtual

            alfa = produto_interno_mesmo_vetor(rAtual) / produto_interno_mesmo_vetor(p)
            xAtual = soma_vetores(xAtual, multiplica_vetor_escalar(p, alfa))
            rAtual = subtrai_vetores(rAtual, multiplica_vetor_escalar(self.multiplica(p), alfa))
            beta = produto_interno_mesmo_vetor(rAtual) / produto_interno_mesmo_vetor(rAnterior)
            p = soma_vetores(transposta.multiplica(rAtual), multiplica_vetor_escalar(p, beta))

            i += 1
        
        print("x apos " + str(i) + " iteracoes:")
        print(xAtual)
        print("\nAx:")
        print(self.multiplica(xAtual))
        print("\nb:")
        print(b)
        
        return xAtual

#------------------------------------------------------------------------------------------------------------

"""
TESTES
"""

erroToleravel = 0.0001

#insira o seu caso aqui, mudando o seu erro tolerável, A, b
'''
erroToleravel = 0.0001
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
N = len(A)
x0 = gera_x_aleatorio(N)
b = [9, 17, 21, 15, 20, 18, 22, 28, 26, 28]
A_csr = transforma_matriz_em_csr(A)
print(A_csr)
print("\nCom o metodo CGNR:\n")
A_csr.cgnr(x, b, erroToleravel)
print("\nCom o metodo CGNE:\n")
A_csr.cgne(x, b, erroToleravel)
print("---------------\n")
'''


print("--------")
print("Teste 1:\n")
# Exemplo da pagina 11 do pdf Matrizes_Esparsas
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
N = len(A)
x = gera_x_aleatorio(N)
b = [9, 17, 21, 15, 20, 18, 22, 28, 26, 28]

A_csr = transforma_matriz_em_csr(A)

print(A_csr)
print("\nCom o metodo CGNR:\n")
A_csr.cgnr(x, b, erroToleravel)
print("\nCom o metodo CGNE:\n")
A_csr.cgne(x, b, erroToleravel)
print("\nFim do Teste 1.")
print("---------------\n")



print("--------")
print("Teste 2:\n")

# Exemplo da pagina 4 do pdf Matrizes_Esparsas
A2 = [
    [10, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [20, 20, 21, 14, 4, 0, 0, 0, 0, 0, 0, 0],
    [90, 65, 82, 64, 10, 3, 0, 0, 0, 0, 0, 0],
    [0, 90, 101, 12, 49, 14, 7, 0, 0, 0, 0, 0],
    [0, 0, 90, 29, 46, 48, 20, 7, 0, 0, 0, 0],
    [0, 0, 0, 90, 101, 92, 83, 20, 4, 0, 0, 0],
    [0, 0, 0, 0, 90, 65, 80, 84, 15, 5, 0, 0],
    [0, 0, 0, 0, 0, 90, 92, 82, 53, 11, 2, 0],
    [0, 0, 0, 0, 0, 0, 90, 101, 79, 47, 5, 9],
    [0, 0, 0, 0, 0, 0, 0, 90, 47, 19, 28, 20],
    [0, 0, 0, 0, 0, 0, 0, 0, 90, 20, 35, 86],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 92, 30],
]
N2 = len(A2)
x2 = gera_x_aleatorio(N2)
b2 = [28, 79, 314, 273, 240, 390, 339, 330, 331, 204, 231, 212]
A_csr2 = transforma_matriz_em_csr(A2)

print(A_csr2)
print("\nCom o metodo CGNR:\n")
A_csr2.cgnr(x2, b2, erroToleravel)
print("\nCom o metodo CGNE:\n")
A_csr2.cgne(x2, b2, erroToleravel)
print("\nFim do Teste 2.")
print("---------------")

