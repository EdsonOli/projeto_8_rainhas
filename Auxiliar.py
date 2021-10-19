from No import No

class Auxiliar:
    def detecta_ameacas(self, matriz, linha, coluna):
        contador = 0
        for linAux in range(len(matriz)):
            if(matriz[linAux][coluna] == matriz[linha][coluna]):
                contador += 1
            for c in range(len(matriz)):
                if(matriz[linAux][c] == matriz[linha][coluna]):
                    contador += 1

        colAux = coluna
        for linAux in range(linha, len(matriz), 1):
            if(matriz[linAux][colAux] == matriz[linha][coluna]):
                contador += 1
            colAux += 1
        
        colAux = coluna
        for linAux in range(linha, -1, -1):
            if(colAux != -1):
                if(matriz[linAux][colAux] == matriz[linha][coluna]):
                    contador += 1
                colAux -= 1
        
        colAux = coluna
        for linAux in range(linha, len(matriz), 1):
            if(colAux != -1):
                if(matriz[linAux][colAux] == matriz[linha][coluna]):
                    contador += 1
                colAux -= 1
        
        colAux = coluna
        for linAux in range(linha, -1, -1):
            if(colAux != len(matriz)):
                if(matriz[linAux][colAux] == matriz[linha][coluna]):
                    contador += 1
                c += 1
        return (contador - 6)

    def caminhos(self, no):
        caminho = []
        while(no != None):
            caminho.append(no)
            no = no.pai
        return caminho

    def expande(self, no, problema):
        filhos = []
        possibilidades = problema.acoes(no)
        if (possibilidades != []):
            for no in range(len(possibilidades)):
                no_filho = No()
                no_filho._init_(possibilidades[no].estado, no, no.custo, no.profundidade + 1)
                filhos.append(no_filho)
        return filhos

    def imprimir_matriz(self, matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                print(matriz[i][j], end="")
            print()
        print("\n")