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

def sort_keys():
	return {k: v for k, v in sorted(count.items(), key=lambda item: item[1])};
'''
def find_character(word):
	for j in range(len(word)): 
    	if word[j] == 'о': 
        	res = i + 1
        	break
'''
change_letters = {}
#FrequentlyUsedLetters = ['о', 'е', 'а', 'и','н','т','с','р','в','л','к','м','д','п','у','я','ы','ь','г','з','б','ч','й','х','ж','ш','ю', 'ц','щ','э','ф','ё']
#FrequentlyUsedLetters = ['о','а','е','и','н','т','р','с','л','в','к','п','м','у','д','я','ы','ь','з','б','г','й','ч','ю','х','ж','ш','ц','щ','ф','э','ъ']
FrequentlyUsedLetters = ['о','е','а','и','н','с','т','л','в','р','д','к','м','у','п','г','я','ь','б','з','ы','ч','й','ж','ш','х','ю','щ','ц','ф','э','ъ']

ABC = ['а', 'б','в', 'г','д','е','ё', 'ж','з', 'и', 'й','к', 'л','м', 'н','о','п','р', 'с','т', 'у','ф', 'х','ц', 'ч','ш', 'щ','ъ', 'ы','ь', 'э','ю', 'я']
delta, old_letters, new_letters, possible_shifts, letters, temp, available_variants, words = [], [], [], [], [], [],[], []
text_with_changed_letters = []


for i in range(30):
	try:
		open_file = str(i)+str('_crypt.txt')
		with open(open_file, 'r') as data:
			temp.append(data.read())
			available_variants.append(i)
	except:
		pass
for i in range(len(temp)):
	letters += temp[i]
print(len(letters), ' quantity of letters')

count = count_concidences(letters)

for key, value in count.items():
	if key in ABC:
		pass
	else:
		count = removekey(count, key)

keys_sorted = sort_keys()
print(keys_sorted, ' letters appearance frequency')
i=len(FrequentlyUsedLetters)-1
for key, value in keys_sorted.items():
	change_letters[key] = FrequentlyUsedLetters[i]
	i-=1
for k in range(len(temp)):
	letters_list = list(temp[k])
	for i in range(len(letters_list)):
		if letters_list[i] in ABC:
			old_letters.append(letters_list[i])
			letters_list[i] = change_letters[letters_list[i]]
			new_letters.append(letters_list[i])
		else:
			pass
	file_name = str('modified_crypt')+str(available_variants[k])+str('.txt')
	text_with_changed_letters.append("".join(letters_list))
	file = open(file_name,'w')
	file.write(text_with_changed_letters[k])
	file.close()
