import random

def piedraPapelTijera():
	humano = input("¿Piedra, papel o tijera?: ")
	maquina = random.choice(['piedra','papel','tijera'])
	if humano == 'piedra' and maquina == 'tijera':
		return "ganaste"
	if humano == 'papel' and maquina == 'piedra':
		return "ganaste"
	if humano == 'tijera' and maquina == 'papel':
		return "ganaste"
	elif humano == maquina:
		return "empate"
	else:
		return "perdiste"

bandera = True
while True:
	print(piedraPapelTijera())
	


