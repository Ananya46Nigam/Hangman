import random
import hangman_words
import hangman_art
from hangman_art import logo
from hangman_art import stages
#4- Inserting ASCII art for hangman




theme_no=input("Choose hangman game's theme number :\n1.Fruits\n2.Bollywood Movies\n3.Hollywood Movies\n4.Random words !!\n")
#1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

if theme_no == "1":
    chosen_word=random.choice(hangman_words.fruit_list)
elif theme_no=="2":
    chosen_word=random.choice(hangman_words.bolly_list)
elif theme_no=="3":
    chosen_word=random.choice(hangman_words.holly_list)
elif theme_no=="4":
    chosen_word=random.choice(hangman_words.word_list)
else:
    print("Please enter a valid number 1 or 2 or 3 or 4 to play the game!")





#2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

word_len=len(chosen_word)

blank_list=[]
for _ in range(word_len):
    blank_list.append("_")
# blank_list=("_ "*word_len)
print(blank_list)


#3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


lives=7

while "_" in blank_list and lives>0:
    guess=input("\nMake a letter guess ! => ").lower()
    
    if guess in blank_list:
        print("You have already guessed the letter",guess)
    
    for position in range(word_len):
        letter=chosen_word[position]
        
        if guess==letter:
            # print("Good Guess !")
            blank_list[position]=guess
            print(stages[lives])
            
            
    if guess not in chosen_word:
            life=stages[lives]
            print(life)
            lives-=1
            print(f"\nOoops! the letter : {guess} is incorrect guess.\n")
            print(lives,"chances left to survive.")
     
    print(" ".join(blank_list))


if lives>0:   
    print("\nThe secret word was : ","".join(blank_list))
          
    
    print("\n********** Hurray !! You won the game ********** \n")  
    
else:
    print("\n********** You Lost ********** \n")
    print("\nThe secret word was : ",chosen_word)
    print("XXXX The man has been hung XXXX")
    