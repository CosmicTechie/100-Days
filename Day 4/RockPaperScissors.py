import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
position=["rock","paper","scissors"]

comp=[0,1,2]
computer = random.choice(comp)

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

if user<3:
  if position[user]=="rock":
    print(rock)
  elif position[user]=="paper":
    print(paper)
  elif position[user]=="scissors":
    print(scissors)
  else:
    print("Not Valid")

  print("\n\nComputer Chooses:")
  if position[computer]=="rock":
    print(rock)
  elif position[computer]=="paper":
    print(paper)
  elif position[computer]=="scissors":
    print(scissors)


  if user==computer:
    print("It's Draw.")
  elif user==0 and computer==2:
    print("You Win.")
  elif computer==0 and user==2:
    print("Computer Win.")
  elif user>computer:
    print("You Win.")
  else:
    print("You Lose.")

else:
  print("Not a Valid Option.")
