# Calculator that works through terminal
# Should be run as "python calc.py op int int"
# Operations accepted - add, sub, mul, div
# This calculator also does comparisons between the two ints given in command line
# Comparisons accepted - gt, ge, le, lt, eq, neq
import sys

def do_op(op, i1, i2):
  if op == 'add':
    result = i1 + i2
  elif op == 'sub':
    result = i1 - i2
  elif op == 'mul':
    result = i1 * i2
  elif op == 'div':
    result = i1 / i2
  elif op == 'gt':
    result = True if i1 > i2 else False
  elif op == 'ge':
    result = True if i1 >= i2 else False
  elif op == 'lt':
    result = True if i1 < i2 else False
  elif op == 'le':
    result = True if i1 <= i2 else False
  elif op == 'eq':
    result = True if i1 == i2 else False
  elif op == 'neq':
    result = True if i1 != i2 else False

  return result

def main():
  op = sys.argv[1]
  i1 = int(sys.argv[2])
  i2 = int(sys.argv[3])

  if op not in ['add', 'sub', 'mul', 'div', 'gt', 'ge', 'le', 'lt', 'eq', 'neq']:
    print("ERROR: The operation argument is invalid.")
    sys.exit(1)

  result = do_op(op, i1, i2)

  print(f"{i1} {op} {i2} = {result}")

if __name__ == "__main__":
  main()