player1 = raw_input ("Player 1 choose Rock, Paper or Scissor?")
while player1 not in ['rock', 'paper', 'scissors']:
    player1 = raw_input("Player 1 choose again Rock, Paper or Scissors?")

player2 = raw_input ("Player 2 choose Rock, Paper or Scissor?")
while player2 not in ['rock', 'paper', 'scissors']:
    player2 = raw_input("Player 2 choose again Rock, Paper or Scissors?")

if (player1 == 'rock' and player2 == 'scissors'):
    print "Rock beats Scissors Player 1 wins."

elif (player1 == 'rock' and player2 == 'rock'):
    print "Rock vs Rock It's a Draw"

elif (player1 == 'scissors' and player2 == 'paper'):
    print "Scissors beats Paper Player 1 wins."

elif (player2 == 'scissors' and player2 == 'scissors'):
    print "Scissors vs Scissors It's a Draw"

elif (player1 == 'paper' and player2 == 'paper'):
    print "Paper vs Paper It's a Draw"

elif (player1 == 'paper' and player2 == 'scissors'):
    print "Scissors beats Paper Player 2 wins."

elif (player1 == 'rock'and player2 == 'paper'):
    print "Paper beats Rock Player 2 wins."

elif (player1 == 'paper' and player2 == 'rock'):
    print "Paper beats Rock Player 1 wins."

elif (player1 == 'scissors' and player2 == 'rock'):
    print "Rock beats Scissors Player 2 wins."
