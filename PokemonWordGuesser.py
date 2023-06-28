import requests
import random

#Generating a random Pokemon name to be guessed in a hangman format.

num = random.randint(1,1010) #There are 1010 total possible entries

BASE_URL = "https://pokeapi.co/api/v2/pokemon/" + str(num) + "/"

response = requests.get(BASE_URL).json()

hidden_word = response['forms'][0]['name']

print("The Pokemon name to guess is: ")

for i in hidden_word:
    print("_ ", end = " ")

print()
print()

#Providing a hint about the Pokemon by giving a key characteristic which is the type.
print("Below are the type(s) of this Pokemon: ")
print()
for i in range(0,len(response['types'])):
    print((response['types'][i]['type']['name']).upper())
    
correctLetters = []                                 # "correctLetters" will keep track of all of the correctly guessed letters throughout.
failedLetters = []                                  # "failedLetters" will keep track of all of the incorrectly guessed letters.
c = 6
while(c > 0):
    print()
    print(str(c) + " chance(s) remaining.") 
    print()
    c = c - 1
    
    temp_word_lst = list(hidden_word.upper())       #Transforming hidden word into a temporary list for each iteration. 
    flag = False
    
    if(c < 5):
        print("Incorrectly guessed letters: " + str(failedLetters))
    
    print()
    enteredLetter = input("Enter a letter in caps: ")
    print()

    for letter in temp_word_lst:
        if(enteredLetter == letter):
            flag = True                             #Letter is in the word
            break

    if(flag == True):
        correctLetters.append(enteredLetter)
    else:
        print("The letter you have just entered is not in the word.")
        print()
        failedLetters.append(enteredLetter)

    for i in range(0,len(temp_word_lst)):
        if(temp_word_lst[i] not in correctLetters):
            temp_word_lst[i] = "_"                  #All currently solved letters are now displayed, the currently unsolved letters
                                                    #are shown as ' _ ' 

    print(temp_word_lst)                            #Displaying unsolved word in it's current state to the user 
    print()
        
    guess = input("Would you like to guess the Pokemon? If YES, enter your guess in upper case, otherwise just hit Enter to continue.")

    if(guess == hidden_word.upper()):
        print()
        print("CONGRATULATIONS, you have guessed the Pokemon!")
        break

print()
print("THE POKEMON WAS " + hidden_word.upper() + "!")