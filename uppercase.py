def index_of_caps(word):
	new_list = []
	for i in range(len(word)):
		if word[i].isupper() == True:
			new_list.append(i)
	print(new_list)

name = input("enter a word")
index_of_caps(name)
