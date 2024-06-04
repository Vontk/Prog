def slice_advanced():
	texto = input("Tu Texto!: ")
	length = len(texto)
	#al parecer con slice [a:b:c] a sera la posicion inicial y b la final y c el paso, es decir cuantos caracteres salta. va a empezar en a + c.
	print(texto[4:length:2])
slice_advanced()