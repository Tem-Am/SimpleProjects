from pickle import TRUE
from tabnanny import check

# center() is for getting space betweeen words, and it goes from left to right. 
# Exercise two: Working on cheking valid websire
#website = input('please enter your website: ')
#checking = website.find("http")
#if checking == 0:
#    print('Valid websire')
#elif checking != 0: 
#    print('Not valid website')

# Rock Paper Scissor:
win = False
numOfGame = 1
Player1win = 0
Player2win = 0
winner  = ""
while numOfGame <= 7: 
    print(str(numOfGame) + " game: ")
    win = False
    while win != True:
        player1 = input('Player 1, it is your turn: ')
        player2 = input('player 2, it is your time: ')
        if player1 == "rock" and player2 == "scissor":
            win = True
            winner = "Player1"
            Player1win = Player1win +1
        if player1 == "paper" and player2 == "rock":
            win = True
            winner = "Player1"
            Player1win = Player1win +1
        if player1 == "scissor" and player2 == "paper":
            win  = True
            winner = "Player1"
            Player1win = Player1win +1
        if player2 == "rock" and player1 == "scissor":
            win = True
            winner = "Player2"
            Player2win = Player2win +1
        if player2 == "paper" and player1 == "rock":
            win = True
            winner = "Player2"
            Player2win = Player2win +1
        if player2 == "scissor" and player1 == "paper":
            win = True
            winner = "Player2"
            Player2win = Player2win +1
        elif player1 == "scissor" and player2 == "scissor":
            print('None of player did not win. Try again: ')
        elif player1 == "rock" and player2 == "rock":
            print('None of player did not win. Try again: ')
        elif player1 == "paper" and player2 == "paper":
            print('None of player did not win. Try again: ')
    numOfGame = numOfGame + 1

print('The player 1 win ' + str(Player1win) + ' time. The player 2 win ' + str(Player2win) + " time")