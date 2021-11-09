#hanman game
import random
import ascii
import words

print(ascii.hangman)
end_of_game = False
lives = 6
word_list = words.word_list
word_choice = random.choice(word_list)
print(word_choice)

blanks = []
for i in range(len(word_choice)):
    blanks.append("_")


guessed = ""

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in blanks:
        print(f"you guessed {guess} ")
    for position in range(len(word_choice)):
        if word_choice[position] == guess:
            blanks[position] = guess

    print(blanks)

    if guess not in word_choice:
        print(f"You guessed {guess} that letter is not in word, you lose a life")
        lives -= 1
        print(ascii.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")

    if "_" not in blanks:
        end_of_game = True
        print("Game over, You win")




