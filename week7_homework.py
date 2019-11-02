# Machine Learning Class Week 7 Homework

# 1. Write a shutting down program:
# First, def a function, shut_down, that takes one argument s. 
# Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down" 
# Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted". 
# Finally, if shut_down gets anything other than those inputs, the function should return "Sorry".


def shut_down(s):
    if s.lower()=='yes':
        return 'Shutting down'
    elif s.lower()=='no':
        return 'Shutdown aborted'
    else:
        return 'Sorry'
    pass



s = "no"
print(shut_down(s))

# 2. Import the math module in whatever way you prefer. 
import math 
# Call its sqrt function on the number 13689 and print that value to the console.
print(math.sqrt(13689))


# 3. First, def a function called distance_from_zero, with one argument (choose any argument name you like). 
# If the type of the argument is either int or float, the function should return the absolute value of the function input. 
# Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and "what?".


def distance_from_zero(num):
    if str(num) == num :
        return 'Nope'
    else:
        return abs(num)


print(distance_from_zero(-5.6))
print(distance_from_zero("what?"))

# 4. Rewrite the pay computation program with time-and-a-half for overtime and 
# create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0


def computepay(hours, rate):
    if hours > 43:
        overtime=hours-43
        return (overtime*1.25*rate)+hours*rate
    

print(computepay(45, 10))