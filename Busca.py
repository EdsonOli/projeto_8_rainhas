from Auxiliar import Auxiliar
from No import No

class Busca:
    def busca_em_largura(self, problema, no):
        borda = []
        Nos = No()
        Nos._init_(problema.estado_iniicial, None, 0, 0)
        borda.insert(0, Nos)
        while(True):
            Auxiliar.imprimirMatriz(self, borda[0].estado)
            if(problema.teste_obsetivo(borda[0])):
                print("Profundidade total:", borda[0].profundidade)
                return Auxiliar.caminhos(self,  borda[0])
            filhos = Auxiliar.expande(self, borda[0], problema)
            borda.pop(0)
            for filho in range(filhos):
                borda.append(filhos[filho])