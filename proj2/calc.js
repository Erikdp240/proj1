// "node calc.js op int int"
// args[2] = op
// args[3] = int
// args[4] = int

function do_op (op, i1, i2) {
  switch (op) {
    case "add":
      return [i1 + i2, "+"];
    case "sub":
      return [i1 - i2, "-"];
    case "mul":
      return [i1 * i2, "*"];
    case "div":
      return [i1 / i2, "/"];
    case "gt":
      if (i1 > i2) return [true, ">"];
      else return [false, ">"];
    case "ge":
      if (i1 >= i2) return [true, ">="];
      else return [false, ">="];
    case "lt":
      if (i1 < i2) return [true, "<"];
      else return [false, "<"];
    case "le":
      if (i1 <= i2) return [true, "<="];
      else return [false, "<="];
    case "eq":
      if (i1 == i2) return [true, "="];
      else return [false, "="];
    case "neq":
      if (i1 != i2) return [true, "!="];
      else return [false, "!="];
    default:
      throw "ERROR: The operation is invalid";
  }
  
}

const args = process.argv;

op = args[2];
i1 = parseInt(args[3]);
i2 = parseInt(args[4]);

[result, op] = do_op(op, i1, i2);

console.log(`${i1} ${op} ${i2} = ${result}`);