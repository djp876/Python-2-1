#Word frequency count program
text = input("Enter the text :").split()
key_word = input("Enter the word :")
if key_word in text:
    print(key_word,text.count(key_word))