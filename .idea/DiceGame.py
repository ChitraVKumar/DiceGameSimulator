import random

def main():
    playerA = 0
    playerB = 0
    Rounds =1
    TotalPlayerAWins = 0
    TotalPlayerBWins = 0

    while Rounds != 6:
        print("Round No: " + str(Rounds))
        playerA = roll()
        print("Player A rolls: " +str(playerA))
        playerB = roll()
        print("player B rolls:" +str(playerB))

        if playerA == playerB:
            print("Its a draw\n")
        elif playerA > playerB:
            TotalPlayerAWins = TotalPlayerAWins + 1
            print("Player A wins\n")
        else:
            TotalPlayerBWins = TotalPlayerBWins + 1
            print("Player B wins\n")

        Rounds = Rounds + 1

    if TotalPlayerAWins == TotalPlayerBWins:
        print("Overall its a Draw\n")
    elif TotalPlayerAWins > TotalPlayerBWins:
        print("Player A wins\nNo of Rounds won: " +str(TotalPlayerAWins) +"/"+ str(Rounds-1))
    else:
        print("Player B wins\nNo of Rounds won: " +str(TotalPlayerBWins) +"/"+ str(Rounds-1))

def roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()