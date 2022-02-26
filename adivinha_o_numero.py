import random

historico = []

numMe = int(random.randint(1, 10))

print("(--- Escreve 'q' para saires ---)")
print('\nAdivinha o numero de 1 a 100 que estou a pensar...')

while True:

	user_number = int(input('\nAcho que é o número: '))
	historico.append(user_number)

	if user_number < numMe:
		print('\nNão, é MAIOR, adivinha outra vez')
		if user_number == 'q':
			break

	if user_number > numMe:
		print('\nNão, MENOR... adivinha outra vez')
		if user_number == 'q':
			break

	if user_number == numMe:
		print('------------------------------------------------------')
		print('\nBoa! Conseguiste! Estavava pensar no número::: ' + str(numMe))
		break

print('\nAdivinhaste em: ' + str(len(historico)) + ' tentativas!')
print('\n(Estes foram os números que tentaste): ' + '\n' + str(historico))

print('\nPressiona (Command + R) para novo jogo.')
