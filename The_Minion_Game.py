# -*- coding: utf-8 -*-
"""

@author: duong
"""

def minion_game(string):
    # your code goes here
    
    vowels = ['A', 'E', 'I', 'O', 'U']

    list_words_vowels = []
    list_words_consonants = []
    
    for i in range(1,len(string)+1):
        for j in range(len(string)-i+1):
            if string[j] in vowels:
                list_words_vowels.append(string[j:j+i])
            else:
                list_words_consonants.append(string[j:j+i])
    
    if len(list_words_vowels) > len(list_words_consonants):
        print('Kevin' + ' ' + str(len(list_words_vowels)))
    elif len(list_words_vowels) < len(list_words_consonants):
        print('Stuart' + ' ' + str(len(list_words_consonants)))
    else:
        print("Draw")
        
        
def minion_game_2(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    count_vowel_words = 0
    count_conso_words = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            count_vowel_words += len(string) - i
        else:
            count_conso_words += len(string) - i
    
    if count_vowel_words > count_conso_words: 
        print('Kevin' + ' ' + str(count_vowel_words))
    elif count_vowel_words < count_conso_words:
        print('Stuart' + ' ' + str(count_conso_words))
    else:
        print("Draw")
    
if __name__ == '__main__':
    string = 'CONSOASNFA'
    minion_game(string)