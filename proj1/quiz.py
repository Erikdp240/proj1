import time as t

class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

def question_type(typ):
  if typ == 'Science':
    q = [
      "What is the smallest unit of life?:\n(a) cell \n(b) inches \n(c) protons \n(d) brain \n\n",
      "What is the chemical formula for water?:\n(a) H2O \n(b) CO2 \n(c) NaCl \n(d) HO \n\n",
      "What is the powerhouse of a cell?:\n(a) membrane \n(b) skin cell \n(c) mitochondria \n(d) nucleus \n\n",
    ]
  else:
    q = [
      "What is x when 5 = 3x + 2?:\n(a) 1 \n(b) 2 \n(c) 3 \n(d) 4 \n\n",
      "What is 13 * 13?: \n(a) 144 \n(b) 169 \n(c) 26 \n(d) Not possible. \n\n",
      "What is the shape of y = x^2 called?: \n(a) Parabola \n(b) Smile \n(c) Frowny Face \n(d) Ellipse \n\n",
    ]

  return q

def introduction():
  print("You are about to take a quiz. But first I need some information")

  name = input("What is your full name: ")
  sid = input("What is your student ID: ")

  print(f"Welcome {name}! Student ID: {sid}")

  quiz_type = []
  while quiz_type not in ['Science', 'Math']:
    quiz_type = input("Which quiz are you taking (Science/Math): ")

  print(f"You are going to take a {quiz_type} quiz.")
  print("You are being transferred...")
  t.sleep(3)
  print("Done.\n")

  return quiz_type

def run_test(typ, questions):
  score = 0

  if typ == 'Science':
    qna = [
      Question(questions[0], 'a'),
      Question(questions[1], 'a'),
      Question(questions[2], 'a'),
    ]
  else:
    qna = [
      Question(questions[0], 'a'),
      Question(questions[1], 'b'),
      Question(questions[2], 'a'),
    ]

  for q in qna:
    ans = input(f"{q.prompt}Your answer: ")
    if ans == q.answer:
      score += 1

  print(f"Final score: {score} / 3")

def main():
  typ = introduction()
  questions = question_type(typ)

  run_test(typ, questions)

if __name__ == "__main__":
  main()