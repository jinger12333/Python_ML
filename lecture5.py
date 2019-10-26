def has_33(nums):
    '''given a a list of integers, return True if the array contains a 3 
    next to a 3 somewhere (consecutive)
    '''
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        if nums[i:i+2] == [3,3]:
            return True
    return False

print (has_33([1,2,3,3,4,5]))#need a list, use sqaure brackets to insert a list
print (has_33([2,3,4,5,6,6]))

nums = [1,2,3,4,5]
print (nums[0:3])#this prints the first 4 indexes of the list 'nums'
# list counts with '0' first


def paper_doll(text):
    ''' Given a sting, return a sting wjere for every character in the original
    there are three characters in the string returned
    EX. hello ---> hhheeellllllooo
    '''

    result=''
    for char in text:
        result= result + char + char + char
    return result
print (paper_doll("hello"))

def black_jack(card1,card2,card3):
    ''' Given three integers between 1 and 11, if their sum is less than or equal to 21, 
    return their sum.
    if their sum exceeds 21 and there is an 11, reduce the total sum by 10. 
    FINALLY , if the sum (even after adjustment) exceeds 21, return 'BUST'
    '''
    if sum((card1, card2, card3))<=21:#needs two brackets here because it's the function's input
        return sum((card1,card2, card3))   


    elif sum ((card1, card2, card3)) <= 31 and 11 in (card1, card2, card3): 
        return sum ((card1,card2, card3)-10)   
    else:
        return ("BUST!!!")

print (black_jack(11,11,10))
print (black_jack(2,1,10))
print (black_jack(13,12,10))

def spy_game(nums):
    '''
    # wwrite a function that takes in a list of integers and reutrn true 
    # if it countains 007 in ORDER
    '''
    code = [0,0,7,"x"]
    for num in nums:
        if num == code [0]:
            code.pop(0)#removes the 0th element on this list
    return len(code) == 1 #this will return True of Flase 


print(spy_game([1,0,4,5,7]))

#i gave up

#Lamba Expressions, Map , and Filter Functions
#Map Function: the map fuction allows you to  'map' a function to an iterable obeject. 
#THis means you can quickly call the same function for every item in an iterable, 
#such as a list

def square(num):
    return num**2 #this sqaures 'num'
my_nums = [1,2,3,4,5]

print([num**2 for num in my_nums])

print(list(map(square, my_nums)))


def splicer(my_string):
    if len(my_string)% 2 == 0:
        return 'even'
    else:
        return my_string[0]
        # this funciton returns even when string is divisible by 2
my_names = ['John','Cindy','Sarah','Kelly','Mike']
print(list(map(splicer, my_names)))

#Filter Functions: returns an iterator yieldind those items of iterable
#for which fuction item is true.  I checks whether or not the functions are 
# funtioning correctly
'''Meaning you need to filter by a function that returns either True or False.  
then passing that into filter, along with your iterable, you get back only the results
that would return True from the function.'''

def check_even(num):
    return num % 2 == 0

nums = [0,1,2,3,4,5,6,7,8,9,10]
print (list(filter(check_even, nums)))

#Lamba Expression:allows us to create "anonymous"
# functions. This meaning we can quickly make ad-hoc functions
# without nedding to preperly define functions using def.

def square(num):
    result = num **2
    return result
square(2)

# one liner
def square(num): return num** 2 
square(2)

#the lambda way
square = lambda num:num**2
square(2)
