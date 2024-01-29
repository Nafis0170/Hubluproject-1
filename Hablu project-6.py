#Hangman Game: Word game. If someone lost this game then he/she will be hanged
word="Hablu"
chances=7
GuessAdd=[]
done=False #mane done hoi nai
while not done: #while done==False: etao likha jai
    MyGuess=input(f"Your chances {chances}, Next letter guess: ")
    GuessAdd.append(MyGuess.lower())
    for letter in word:
        if letter.lower() in GuessAdd:
        #if GuessAdd in letter.lower():( eta hobe na karon list k shudu list er sathe compare kora
        #kintu string ke list er sathe compare kora jai
            print(letter, end=" ")
        else:
            print("-",end="")

    if MyGuess.lower() not in word.lower():
        chances=chances-1 #chances-=1
        if chances==0:
            break
    done=True

    for letter in word:
        if letter.lower() not in GuessAdd:
            done=False
if done:
    print(f"yes, you won the game, the word is {word}")
else:
    print(" you lost the game")




