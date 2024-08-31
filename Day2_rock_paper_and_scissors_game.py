#Here is a rock, paper and scissors game
import random
options=["rock", "paper", "scissors"]

print("Welcome to the grand game of Rock , Paper and Scissors! ")
print("Type exit to leave the game if you don't dare: ")

your_score=0
computer_score=0
winning_score=3
while your_score < winning_score and computer_score < winning_score:

    your_choice=input("Enter your choice (Rock, Paper or Scissors): ").lower()
    if your_choice=="exit":
        break
    if your_choice not in options:
        print("Invalid input! please enter the correct option: ")
        continue
    #computer choice
    computer_choice=random.choice(options)
    print("The computer chose: "+computer_choice)

    #judging
    if your_choice==computer_choice:
        print("Its a tie!")
 
    elif (your_choice=="rock" and computer_choice=="scissors")or\
          (your_choice == "scissors" and computer_choice == "paper")or\
            (your_choice=="paper" and computer_choice=="rock"):
        print("Oh, look you won! ")
        your_score+=1
    else:
        print("You Lost this one!")    
        computer_score+=1

#final scores
print("You: "+str(your_score)+" Computer_score: "+str(computer_score))

#winner announcement

if your_score==winning_score:
    print("Oh great, you won!")
elif computer_score==winning_score:
    print("The machine prevails")



