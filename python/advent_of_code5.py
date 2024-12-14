from collections import defaultdict

def advent_of_code5a(ruleset: str, input: str):

    # make hashmap/dictionary for ruleset
    ruleset = ruleset.split('\n')
    ruleset = [rule.split('|') for rule in ruleset]

    rule_dict = defaultdict(list)
    [rule_dict[key].append(int(value)) for key, value in ruleset]

    input = input.split('\n')
    input = [line.split(',') for line in input]
    input = [list(map(int, line)) for line in input]

    # check mapping
    valid_ordering = [check_ruleset(rule_dict, line) for line in input]
    middle_values = [get_middle_value(x) for index, x in enumerate(input) if valid_ordering[index]]

    return sum(middle_values)

def advent_of_code5b(ruleset: str, input: str):

     # make hashmap/dictionary for ruleset
    ruleset = ruleset.split('\n')
    ruleset = [rule.split('|') for rule in ruleset]

    rule_dict = defaultdict(list)
    [rule_dict[key].append(int(value)) for key, value in ruleset]

    input = input.split('\n')
    input = [line.split(',') for line in input]
    input = [list(map(int, line)) for line in input]

    # check mapping
    valid_ordering = [check_ruleset(rule_dict, line) for line in input]
    correct_input_failed_ordering = [reorder_line(rule_dict, x) for index, x in enumerate(input) if not valid_ordering[index]]

    middle_values = [get_middle_value(x) for x in correct_input_failed_ordering]

    return sum(middle_values)



def get_middle_value(input_list: list[int]) -> int:
    middle_index = int((len(input_list)-1)/2)
    return input_list[middle_index]

def check_ruleset(rule_dict: dict, input: list[int]) -> bool:

    for index, element in enumerate(input):
        rule = rule_dict[str(element)]
        if  all(map(lambda x: x in rule, input[index+1:])):
            rule_output=True
        else:
            return False
    
    return rule_output

def reorder_line(rule_dict: dict, line: list[int]):
    
    for index, element in enumerate(line):
        rule = rule_dict[str(element)]

        if not all(map(lambda x: x in rule, line[index+1:])):
            line.remove(element)
            line.append(element)
            line = reorder_line(rule_dict, line)    
        else:
            line = line

    return line

if __name__ == "__main__":
    
    test_ruleset = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""
    
    test_input = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    test_output = advent_of_code5a(test_ruleset, test_input)
    print(f"{test_output}")
    assert test_output == 143

    with open("../data/advent_of_code5/puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_ruleset, puzzle_input = puzzle_input.split('\n\n')

    puzzle_output = advent_of_code5a(puzzle_ruleset, puzzle_input)
    print(f'the answer to advent_of_code4a is: {puzzle_output}')

    test_output = advent_of_code5b(test_ruleset, test_input)
    print(f"{test_output}")
    assert test_output == 123

    puzzle_output = advent_of_code5b(puzzle_ruleset, puzzle_input)
    print(f'the answer to advent_of_code4a is: {puzzle_output}')
