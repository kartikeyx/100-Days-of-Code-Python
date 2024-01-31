import random
import hangman_words
#import hangman_art


end_of_game = False
chosen_word = random.choice(hangman_words.word_list)


word_length = len(chosen_word)

from hangman_art import logo
print(logo)

lives = 6



display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed the letter {guess}")

   
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        print(f"Guessed letter {guess} is not in chosen word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE")
                    
    

    
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])