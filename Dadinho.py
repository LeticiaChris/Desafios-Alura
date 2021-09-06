import random

VSim = ("yes", "sim", 'ss', 's', "true", 'yep')
VNao = ("nao", "não", "no", "false", "n", "nop")


def Pergunta():
    print("Olá, gostaria de rodar o dado?")
    resposta = input().lower()
    if resposta in VSim:
        Rodar_Dado()
    elif resposta in VNao:
        print('Ok, tenha um bom dia')
    else:
        print('resposta inválida')
        Pergunta()


def Rodar_Dado():
    print("quantos lados seu dado tem?")
    LadosPedidos = int(input())
    Limite = LadosPedidos + 1
    print("Seu dado caiu no número {}".format(random.randrange(1, Limite)))
    Pergunta()


Pergunta()
