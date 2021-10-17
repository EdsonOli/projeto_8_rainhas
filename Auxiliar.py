class Auxiliar:
    def detecta_ameacas(self, matriz, linha, coluna):
        contador = 0
        for linAux in range(len(matriz)):
            if(matriz[linAux][coluna] == matriz[linha][[coluna]]):
                contador += 1
            for c in range(len(matriz)):
                if(matriz[linha][c] == matriz[linha][coluna]):
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