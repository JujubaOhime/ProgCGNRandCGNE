class CSR:
    def __init__(self, vaa, vja, via, linhas, colunas):
        self.vaa = vaa
        self.vja = vja
        self.via = via
        self.linhas = linhas
        self.colunas = colunas

    def __str__(self):
        return '{{\n\tvaa: {0}\n\tvja: {1}\n\tvia: {2}\n\tlinhas: {3}\n\tcolunas: {4}\n}}'.format(self.vaa, self.vja, self.via, self.linhas, self.colunas)
    
    def multiplica(self, outroVetor):
        if isinstance(outroVetor, list) and self.colunas == len(outroVetor):
            resultado = [0] * self.linhas
            linha = 0

            for i in range(len(self.vaa)):
                if i == self.via[linha] and i != 0:
                    linha += 1
                resultado[linha] += self.vaa[i] * outroVetor[self.vja[i]]
            
            return resultado

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
            print("Multiplicação incompatível")
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

    # TODO
    def convergiu(self, elem):
        return True

    # TODO 
    def norma(self):
        return 0

    # TODO
    def normaEuclidiana(self):
        return 0

    # TODO 
    def cgnr(self, b):
        transposta = self.transposta()

        r = []
        z = []
        p = []
        w = []
        x = []

        alfa = []
        beta = []

        i = 0
        while (not(convergiu(p[i])) and (i <= len(self))):
            w[i] = self.multiplicaMatriz(p[i])
            alfa[i] = (z[i].norma() ** 2) / (w[i].normaEuclidiana() ** 2)
            x[i + 1] = x[i] + p[i].multiplica(alfa[i])
            r[i + 1] = r[i] + w[i].multiplica(alfa[i])
            z[i + 1] = transposta.multiplicaMatriz(r[i + 1])
            beta[i] = (z[i + 1].normaEuclidiana() ** 2) / (z[i].normaEuclidiana() ** 2)
            p[i + 1] = z[i + 1].soma(p[i].multiplica(beta[i]))

            i += 1

        if (i > len(self) and not(convergiu(p[i]))):
            raise Exception('A matriz não convergiu!')
        
        return p[i]

    # TODO 
    def cgne(self, b):
        return 0


b = [7, 2.5, 6.002]

vaa = [10, -7, 3, 2.5, 5, 6.002]
vja = [0, 1, 2, 1, 2, 2]
via = [0, 3, 5]

n_linha = 3
n_coluna = 3
matriz = CSR(vaa, vja, via, n_linha, n_coluna)
x0 = ['x1', 'x2', 'x3']
a = CSR([6, 2, 4, 10], [1,2,0,2], [0, 2, 3], 3, 3)
b = CSR([1, 7, 3, 5, 9], [0,2,1,2,1], [0, 2, 4], 3, 3)

#print(matriz)
#print(matriz.transposta())
print(a.soma(b))
print(a.subtracao(b))
print(b.subtracao(a))
print(a.multiplicaMatriz(b))


