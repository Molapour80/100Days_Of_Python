try:
    text = input("Enter your text:")
    count_alpha =len(text.split())
    count_word = len(text)
    print(f"This text have {count_alpha}\n "
          f"count_word :{count_word}")
except:
    print("this is not True")
