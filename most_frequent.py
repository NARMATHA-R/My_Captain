#Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

text = input("Please enter a string ")
def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)# dictionary.get('letter', 0) tells python to look for the 'letter' in the dictionary
    return dictionary

def most_frequent(text):
   letters = [letter.lower() for letter in text if letter.isalpha()]
   dictionary = make_dict(letters)
   result = []
   for key in dictionary:
        result.append((dictionary[key], key))
   result.sort(reverse=True)
   for count, letter in result:
        print( letter, count ,end=' ')

most_frequent(text)

#OUTPUT
Please enter a string Mississipi
s 4 i 4 p 1 m 1 
