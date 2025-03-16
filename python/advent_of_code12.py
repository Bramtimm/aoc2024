def advent_of_code12a(input_str: str) -> int:
    return 0

if __name__=="__main__":
    
    test_input1 = """AAAA
BBCD
BBCC
EEEC"""

    test_result1 = advent_of_code12a(test_input1)
    assert test_result1==772

    test_input2 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

    test_result2 = advent_of_code12a(test_input2)
    assert test_result2==1930

    with open("../data/advent_of_code12/puzzle_input.txt", 'r') as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code12a(puzzle_input)
    print(f"puzzle_output is: {puzzle_output}")
    