
from Auxiliar import Auxiliar
from No import No


class Busca:
    def busca_em_largura(self, problema):
        borda = []
        Nos = No()
        Nos._init_(problema.estado_inicial, None, 0)
        borda.insert(0, Nos)
        while(True):
            Auxiliar.imprimir_matriz(self, borda[0].estado)
            if(problema.teste_objetivo(borda[0]) == True):
                print("Profundidade total:", borda[0].profundidade)
                return Auxiliar.caminhos(self, borda[0])
            filhos = Auxiliar.expande(self, borda[0], problema)
            borda.pop(0)
            for filho in range(len(filhos)):
                borda.append(filhos[filho])