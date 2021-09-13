
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
notas = (n1, n2, n3, n4)


def notas_d():
    for nota in notas:
        if nota > 10 or nota < 0:
            print('Nota(s) invalida(a), digite(as) novamente')
            break

    calculo_notas()


def calculo_notas():
    soma = n1 + n2 + n3 + n4
    if soma == 0:
        print("Nossa, você tirou 0 em todas, boa sorte na proxima... Reprovado")
    else:
        divisa = soma / 4

        if divisa >= 4 and divisa <= 6:
            print("Notas: |{}|{}|{}|{}| --> {}".format(n1, n2, n3, n4, divisa))
            print("Que pena, em recuperação")
        elif divisa < 3.9:
            print("Notas: |{}|{}|{}|{}| --> {}".format(n1, n2, n3, n4, divisa))
            print("Puts, você foi Reprovado...")
        elif divisa >= 6:
            print("Notas: |{}|{}|{}|{}| --> {}".format(n1, n2, n3, n4, divisa))
            print('Parabens, você passou')


notas_d()
