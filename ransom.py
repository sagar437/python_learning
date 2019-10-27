def checkMagazine(magazine, note):
	count_yes = 0
	mag = list(magazine.split(" "))
	noted = list(note.split(" "))
	print(mag)
	print(noted)
	for each in noted:
		if each in mag:
			count_yes += 1
		else:
			pass
	if count_yes == len(noted):
		print('yes')
	else:
		print('no')
magazi = 'I am no one'
notess = 'I am no one'
checkMagazine(magazi,notess)
