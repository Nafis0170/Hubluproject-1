#Text Based adventure game
answer=input("do you want to play this adventurus game?:[Yes/No]")
if answer=="Yes" or answer=="yes"or answer=="YES":
    print("Welcome to the game!")
    answer2=input("Do you want to go to Jungle or cave?[jungle/cave]")
    if answer2=="Cave" or answer2=="CAVE" or answer2=="cave":
        print(" You have entered into a cave and now you are infront of a bear.")
        answer3=input("Do you want to fight with bear or you want to run?[fight/run]")
        if answer3=="fight" or answer3=="FIGHT" or answer3=="Fight":
            print("Oops bear is stronger than you!\n So you died here!")
        elif answer3 == "Run"or answer3=="RUN" or answer3=="run":
            print("Hurray!You you are escaped from bear")
        else:
            print(" Please choose one of mentioned words")
    elif answer2 == "JUNGLE" or answer2=="Jungle" or answer2=="jungle" :
        print("You are in the jungle! You can see some wild animals.\n They are so beautiful and gorgeous.")
        x=input(" Do you want to stay for a while in this jungle or leave?[stay/leave]")
        if x== "stay" or x=="Stay "or x=="STAY":
            print("Enjoy the scinario")
        else:
            print("You are out of the jungle now.\n Good bye!")
    else:
        print(" Choose only one of mentioned keywords")
else:
    print("try this game later")
