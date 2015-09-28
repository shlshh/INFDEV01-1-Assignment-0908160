player1 = raw_input ("Player 1 choose Rock, Paper, Scissors, Lizard or Spock?")
while player1 not in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
    player1 = raw_input("Player 1 choose again Rock, Paper, Scissors, Lizard or Spock?")

player2 = raw_input ("Player 2 choose Rock, Paper, Scissors, Lizard or Spock?")
while player2 not in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
    player2 = raw_input("Player 2 choose again Rock, Paper, Scissors, Lizard or Spock?")

if (player1 == 'rock' and player2 == 'scissors'):
    print "Rock crushes Scissors Player 1 wins."

elif (player1 == 'rock' and player2 == 'rock'):
    print "Rock vs Rock It's a Draw"

elif (player1 == 'scissors' and player2 == 'paper'):
    print "Scissors beats Paper Player 1 wins."

elif (player2 == 'scissors' and player2 == 'scissors'):
    print "Scissors vs Scissors It's a Draw"

elif (player1 == 'paper' and player2 == 'paper'):
    print "Paper vs Paper It's a Draw"

elif (player1 == 'paper' and player2 == 'scissors'):
    print "Scissors cuts Paper Player 2 wins."

elif (player1 == 'rock'and player2 == 'paper'):
    print "Paper covers Rock Player 2 wins."

elif (player1 == 'paper' and player2 == 'rock'):
    print "Paper covers Rock Player 1 wins."

elif (player1 == 'scissors' and player2 == 'rock'):
    print "Rock crushes Scissors Player 2 wins."

elif (player1 == 'lizard' and player2 == 'rock'):
    print "Rock crushes Lizard Player 2 wins."

elif (player1 == 'rock' and player2 == 'lizard'):
    print "Rock crushes Lizard Player 1 wins."

elif (player1 == 'lizard' and player2 == 'spock'):
    print "Lizard poisons Spock Player 1 wins."

elif (player1 == 'spock' and player2 == 'lizard'):
    print "Lizard poisons Spock Player 2 wins."

elif (player1 == 'spock' and player2 == 'scissors'):
    print "Spock smashes Scissors Player 1 wins."

elif (player1 == 'scissors' and player2 == 'spock'):
    print "Spock smashes Scissors Player 2 wins."

elif (player1 == 'scissors' and player2 == 'lizard'):
    print "Scissors decapitate Lizard Player 1 wins."

elif (player1 == 'lizard' and player2 == 'scissors'):
    print "Scissors decapitate Lizard Player 2 wins."

elif (player1 == 'lizard' and player2 == 'paper'):
    print "Lizard eats Paper Player 1 wins."

elif (player1 == 'paper' and player2 == 'lizard'):
    print "Lizard eats Paper Player 2 wins."

elif (player1 == 'paper' and player2 == 'spock'):
    print "Paper disproves Spock Player 1 wins."

elif (player1 == 'spock' and player2 == 'paper'):
    print "Paper disproves Spock Player 2 wins."

elif (player1 == 'spock' and player2 == 'rock'):
    print "Spock vaporizes Rock Player 1 wins."

elif (player1 == 'rock' and player2 == 'spock'):
    print "Spock vaporizes Rock Player 2 wins."

elif (player1 == 'lizard' and player2 == 'lizard'):
    print "Lizard vs Lizard It's a Draw"

elif (player1 == 'spock' and player2 == 'spock'):
    print "Spock vs Spock It's a Draw"