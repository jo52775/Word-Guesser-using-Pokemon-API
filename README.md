# Word-Guesser-using-Pokemon-API
This Python project uses PokeAPI V2 (Details found at https://pokeapi.co/). Firstly, every time the project is run, a random ID from the API will be selected, therefore
increasing the ambiguity. In a hangman style format, users are allowed six chances to guess a letter that might be in the hidden word. Each turn, users are given the
opportunity to guess the word outright. If the word is guessed correctly, the user wins and the game ends. Otherwise, the user will keep guessing until the amount of chances runs out. 
Important notes from the code:
- Letters that have been guessed correctly are revealed in the word.
- Letters that are guessed incorrectly are displayed to the user so that they are not chosen again.
- In the case that all letters are not guessed, but the user desires to guess the entire word, they have the opportunity to do so each turn.
- A key hint, which is the type of Pokemon, is given to the user before they start guessing. The types are taken from the data that is provided by the API.
