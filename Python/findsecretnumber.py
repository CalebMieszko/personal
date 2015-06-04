#This program will guess the user's number between 0 and 100 based on their input.
low = 0
high = 100
guess = (high + low)/2
numFound = 0

print('')
print('Please think of a number between 0 and 100!')
while numFound == 0:
    print('')
    print('Is your secret number ' + str(guess) + '?')
    response = (raw_input('Enter ' + "'h'" + ' to indicate the guess is too high. Enter ' + "'l'" + ' to indicate the guess is too low. Enter ' + "'c'" + ' to indicate I guessed correctly.: '))
    if response == 'h':
        high = guess
        guess = (low + high)/2
    elif response == 'l':
        low = guess
        guess = (high + low)/2
    elif response == 'c':
        numFound = 1
        break
    else:
        print("Sorry, I did not understand your response.  Please respond to my questions with only the letters 'c', 'l', or 'h'.  Let's try this again!")


print('Game over.  Your secret number was ' + str(guess) + '.')