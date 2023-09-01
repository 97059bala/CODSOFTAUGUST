import random
options=("rock","paper","scissors")

playing=True 
while playing:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter a choice(Rock,Paper,Scissors):")
    print(f"Player:{player}")
    print(f"computer:{computer}")
    if player==computer:
        print("It's a Tie!")
    elif player=="rock" and computer=="scissors":
        print("You Win!")
    elif  player=="paper" and computer=="rock":
        print("You Win!")
    elif player=="scissors" and computer=="paper":
        print("You Win!")
    else:
        print("You lose!")
    play_again=input("Play Again?(y/n)").lower()
    if not play_again=="y":
        playing=False
print("Thanks for playing!!")