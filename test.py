pyg = 'ay'
original = input('Enter a Word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == ('a'or 'e'or'i'or'o'or'u'):
        new_word = word + pyg
        print (new_word)
    else:
        new_word = word[1:] + first + pyg
        print (new_word)
else:
    print ('empty')