import random

def computerGuess(lowval, highval, randum, count=0):
    if highval>=lowval:
        guess=lowval+(highval-lowval)//2
        if guess==randum:
            return count
        # if "guess" is greater than the number,
        # It must be found in the lower half set of the number
        #between the lower value and guess
        elif guess > randum:
            count=count+1
            return computerGuess(lowval, guess-1, randum, count)
        #the number must be in upper set of numbers
        #between the guess and the uppper value
        else:
            count=count+1
            return computerGuess(guess +1, highval, randum, count)
    else:
        #Number not found
        return -1
#end of function


#gentrate a random number between 1 and 100
randum= random.randint(1,101)

count=0
guess=-99
while(guess!=randum):
    #Get the user guess
    guess =  int(input("Enter your guess between 1 and 100:"))

    if guess < randum:
        print("higher")
    elif guess > randum:
        print("lower")
    else:
        print("you gussed it!")
        break
    count=count+1
#end of while loop

print("You took " +str(count)+ " steps to guess the number")
print("computer took "+ str(computerGuess(0,100, randum))+ " steps!")