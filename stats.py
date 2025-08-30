def num_words(book):
	list = book.split()
	return len(list)
	
def char_counts(string):
	dict = {}
	for i in range(len(string)):
		if string[i].lower() in dict:
			dict[string[i].lower()] += 1
		else:
			dict[string[i].lower()] = 1
	return dict

def sort_on(items):
    return items["num"]
	
def sorted_char_counts(dict):
	counts = []
	for item in dict:
		counts.append({"char": item, "num": dict[item]})
	counts.sort(reverse = True, key = sort_on)
	return counts