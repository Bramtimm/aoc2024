
def advent_of_code19a(input_str: str) -> int:

    # preprocessing
    towels, combinations = input_str.split('\n\n')  
    towels = towels.split(', ')
    combinations = combinations.split('\n')

    # combination mapping
    rest_combinations = [is_valid(towels, combination) for combination in combinations]

    
    return sum(rest_combinations)
 

def is_valid(towels: list[str], combination: str, cache: dict[str, bool] = None) -> bool:

    if cache is None:
        cache = {}

    if combination in cache:
        return cache[combination]
        
    if len(combination)==0:
        return True
    
    for towel in towels:
        if combination.startswith(towel):
            combi_remprefix = combination.removeprefix(towel)
            if is_valid(towels, combi_remprefix, cache):
                    cache[combination] = True
                    return True
    
    cache[combination] = False
        
    return False


if __name__ == "__main__":
     
    test_input="""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

    test_output = advent_of_code19a(test_input)
    print(f"{test_output}")
    assert test_output == 6

    with open("../data/advent_of_code19/puzzle_input.txt", 'r') as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code19a(puzzle_input)
    print(f"{puzzle_output}")  