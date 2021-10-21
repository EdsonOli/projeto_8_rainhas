import copy
from Auxiliar import Auxiliar

class Rainhas:
    estado_inicial = []
    indice = 8
    for i in range(indice):
        linha = []
        for j in range(indice):
            linha.append("X")
        estado_inicial.append(linha)
    
    def teste_objetivo(self, no):
        matriz = no.estado
        cont = 0
        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if (matriz[linha][coluna] == "Q"):
                    cont += 1
        if(cont == len(matriz)):
            return True
        return False

    def acao(self, no):
        vetor = []
        matriz = no.estado
        linha = no.profundidade
        for coluna in range(len(matriz)):
            matriz[linha][coluna] = "Q"
            conflitos = Auxiliar.detecta_ameacas(self, matriz, linha, coluna)
            if(conflitos == 0):
                auxiliar = copy.deepcopy(matriz)
                vetor.append(auxiliar)
            matriz[linha][coluna] = "X"
        return vetor
