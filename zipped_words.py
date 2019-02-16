import zipfile
import string

archive = zipfile.ZipFile('zadanie_1_words.zip', 'r')

file_dict = {}
for letter in string.ascii_lowercase:
	file_dict[letter] = 0
for file in archive.namelist():
	word_file = archive.read(file)
	for letter in str(word_file):
		if letter.lower() in file_dict.keys():
			file_dict[letter.lower()] += 1
print(file_dict)

