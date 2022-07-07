from os.path import dirname, realpath, isfile
from json import load

class ArquivoJson:
    def __init__(self): # Método construtor
        self.path = dirname(realpath(__file__))

    def lerJson(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as arquivo:
                dado = load(arquivo)
            return dado
        else:
            return False

if __name__ == '__main__':
    arquivoJson = ArquivoJson()
    dados = arquivoJson.lerJson("\Dados\dados.json")
    print(dados)