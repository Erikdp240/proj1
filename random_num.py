import random as r

def main():
  num = r.randint(1,100)

  while True:
    try:
      answer = int(input('Guess the number between 1-100: '))

      if answer > num:
        print("Too high")
      elif answer < num:
        print("Too low")
      elif answer == num:
        print("Congratulations! You guessed the number.")
        break
    except ValueError:
      print("Please enter a valid number!")
      
if __name__ == '__main__':
  main()