with open('rows.txt', 'r') as f:
	content = f.readlines()

suma_kontrolna=0
for row in content:
	new_string = row.strip().split("\t")
	int_array=[]
	for value in new_string:
		int_array.append(int(value))
	suma_kontrolna+=((max(int_array) - min(int_array)))
print(suma_kontrolna)


	