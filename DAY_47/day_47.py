import string

# frist part :
text = input("Please Enter your text :")
text = text.lower()

for punct in string.punctuation:
    text = text.replace(punct,'')

words = text.split()

word_count = len(words)

print(f"count word in the text:{word_count}")



