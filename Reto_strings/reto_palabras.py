
def isogram (word) :
    condition = True
    count_past = 0
    count_now = 0
    for i in range(0, len(word),1) :
        if (i == 0) :
            count_now = word.count(word[i])
        else :
            count_past = count_now
            count_now = word.count(word[i])
            condition = condition and (count_now == count_past)
    if condition : 
        print(f'{word.capitalize()} es un isograma')
    else :
        print(f'{word.capitalize()} no es un isograma')

def palidrom (word) :
    w = word[::-1]
    if (w == word) :
        print(f'{word.capitalize()} es un palíndromo')
    else :
        print(f'{word.capitalize()} no es un palíndromo')

def anagram (worda, wordb) :
    if(sorted(worda) == sorted(wordb)) :
        print('Ambas palabras son anagramas')
    else :
        print('Ambas palabras no son anagramas')




word1 = input('Ingrese la primera palabra: ')
word2 = input('Ingrese la segunda palabra: ')

word1 = word1.lower().removesuffix('.')
word2 = word2.lower().removesuffix('.')

isogram(word1)
isogram(word2)

palidrom(word1)
palidrom(word2)

anagram(word1, word2)


'''if (len(word1) == len(word2)) :
    for i in range(0, len(word2), 1):
        if (word1.count(word1[i]) == word2.count(word1[i])):
            if(i == (len(word1) - 1)) :
                print(f'Ambas palabras son anagramas')
        else :
            print('Ambas palabras no son anagramas')
            break;
else :
    print('Ambas palabras no son anagramas')
print('Fin de programa')
'''