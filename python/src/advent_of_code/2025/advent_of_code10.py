import re

def advent_of_code10(patterns: list[tuple]) -> int:
    
    minimal_presses = 0
    for pattern in patterns:
        indicator, buttons, joltage_requirement = pattern
        indicator = unpack_indicator_as_bool(indicator)
        buttons = unpack_buttons(buttons)

        minimal_presses += determine_minimum_presses(indicator, buttons)


def determine_minimum_presses(indicator: list[int], buttons: list[list[int]]) -> int:
    pass


def unpack_indicator_as_bool(indicator: str) -> list[int]:
    pattern = re.compile(r"\[(.+)\]")
    indicator = list(pattern.match(indicator).group(1))
    indicator = [0 if ele == "." else 1 for ele in indicator]
    
    return indicator

def unpack_buttons(buttons: str) -> list[list[int]]:
    buttons = buttons.strip()
    pattern = r"\(([^)]*)\)"
    buttons = re.findall(pattern, buttons)

    buttons = [list(map(int,button.split(','))) for button in buttons]

    return buttons
    

if __name__ == "__main__":
    test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

    test_indicators = test_input.splitlines()
    pattern_to_capture_groups = re.compile(r"(\[.+])(.+\) )(\{.+\})")
    
    patterns = [pattern_to_capture_groups.match(indicator).group(1,2,3) for indicator in test_indicators]


    test_output = advent_of_code10(patterns=patterns)
    print(f"the test answer to aoc10a is: {test_output}")

    assert test_output == 40

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code8/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_grid = puzzle_input.splitlines()
        puzzle_grid = [list(map(int, line.split(","))) for line in puzzle_grid]

    puzzle_output = advent_of_code8a(puzzle_grid, num_connections=1000)
    print(f"the answer to aoc8a is: {puzzle_output}")

    test_output = advent_of_code8b(test_grid)
    print(f"the test answer to aoc10b is: {test_output}")
    assert test_output == 25272

    puzzle_output = advent_of_code8b(puzzle_grid)
    print(f"the answer to aoc8b is: {puzzle_output}")
