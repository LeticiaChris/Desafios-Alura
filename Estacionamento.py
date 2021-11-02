
vagas = [True for x in range(1, 81)] #Quando verdadeiro a vaga está livre
somaCaixa = 0

# Total de veículos por tipo
motos = 0
carros = 0
caminhonetes = 0
caminhoes = 0


def NumeroVagas():
	vagasMoto = 0
	vagasCarro = 0
	vagasCaminhoes1 = 0
	vagasCaminhoes2 = 0
	for i in range(0, len(vagas)):
		if (i + 1) >= 1 and (i + 1) <= 20 and vagas[i]:
			vagasMoto += 1
		elif (i + 1) >= 21 and (i + 1) <= 50 and vagas[i]:
			vagasCarro += 1
		elif (i + 1) >= 51 and (i + 1) <= 70 and vagas[i]:
			vagasCaminhoes1 += 1
		elif (i + 1) >= 71 and (i + 1) <= 80 and vagas[i]:
			vagasCaminhoes2 += 1
	print('------------Possumios atualmente:---------------')
	print(f"{vagasMoto} Disponíveis para Motos\n{vagasCarro} Disponíveis para Carros\n{vagasCaminhoes1} Disponíveis para Camionetes, Vans abaixo de 15 lugares, Micro-Ônibus ou Pequenos Caminhões\n{vagasCaminhoes2} Disponíveis para Ônibus de até 40 passageiros e caminhões grandes")
	print(f"O valor total disponivel no caixa é : {somaCaixa}")

while True:
	NumeroVagas()
	print("------Bem vindo, selecione um numero do menu------")
	print("1 - Moto\n2 - Carro\n3 - Classe de Caminhonetes e Vans\n4 - Onibus e Caminhoes Grandes\n5 - Liberar Vaga\n0 - Fechar Expediente")
	resp = int(input("Qual o tipo de veiculo? \n"))
	if resp == 1:
		disponivel = -1
		for i in range(0, 21):
			if (i + 1) >= 1 and (i + 1) <= 20 and vagas[i]:
				disponivel = i
				break
		if disponivel == -1:
			print("Não existe vagas disponíveis para Motos neste momento!")
		else:
			somaCaixa += 5
			vagas[disponivel] = False
			motos += 1
			print(f"Dirija o motorista até a vaga de Número {disponivel + 1}")

	elif resp == 2:
		disponivel = -1
		for i in range(20, 51):
			if (i + 1) >= 21 and (i + 1) <= 50 and vagas[i]:
				disponivel = i
				break
		if disponivel == -1:
			print("Não existe vagas disponíveis para Motos neste momento!")
		else:
			somaCaixa += 15
			vagas[disponivel] = False
			motos += 1
			print(f"Dirija o motorista até a vaga de Número {disponivel + 1}")
	elif resp == 3:
		disponivel = -1
		for i in range(50, 71):
			if (i + 1) >= 51 and (i + 1) <= 70 and vagas[i]:
				disponivel = i
				break
		if disponivel == -1:
			print("Não existe vagas disponíveis para Motos neste momento!")
		else:
			somaCaixa += 20
			vagas[disponivel] = False
			motos += 1
			print(f"Dirija o motorista até a vaga de Número {disponivel + 1}")
	elif resp == 4:
		disponivel = -1
		for i in range(70, 81):
			if (i + 1) >= 71 and (i + 1) <= 80 and vagas[i]:
				disponivel = i
				break
		if disponivel == -1:
			print("Não existe vagas disponíveis para Motos neste momento!")
		else:
			somaCaixa += 50
			vagas[disponivel] = False
			motos += 1
			print(f"Dirija o motorista até a vaga de Número {disponivel + 1}")
	elif resp == 5:
		vaga = int(input("Informe o número da vaga que deseja liberar "))
		vagas[vaga - 1] = True
		print("Vaga liberada!")
	elif resp == 0:
		print(f"Parabens pelo trabalho, no final do dia lucramos R$ {somaCaixa},00")
		break
	else:
		print("Tipo de Veiculo não encontrado!")