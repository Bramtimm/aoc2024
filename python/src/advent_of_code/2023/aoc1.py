import re

def advent_of_code1a(puzzle_input: list[str], pattern=r"[0-9]") -> int:

    numbers = []
    for line in puzzle_input:
        digits = re.findall(pattern=pattern, string=line)
        
        digit = str(digits[0])+str(digits[-1])
        numbers.append(int(digit))

    return sum(numbers)

def advent_of_code1b(puzzle_input: list[str]) -> int:

    replace_dict={"one": "1",
                  "two": "2",
                  "three": "3",
                  "four": "4",
                  "five": "5",
                  "six": "6",
                  "seven": "7",
                  "eight": "8",
                  "nine": "9"}
    
    pattern = re.compile(r"[1-9]|one|two|three|four|five|six|seven|eight|nine")
    numbers = []

    for line in puzzle_input:
        digits = []
        i = 0
        while i < len(line):
            match = pattern.match(line, i)
            if match:
                val = match.group(0)
                digits.append(replace_dict.get(val, val))
                i += 1
            else:
                i += 1
            
        if digits:
            number = int(digits[0] + digits[-1])
            numbers.append(number)
            
    return sum(numbers)
    


if __name__ == "__main__":
    test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    test_input = test_input.split("\n")

    test_output = advent_of_code1a(test_input)
    print(f"the test answer to aoc1a is: {test_output}")
    assert test_output == 142

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2023/advent_of_code1/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.readlines()

    puzzle_output = advent_of_code1a(puzzle_input)
    print(f"the answer to aoc1a is: {puzzle_output}")

    test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    test_input = test_input.split("\n")

    test_output = advent_of_code1b(test_input)
    print(f"the test answer to aoc1b is: {test_output}")
    assert test_output == 281

    puzzle_output = advent_of_code1b(puzzle_input)
    print(f"the answer to aoc1b is: {puzzle_output}")
