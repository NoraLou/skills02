





string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	count_unique = {}
	for word in string1:
		count_unique[word] = count_unique.get(word, 0) + 1
	return count_unique

print(count_unique(string1))

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""

def common_items(list1, list2):
	list1.extend(list2)
	for i in range(len(list1)):
		list1[i] = (list1[i], list1.count(list1[i]))
	common_items = []	
	for pair in list1:
		if pair[1]>1:
			common_items.append(pair[0])
	return common_items
    
print(common_items(list1,list2))
 
"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	w_dict = {}
	list1.extend(list2)
	for item in list1:
		w_dict[item] = w_dict.get(item, 0) + 1
	common = []
	for i in w_dict:
		if w_dict[i]>1:
			common.append(i)
	return common

print (common_items2(list1,list2))

"""
Given a list of numbers, return list of number pairs that sum to zero
"""

def sum_zero(list1):
	sum_zero_lis = []
	for item in list1:
		item = (item, 0-item)
		sum_zero_lis.append(item)
	return sum_zero_lis

print(sum_zero(list1))

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	no_dups = []
	set_no_dups = set(words)
	for i in set_no_dups:
		no_dups.append(i)
	return no_dups


print(find_duplicates(words))

"""
# Given a list of words, print the words in ascending order of length
# Bonus: do it on a file instead of the list provided
# Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
	word_length_lis = []
	for item in words:
		item = (len(item),item)
		word_length_lis.append(item)
	word_length_lis.sort()
	return word_length_lis

print(word_length(words))

"""
# Here's a table of English to Pirate translations
# English     Pirate

# sir         matey
# hotel       fleabag inn
# student     swabbie
# boy         matey
# madam       proud beauty
# professor   foul blaggart
# restaurant  galley
# your        yer
# excuse      arr
# students    swabbies
# are         be
# lawyer      foul blaggart
# the         th'
# restroom    head
# my          me
# hello       avast
# is          be
# man         matey

# Write a program that asks the user to type in a sentence and then
# print the sentece translated to pirate.
# """

 
p_dict = {
	'sir' : 'matey',
	'hotel' :'fleaba inn',
	'student' : 'swabbie',
	'boy' : 'matey',
	'madam' : 'proud beauty',
	'professor' : 'foul blaggart',
	'restaurant' : 'galley',
	'your' : 'yer',
	'excuse' : 'arr',
	'students': 'swabbies',
	'are':'be',
	'lawyer':'foul blaggart',
	'the':'th',
	'restroom':'head',
	'my':'me',
	'hello' : 'avast',
	'is':'be',
	'man': 'matey'
	}

# sentence = raw_input("Please give us a song..")
sentence = "Sir where can I find a hotel for my students ?"

def pirate_translation():
	sentence = raw_input("give me a song")
	translation = " "
	split = sentence.lower().split()	
	for i in range(len(split)):
		if split[i] in p_dict:
			translation += " " + p_dict[(split[i])]
		else:
			translation += " " + split[i]
	return translation	


print(pirate_translation()) 


























