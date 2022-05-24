import random
import time

game = True
exit_game = False


while (exit_game == False):
    play = True
    select_game = input("Which game do you want to play\n1.Coin Flip\n2.Dice\n3.Exit\n")
    print(select_game)
    if select_game == '1':
        game = True
    elif select_game == '2':
        game = False 
    elif select_game == '3':
        exit_game = True
        game = None

    if game == True:
        win_count = 0
        total_count = 0
        while (play == True):
            if total_count != 0: print ("You have played:", total_count, "time(s)\nYou have won:",win_count,"time(s)\n")
            
            total_count +=1
            # Generates a random number which will be uses to define the outcome of the game
            random_number = random.randint(1,2)
            Head_Tails = ""

            #Promp the user for their guess 

            guess = input("Write your guess, Heads or Tails\n")
            #Depending on the random number generated we define the correct Head_Tails

            Head_Tails = "Heads" if random_number == 1 else "Tails"
            #A little bit of drama

            for i in range (3,0,-1): time.sleep(1); print (i) 
            #Give the correct answer and the user guess
            time.sleep(0.5)
            print("\nCoin landed on:", Head_Tails)
            time.sleep(0.5)
            print ("\nYour guess was...", guess)

            #Decide if the user won or not.
            time.sleep(0.5)
            if guess == Head_Tails:
                print ("\nYOU WON!") 
                win_count +=1  
            else: 
                print("\nYou lost :c")

            repeat = input("Another round? Y/N\n")

            if repeat == "N" or repeat == "n": play = False 

        print ("You played:", total_count, "time(s)\nYou won:",win_count,"time(s)\nBye! :D")
    elif game == False:
        win_count = 0
        total_count = 0
        while (play == True):
            if total_count != 0: print ("You have played:", total_count, "time(s)\nYou have won:",win_count,"time(s)\n")
            
            total_count +=1
            # Generates a random number which will be uses to define the outcome of the game
            random_number = random.randint(1,6)
            Dice_Face = ""

            #Promp the user for their guess 

            guess = input("Write your guess, which face will the dice land on?\n1, 2, 3, 4, 5, 6\n")
            #Depending on the random number generated we define the correct Dice_Face
            
            if random_number == 1:
                Dice_Face = '1'
            elif random_number == 2:
                Dice_Face = '2'
            elif random_number == 3:
                Dice_Face = '3'
            elif random_number == 4:
                Dice_Face = '4'
            elif random_number == 5:
                Dice_Face = '5'
            elif random_number == 6:
                Dice_Face = '6'
            else:
                print("Error setting the outcome.")    

            #Cheat ;) (For debugging purposes :D)
            #Dice_Face = '4'

            #A little bit of drama

            for i in range (3,0,-1): time.sleep(1); print (i) 
            #Give the correct answer and the user guess
            time.sleep(0.5)
            print("\nDice landed on:", Dice_Face)
            time.sleep(0.5)
            print ("\nYour guess was...", guess)

            #Decide if the user won or not.
            time.sleep(0.5)
            if guess == Dice_Face:
                print ("\nYOU WON!") 
                win_count +=1  
            else: 
                print("\nYou lost :c")

            repeat = input("Another round? Y/N\n")

            if repeat == "N" or repeat == "n": play = False 

        print ("You played:", total_count, "time(s)\nYou won:",win_count,"time(s)\nBye! :D")