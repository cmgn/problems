import ctypes
import operator
import collections
import sys

# times out sadly

variables = collections.defaultdict(int)
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
    "<>": operator.ne,
    "=": operator.eq,
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
}


def arithmetic_expression(x, op=None, y=None):
    x = evaluate_value(x)
    if y is None:
        return ctypes.c_int(x).value
    else:
        y = evaluate_value(y)
        return ctypes.c_int(operators[op](x, y)).value


def evaluate_value(x):
    if x.isdigit():
        return int(x)
    elif x.startswith("\""):
        return x[1:-1]
    else:
        return variables[x]


def boolean_expression(x, op, y):
    return operators[op](evaluate_value(x), evaluate_value(y))


def main():
    jump_labels = {}
    sorted_instructions = []
    for instruction in sys.stdin:
        split = instruction.split()
        label = split[0]
        rest = split[1:]
        sorted_instructions.append((label, rest))

    sorted_instructions.sort(key=lambda s: int(s[0]))
    for index, instruction in enumerate(sorted_instructions):
        jump_labels[instruction[0]] = index

    line_no = 0
    while line_no < len(sorted_instructions):
        space_splitted_tokens = sorted_instructions[line_no][1]
        if space_splitted_tokens[0] == "LET":
            variables[space_splitted_tokens[1]] = arithmetic_expression(*space_splitted_tokens[3:])
        elif space_splitted_tokens[0] == "IF":
            condition = space_splitted_tokens[1:-3]
            if boolean_expression(*condition):
                line_no = jump_labels[space_splitted_tokens[-1]]
                continue
        elif space_splitted_tokens[0] == "PRINT":
            sys.stdout.write(str(evaluate_value(" ".join(space_splitted_tokens[1:]))))
        elif space_splitted_tokens[0] == "PRINTLN":
            sys.stdout.write(str(evaluate_value(" ".join(space_splitted_tokens[1:]))) + "\n")
        line_no += 1


if __name__ == '__main__':
    main()
