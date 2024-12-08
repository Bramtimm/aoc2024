import re

def advent_of_code3a(input_str: str) -> int:

    mul_pairs = re.findall(pattern = r"mul\((\d{1,3}),(\d{1,3})\)", string=input_str)

    x = [int(pair[0]) * int(pair[1]) for pair in mul_pairs]

    return sum(x)

def advent_of_code3b(input_str: str) -> int:

    # split on do
    input_str_splitted = re.split(pattern= r"do\(\)", input_str)

    mul = []
    for sub_str in input_str_splitted:

        # take first element as we aren't interested in any sub_str after mul_str
        mul_str = re.split(r"don't\(\)", sub_str)
        mul.append(advent_of_code3a(mul_str[0]))

    return sum(mul)


if __name__ ==  "__main__":

    test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    test_output_3a = advent_of_code3a(test_input)
    print(f"the added multiplications of the input is: {test_output_3a}!")
    assert test_output_3a == 161

    with open("../data/advent_of_code3/puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_output_3a = advent_of_code3a(puzzle_input)
    print(f"the added multiplications of the input is: {puzzle_output_3a}!")

    # 3B
    test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    test_output_3b = advent_of_code3b(test_input)
    print(f"the added multiplications of the input is: {test_output_3b}!")
    assert test_output_3b == 48

    puzzle_output_3b = advent_of_code3b(puzzle_input)
    print(f"the added multiplications of the input is: {puzzle_output_3b}!")
