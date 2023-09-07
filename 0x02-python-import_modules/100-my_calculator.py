#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

ac = len(sys.argv)

if ac != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

else:
    operator = sys.argv[2]
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    else:
        a, b = int(sys.argv[1]), int(sys.argv[3])
        if (operator == '+'):
            res = (add(a, b))
        elif (operator == '-'):
            res = (sub(a, b))
        elif (operator == '*'):
            res = (mul(a, b))
        elif (operator == '/'):
            res = (div(a, b))
print("{} {} {} = {}".format(a, operator, b, res))
sys.exit(0)
