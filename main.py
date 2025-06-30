import random 

def word_guessing_game():
    words = ["cat", "dog", "elephant", "lion", "tiger"]
    word = random.choice(words).upper()
    chances = 5
    underscore = "_" * len(word)
    while True:
        print(underscore)
        guess = input("Enter a letter to guess : ").upper()
        if guess in word:
            for index in range(len(word)):
                if guess == word[index]:
                    underscore = underscore[:index] + guess + underscore[index+1:]
            if underscore == word:
                print(word)
                print("Congratulation ! You won !!!")
                break
        else:
            chances -= 1
            if chances == 0:
                print("You lose !!!")
                break
            print(f"{chances} left")
            print("Wrong guess !!!")

word_guessing_game()

again = input("Do you want to play again (y/n) : ").lower()

if again == "y":
    word_guessing_game()
elif again != "y" or again != "n":
    print("Error !!! You entered wrong letter you have to enter (y/n).")
else:
    print("Thanks for playing !!!")
