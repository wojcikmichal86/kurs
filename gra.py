import random
dalej='t'
knp = {'P': 'Papier', 'K': 'Kamień', 'N': 'Nożyce'}
gracz_score = 0
komp_score = 0
while dalej == 't':
	wyniki = {
	('P', 'Papier'): 'remis', ('P', 'Kamień'): 'gracz', ('P', 'Nożyce'): 'komputer',
	('K', 'Kamień'): 'remis', ('K', 'Papier'): 'komputer', ('K', 'Nożyce'): 'gracz',
	('N', 'Nożyce'): 'remis', ('N', 'Kamień'): 'komputer', ('N', 'Papier'): 'gracz'
	}
	wybor_komp = random.choice(['Papier', 'Kamień', 'Nożyce'])
	wybor = input('Wybierz figurę: (P)apier, (K)amień, (N)ożyce > ').upper()
	print('Gracz: ' +knp[wybor])
	print('Komputer: '+wybor_komp)
	#if wybor
	wygr = '+--------------+\n'+'|Gracz wygrywa!|\n'+'+--------------+'
	przegr = '+-----------------+\n'+'|Komputer wygrywa!|\n'+'+-----------------+'
	remis = '+------+\n'+'|Remis!|\n'+'+------+'
	rezultat = wyniki[(wybor, wybor_komp)] 
	if rezultat == 'gracz':
		print(wygr)
		gracz_score += 1
	elif rezultat == 'komputer':
		print(przegr)
		komp_score += 1
	else:
		print(remis)
	print('Aktualny wynik: Gracz %i:%i Komputer'%(gracz_score, komp_score))
	dalej = input('Czy chcesz grać dalej [t/n]? > ').lower()
	if dalej == 't':
		print('=================================')

