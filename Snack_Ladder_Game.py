import random

# This function is used for the Sncak 

def Snack(pn):
    
    if(pn == 17): 
        return 10
    elif(pn == 63):
        return 44
    elif(pn == 87):
        return 51
    elif(pn == 93):
        return 20
    elif(pn == 95):
        return 30
    elif(pn == 98):
        return 19
    else:
        return 0
        
# This function used for the Ladder 

def Ladder(pn):
    
    if(pn == 2): 
        return 36
    elif(pn == 4):
        return 10
    elif(pn == 21):
        return 21
    elif(pn == 28):
        return 56
    elif(pn == 53):
        return 14
    elif(pn == 72):
        return 19
    else:
        return 0


# Here we are create Snack Ladder Game 

player_1 = 1
player_2 = 1

player1Name = input("Enter Your Name(Player-1) : ")
player2Name = input("Enter Your Name(Player-2) : ")
print("\n")

# Here we are create the text file which is store the all positon of the player and also store who win the game

f = open("Game.txt" ,"a")

f.write("\n\n")
f.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
f.write(f"****** {player1Name} Vs {player2Name} ******")
f.write("\n")
f.write("-----------------------------------------------------------\n")
f.write(f"Turn   {player1Name}'s-Positions       {player2Name}'s-Positions")
f.write("\n")
f.write("-----------------------------------------------------------\n")
f.write("\n")

# Which is count the turn of the player
count=0

# Which is handle the Aboart game & who is win the game
flag = 0   

while(player_1 <= 100 and player_2 <= 100):
    
    # Here first term is a player-1
    print(f"##### {player1Name}'s turn #####")
    currentPos = player_1 # This is used for the handle the game when player_2 enter the wrong number for throw the dice
    num1 = (int)(input("Enter the number... 1 for Throw Dice & 0 for Aboard Game : "))
    if(num1 == 1):
        randnum1 = ((random.randrange(9))) % 6 +1  # random.randrange(9)  genrate the number between 1 to 9
        print(f"Player-1 dice number is {randnum1}")
        player_1 = player_1 + randnum1
        val1f=player_1
        print(f"Now palyer-1 position is {player_1}")
        player_1 = player_1 - Snack(player_1)
        if(player_1 != val1f):
            print(f"After Snack Efect position is {player_1}")
        val1h = player_1
        player_1 = player_1 + Ladder(player_1)
        if(player_1 != val1h):
            print(f"After Ladder Efect position is  {player_1}")
    elif(num1 == 0):
        flag=-1
        break
    else:
        print("Pls Throw Dice in right a way !")
        print("\n---------------------------------------------------------------\n")
        continue
        
    # Here first term is a player-2
    print(f"##### {player2Name}'s turn #####")
    num2 = (int)(input("Enter the number... 1 for Throw Dice & 0 for Aboard Game : "))
    if(num2 == 1):
        randnum2 = ((random.randrange(9))) % 6 +1
        print(f"Player-2 dice number is {randnum2}" )
        player_2 = player_2 + randnum2
        val2f =player_2
        print(f"Now palyer-2 position is {player_2}")
        player_2 = player_2 - Snack(player_2)
        if(player_2 != val2f):
            print(f"****** After Snack Efect position is {player_2}")
        val2h=player_2
        player_2 = player_2 + Ladder(player_2)
        if(player_2 != val2h):
            print(f"******After Ladder Efect position is  {player_2}")
    elif(num2 == 0):
        flag = -2
        break
    else:
        print("Pls Throw Dice in right a way !")
        player_1 = currentPos  # Here we are Discarded all the operation on player_1 positon due to player_2 wrong number enter
        print("\n---------------------------------------------------------------\n")
        continue
    
    currentPos = player_1 # After complete both turn we are add the palyer current postion 
    count= count + 1
    
    if((player_1>=1 and player_1<=9) and (player_2>=1 and player_2<=9)):
        f.write(f" {count}            0{player_1}                        0{player_2}")
    elif(player_1>=1 and player_1<=9):
        f.write(f" {count}            0{player_1}                        {player_2}")
    elif(player_2>=1 and player_2<=9):
        f.write(f" {count}            {player_1}                         0{player_2}")
    else:
        f.write(f" {count}            {player_1}                         {player_2}")  
    f.write("\n")
        
    # Here we are check the who is win the game 
    if(player_1 >= 100):
        print("\n---------------------------------------------------------------------------\n")
        print("Player-1 Won the Game")
        print("\n---------------------------------------------------------------------------\n")
        flag=1
        break
    elif(player_2 >= 100):
        print("\n---------------------------------------------------------------------------\n")
        print("Player-2 Won the Game")
        print("\n---------------------------------------------------------------------------\n")
        flag=2
        break
        
    print("\n---------------------------------------------------------------\n")

# This is used for the writ the End result of the game into the text file 
if(flag==-1):
    f.write("-----------------------------------------------------------\n")
    f.write(f"               Aboart The Game By {player1Name}")
    f.write("\n")
    f.write("-----------------------------------------------------------\n")  
elif(flag==-2):
    f.write("-----------------------------------------------------------\n")
    f.write(f"               Aboart The Game By {player2Name}")
    f.write("\n")
    f.write("-----------------------------------------------------------\n")
elif(flag==1):
    f.write("-----------------------------------------------------------\n")
    f.write(f"               {player1Name} Won The Game")
    f.write("\n")
    f.write("-----------------------------------------------------------\n")
elif(flag==2):
    f.write("-----------------------------------------------------------\n")
    f.write(f"               {player2Name} Won The Game")
    f.write("\n")
    f.write("-----------------------------------------------------------\n")   
else:
    f.write("-----------------------------------------------------------\n")
    f.write(f"                        Error         ")           
    f.write("\n")
    f.write("-----------------------------------------------------------\n")
