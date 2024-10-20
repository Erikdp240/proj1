# Calculator that works through terminal
# Should be run as "python calc.py op int int"
# Operations accepted - add, sub, mul, div
# This calculator also does comparisons between the two ints given in command line
# Comparisons accepted - gt, ge, le, lt, eq, neq
import sys

def do_op(op, i1, i2):
  if op == 'add':
    return i1 + i2, '+'
  elif op == 'sub':
    return i1 - i2, '-'
  elif op == 'mul':
    return i1 * i2, '*'
  elif op == 'div':
    return i1 / i2, '/'
  elif op == 'gt':
    if i1 > i2:
      return True, '>'
    else:
      return False, '>'
  elif op == 'ge':
    if i1 >= i2:
      return True, '>='
    else:
      return False, '>='
  elif op == 'lt':
    if i1 < i2:
      return True, '<'
    else:
      return False, '<'
  elif op == 'le':
    if i1 <= i2:
      return True, '<='
    else:
      return False, '<='
  elif op == 'eq':
    if i1 == i2:
      return True, '='
    else:
      return False, '='
  elif op == 'neq':
    if i1 != i2:
      return True, '!='
    else:
      return False, '!='

def main():
  op = sys.argv[1]
  i1 = int(sys.argv[2])
  i2 = int(sys.argv[3])

  if op not in ['add', 'sub', 'mul', 'div', 'gt', 'ge', 'le', 'lt', 'eq', 'neq']:
    print("ERROR: The operation argument is invalid.")
    sys.exit(1)

  result, op = do_op(op, i1, i2)

  print(f"{i1} {op} {i2} = {result}")

if __name__ == "__main__":
  main()