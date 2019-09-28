
def lesser_of_two(a,b):
    '''
    a function that returns the lesser of two given numbers if BOTH are even
    but returns the greater if one or both numbers are odd.
    '''
    if a % 2==0 and b % 2 ==0:
        return min(a,b)
    else:
        return max(a,b)


print(lesser_of_two(2,4))

print(lesser_of_two(2,5))


def animal_crackers(text):
    '''
    This function takes a two-word string and returns True if BOTH words being with the same letter
    Hint:use   .split()
    '''
    wordList = text.lower().split()
    print(wordList)
    result= wordList[0][0] == wordList[1][0]
    return result



print(animal_crackers('levelheaded Llama'))
print(animal_crackers('lady Gaga'))

def makes_twenty(n1, n2):
    '''
    Diven two intergers, return True if the sum of the integers is 20 or id one of the integers is 20
    if not, return false
    '''
    return(n1+n2)==20 or n1==20 or n2==20
print('20+1',makes_twenty(20,1))
print('15+5',makes_twenty(15,5))
print('10+39',makes_twenty(10,39))

#HARD LEVEL1
def old_macdonald(name):
    ''' 
    write a function that capitalizes the first and fourth letter of name
    If the name is less than 4 letters, return "name is too short"
    *Hint: len() checks the length of a object
       .capitalize()makes the currnt character Capital
       '''
    if len(name) < 4:
        return "Sorry, your name is too short"
    else:
        return name[:3].capitalize() + name[3:].capitalize()

print(old_macdonald('macdonald'))
print(old_macdonald('jam'))

def fake_master_yoda(sentence):
    '''
    given a sentence, and return it back reversed
    '''
    wordList=sentence.split(" ")
    return ' '.join(wordList[::-1]) #going from front to back by -1 reverses it

print(fake_master_yoda('I am home'))
print(fake_master_yoda('We are ready'))

def real_master_yoda(sentence):
    '''given a sentence, return another sentence with the first 2 or 3 words added tp the end of the sentence
    'you will find what you are looking for', turns into' Find what you are looking for, you will'
    '''
    import random
    number_of_words = random.randint(2,3)
    wordList = sentence.split()
    if len(wordList) < 3:
        return sentence 
    else:
        return ' '.join(wordList[number_of_words:] + wordList[:number_of_words])

print(real_master_yoda("you will find what you are looking for"))

def we_are_almost_there(n):
    '''
    Given an integer n, return True if n is with 10 or either 100 or 200
    '''
    return abs(100-n)<=10 or abs(200-n)<=10
print(we_are_almost_there(100))

def print_big(letter):
    ''' write a function that akes in a single letter and returns 
    a 5x5 representation of that letter
    '''
    patterns = {
        1:'  *  ',
        2:' * * ',
        3:'*   *',
        4:'*****',
        5:'**** ',
        6:'   * ',
        7:' *   ',
        8:'*  * ',
        9:'*    ',
        10:'* ***',

    }   
    alphabet ={
        'A':[1,2,4,3,3],
        'B':[5,3,5,3,5],
        'C':[4,9,9,9,4],
        'D':[5,3,3,3,5],
        'E':[4,9,4,9,4],
        'F':[4,9,4,9,9],
        'G':[4,9,10,3,5],
    
    }
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('g')