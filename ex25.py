def break_words(stuff):
	'''This function will break up words for us.''' # 在help方法里显示注释内容
	words = stuff.split(' ')
	print(type(words))  #list
	return words

def sort_words(words):
	'''Sorts the words.'''
	return sorted(words) 
	# 函数sorted会有返回值，原list不变；方法sort返回None，改变原list

def print_first_word(words):
	''' Prints the first word after popping it off.'''
	word = words.pop(0) # 原list改变
	print(word)

def print_last_word(words):
	''' Prints the last word after popping it off.'''
	word = words.pop(-1) # 原list改变
	print(word)

def sort_sentence(sentence):
	'''Takes in a full sentence and returns the sorted words.'''
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	'''Prints the first and last words of the sentence.'''
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	'''Sorts the words then prints the first and last one.'''
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)