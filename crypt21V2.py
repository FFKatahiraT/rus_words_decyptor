from random import shuffle

def dict_to_list(dictionary):
	dictlist=[]
	for key, value in dictionary.items():
	    #temp = [key,value]
	    dictlist.append(key)
	return dictlist;

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


def substitution_of_letters(letters_in_text, keys_sorted, FrequentlyUsedLetters ,type_of_proccessing):
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
		substitution_of_letters(letters_in_text, keys_sorted, FrequentlyUsedLetters, type_of_proccessing)
		print('files were decrypted')
		break

	elif type_of_proccessing == 'encrypt':
		keys_sorted, letters_in_text  = read_data('decrypt')
		key = dict_to_list(keys_sorted)
		encrypt(key)	#ENCRYPTING
		substitution_of_letters(letters_in_text, keys_sorted, key, type_of_proccessing)
		keys_sorted = dict_to_list(keys_sorted)
		keys_sorted.reverse()
		file = open('key.txt','w')
		for i in range(len(key)):
			file.write(str(keys_sorted[i])+str(' = ')+str(key[i])+str('\n'))
		file.close()
		print('files were encrypted')
		break

	elif type_of_proccessing == 'read':
		real_letter, crypt_letter=[], []
		with open(str('key.txt'), 'r') as data:
			data_new = data.readlines()
			for i in range(len(data_new)):
				elements = data_new[i].strip().split(' = ')
				real_letter.append(elements[0])
				crypt_letter.append(elements[1])
		keys_sorted, letters_in_text  = read_data('encrypt')
		crypt_letter.reverse()
		crypt_letter = dict.fromkeys(crypt_letter, "")
		print(crypt_letter, 'crypt_letter')
		print(real_letter, 'real_letter')
		substitution_of_letters(letters_in_text, crypt_letter, real_letter, type_of_proccessing)
		break

	else:
		print('write it again, there is a mistake!')
		type_of_proccessing = input('type_of_proccessing (encrypt/decrypt): ')