from json import load
from os.path import realpath, dirname, join, isfile
from ArquivoJson import ArquivoJson

class Codigo(ArquivoJson):

    def __init__(self):
        self.root = (dirname(realpath(__file__)))
        self.dados = (self.root + "\Dados\dados.json")
        self.dirDados = "\Dados\dados.json"

    def imprimirDados(self):
        print(self.dirDados)
        for i in range(0, 30):
            print(ArquivoJson().lerJson(self.dirDados)[i])

    def calcularMaiorValor(self):
        maiorValor = 0
        for i in range(0, 30):
            if(maiorValor < ArquivoJson().lerJson(self.dirDados)[i]['valor']):
                    maiorValor = ArquivoJson().lerJson(self.dirDados)[i]['valor']
        return maiorValor

    def calcularMenorValor(self):
        menorValor = self.calcularMaiorValor()
        for i in range(0, 30):
            if (menorValor > ArquivoJson().lerJson(self.dirDados)[i]['valor']):
                if(ArquivoJson().lerJson(self.dirDados)[i]['valor'] > 0):
                    menorValor = ArquivoJson().lerJson(self.dirDados)[i]['valor']
        return menorValor
    def calcularMedia(self):
        soma =0
        for i in range(0, 30):
             soma += ArquivoJson().lerJson(self.dirDados)[i]['valor']
        return soma / 30

    def calcularDia(self):
        media = self.calcularMedia()
        dias = []
        for i in range(0, 30):
            if(ArquivoJson().lerJson(self.dirDados)[i]['valor'] > media):
                dias.append(ArquivoJson().lerJson(self.dirDados)[i]['dia'])
        return dias


if __name__ == '__main__':
    cod = Codigo()
    cod.imprimirDados()
    print("Maior valor: R$"+str(cod.calcularMaiorValor()))
    print("Menor valor: R$"+str(cod.calcularMenorValor()))
    print("Média: R$"+str(cod.calcularMedia()))
    print("Dias: "+str(cod.calcularDia()))


