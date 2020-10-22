i = True
print("Good day! This is Word Palindrome Checker")

while i == True:
	default_word = input("\nGive me a word: ")
	default_list = list(default_word.strip())
	reversed_list = default_list
	reversed_list.reverse()
	reversed_word = "".join(reversed_list)
	if default_word == reversed_word:
		print(default_word, "is a Palindrome.")
	else:
		print(default_word, "is not a Palindrome.")
	while True:
		work = input("\nDo you still want to check? Y/N\n")
		if work in ("Y","N"):
			if work == "N":
				i = False
			break