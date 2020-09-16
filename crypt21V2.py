from random import shuffle

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def count_concidences(Func):
	count = {}
	for i in Func:
		if i in count:
			count[i] += 1
		else:
	  		count[i] = 1
	return count;

def encrypt(key):
	shuffle(key)

def read_data(data_type):
	letters = []
	#READ DATA
	for i in range(30):
		try:
			open_file = str(data_type)+str(i)+str('_crypt.txt')
			with open(open_file, 'r') as data:
				letters_in_text.append(data.read())
				available_variants.append(i)
		except:
			pass

	#SPLITTING A TEXT INTO LETTERS
	for i in range(len(letters_in_text)):
		letters += letters_in_text[i]
	print(len(letters), ' quantity of letters')
	count = count_concidences(letters)

	#REMOVE NON_DICTIONARY CHARACTERS 
	for key, value in count.items():
		if key in ABC:
			pass
		else:
			count = removekey(count, key)
	
	#SORTING LETTERS BY APPEARANCE FREQUENCY
	keys_sorted = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])};
	print(keys_sorted, ' letters appearance frequency')
	return keys_sorted, letters_in_text;


def substitution_of_letters(letters_in_text, FrequentlyUsedLetters ,type_of_proccessing):
	change_letters = {}
	#CHANGING LETTERS WITH FREQUENTLY APPEARING ONES
	i=len(FrequentlyUsedLetters)-1
	for key, value in keys_sorted.items():
		change_letters[key] = FrequentlyUsedLetters[i]
		i-=1
	for k in range(len(letters_in_text)):
		letters_list = list(letters_in_text[k])
		for i in range(len(letters_list)):
			if letters_list[i] in ABC:
				letters_list[i] = change_letters[letters_list[i]]
			else:
				pass

		#DATA STORAGE
		file_name = str(type_of_proccessing)+str(available_variants[k])+str('_crypt.txt')
		text_with_changed_letters.append("".join(letters_list))
		file = open(file_name,'w')
		file.write(text_with_changed_letters[k])
		file.close()

#DICTIONARY AND DATA INITIALIZING
ABC = ['а', 'б','в', 'г','д','е','ё', 'ж','з', 'и', 'й','к', 'л','м', 'н','о','п','р', 'с','т', 'у','ф', 'х','ц', 'ч','ш', 'щ','ъ', 'ы','ь', 'э','ю', 'я']
delta, old_letters, new_letters, possible_shifts, letters_in_text, available_variants, words = [], [], [], [], [],[], []
text_with_changed_letters = []

type_of_proccessing = input('type_of_proccessing (encrypt/decrypt): ')
while True:
	if type_of_proccessing == 'decrypt':
		#LIST OF FREQUENTLY APPEARING LETTERS
		FrequentlyUsedLetters = ['о','е','а','и','н','с','т','л','в','р','д','к','м','у','п','г','я','ь','б','з','ы','ч','й','ж','ш','х','ю','щ','ц','ф','э','ъ']

		#READ DATA
		keys_sorted, letters_in_text = read_data('')

		#LETTERS EXCHANGE
		substitution_of_letters(letters_in_text, FrequentlyUsedLetters, type_of_proccessing)
		print('files were decrypted')
		break

	elif type_of_proccessing == 'encrypt':
		key = list(ABC)
		encrypt(key)	#ENCRYPTING
		keys_sorted, letters_in_text  = read_data('decrypt')
		substitution_of_letters(letters_in_text, key, type_of_proccessing)
		file = open('key.txt','w')
		for i in range(len(ABC)):
			file.write(str(ABC[i])+str(' = ')+str(key[i])+str('\n'))
		file.close()
		print('files were encrypted')
		break

	else:
		print('write it again, there is a mistake!')
		type_of_proccessing = input('type_of_proccessing (encrypt/decrypt): ')