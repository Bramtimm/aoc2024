from itertools import product
from operator import add, mul

def advent_of_code_7a(input_str: str) -> int:

    equations = input_str.splitlines()

    equations = [equation.split(":") for equation in equations]

    values = [find_calibirations(equation) for equation in equations]

    return sum(values)


def find_calibirations(equation: list[str], operators = [add, mul]) -> int:

    if len(equation) > 2:
        return ValueError("len should not be longer than 2 of list")
    
    value, input = equation

    input = list(map(int, input.split()))

    possible_operands = list(product(operators, repeat=len(input)-1))

    possible_values = [apply_operands(operands, input) for operands in possible_operands]

    if int(value) in possible_values:
        return int(value)
    else:
        return 0
   

def apply_operands(operands: list, input: list[str]) -> int:
    result = input[0]
    for i, op in enumerate(operands):
        result=op(result, input[i+1])
    return result
    

if __name__ == "__main__":
    
    test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

    test_output = advent_of_code_7a(test_input)
    print(f"{test_output}")
    assert test_output == 3749

    with open("../data/advent_of_code7/puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code_7a(puzzle_input)
    print(f"{puzzle_output}")
