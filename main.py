from stats import num_words, char_counts, sorted_char_counts
import sys

def get_boot_text(filepath):
	with open(filepath) as f:
		string = f.read()
	return string
	
def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	string = get_boot_text(sys.argv[1])
	print("============ BOOKBOT ============")
	print(f'Analyzing book found at {sys.argv[1]}...')
	print("----------- Word Count ----------")
	print(f'Found {num_words(string)} total words')
	print("--------- Character Count -------")
	counts = sorted_char_counts(char_counts(string))
	for count in counts:
		if count["char"].isalpha():
			print(f'{count["char"]}: {count["num"]}')
	print("============= END ===============")
	
main()