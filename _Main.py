
from Busca import Busca
from Problema import Problema
from Rainhas import Rainhas

class Main:

    def executar(self):
        busca = Busca()
        rainhas = Rainhas()
        problema = Problema()
        problema._init_(rainhas.estado_inicial ,rainhas.acao, rainhas.teste_objetivo, 1)
        busca.busca_em_largura(problema)
    
Exe = Main()
A = Exe.executar()
    