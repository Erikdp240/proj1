import random as r
import sys

def roll_dice():
  dice1 = r.randint(1, 6)
  dice2 = r.randint(1,6)

  die = (dice1, dice2)

  print(die)

def main():

  while True:
    answer = input("Roll the dice? (y/n): ")

    if answer in ['n', 'N']:
      print("Thanks for playing!")
      sys.exit(1)
    elif answer in ['y', 'Y']:
      roll_dice()
    else:
      print("Invalid choice!")

if __name__ == '__main__':
  main()