

class CaixaGeral:

    # cria fichas

    def __init__(self):
        self.fichas = 1000

    def vender_fixas(self, quantia):
        if quantia <= self.fichas:
            self.fichas -= quantia
        else:
            print('Quantia indisponivel, peça um numero até {}'.format(self.fichas))

    #retorna fichas
    def retornar_fixas(self, quantia):
        self.fichas += quantia


class CaixaBarraca:

    # cria Barraca
    def __init__(self, nome):
        self.nome = nome
        self.fichas = 0

    def vende_produto(self, quantiaFichas):
        self.fichas += quantiaFichas
        print(f"Obrigado, ocê comprou {str(quantiaFichas)} {self.nome}(s), aproveite")
        return quantiaFichas

    def retornar_ficha(self, ):
        retorno = self.fichas
        self.fichas = 0
        return retorno

    def __str__(self):
        return self.nome


def main():
    caixa = CaixaGeral()

    # Cria a lista de  'objetos' barracas
    barracas = [CaixaBarraca("Milho"), CaixaBarraca("Sonho"), CaixaBarraca("Churrasquin"), CaixaBarraca("Morango"), CaixaBarraca("Pipoca"), CaixaBarraca("Paçoca"), CaixaBarraca("Pamonha"), CaixaBarraca("Quentão"), CaixaBarraca("Pinhão"), CaixaBarraca("Canjica"), CaixaBarraca("Pé de Moleque")]
    fichasRetorno = 0
    while True:
        print("Bien vindo a festa junina, oque cê que faze?")
        resp = input("1 - Comprar fichas \n 2 - Comprar Comida \n 3 - Ver fichas restantes \n 4 - Retornar ficha \n 0 - Sair da festa \n")
        if resp == '1':
            quantiaPedida = int(input('Quantas fichas cê que?'))
            caixa.vender_fixas(quantiaPedida)
        elif resp == '2':
            print('Oque ocê que come?')

            # Printa a lista de barracas
            q = 0
            for barr in barracas:
                print(f'{q + 1} - {str(barr)}')
                q = q + 1

            resp = int(input("")) - 1
            # Troca as fichas pelo produto
            quantiaComprar = int(input(f'Quantos {str(barracas[resp])} ocê que?'))
            fichasRetorno += barracas[resp].vende_produto(quantiaComprar)
        elif resp == '3':
            print(f'Ainda possuimos {caixa.fichas} fichas')

        elif resp == '4':
            print('Quar barraca ocê que retorna?')

            # Printa a lista de barracas
            q = 0
            for barr in barracas:
                print(f'{q + 1} - {str(barr)}')
                q = q + 1

            resp = int(input("")) - 1

            fichasRetorno = barracas[resp].retornar_ficha()

            caixa.retornar_fixas(fichasRetorno)
            print(f'Temos {fichasRetorno} fichas pra retorno, a quantia total de fichas é de {caixa.fichas}')
            fichasRetorno = 0

        elif resp == '0':
            break

        else:
            print("Opção indisponivel")


if __name__ == '__main__':
    main()
