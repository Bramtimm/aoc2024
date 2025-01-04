from functools import cache

def advent_of_code11a(input_str: str, blinks: int) -> int:

    input_list = [int(element) for element in input_str.split(" ")]
    
    for _ in range(0, blinks):
        input_list = blink_ruleset(input_list)

    return len(input_list)

def blink_ruleset(input_list: list[int]) -> list[int]:
    
    output_list = []
    
    for element in input_list:
        if element == 0:
            output_list.append(1)
        elif len(str(element))%2 == 0:
            len_element = len(str(element))
            first_stone = int(str(element)[0:(len_element//2)])
            second_stone = int(str(element)[(len_element//2):len_element])
            output_list.append(first_stone)
            output_list.append(second_stone)
        else:
            output_list.append(element * 2024)
    return output_list

@cache
def blink_element(element: int, steps:int) -> int:

    if steps==0: 
        return 1
    elif element==0:
        return blink_element(1, steps-1)
    elif len(str(element))%2 == 0:
        len_element = len(str(element))
        first_element = int(str(element)[0:(len_element//2)])
        second_element = int(str(element)[(len_element//2):len_element])
        return blink_element(first_element, steps-1) + blink_element(second_element, steps-1) 
    else:
        return blink_element(element*2024, steps-1)
    

def advent_of_code11b(input_str: str, blinks: int) -> int:

    input_list = [int(element) for element in input_str.split(" ")]

    output_len = 0
    for element in input_list:
        output_len += blink_element(element, blinks)

    return output_len
            
        



if __name__ == "__main__":

    test_input = "125 17"
    test_output = advent_of_code11a(test_input, blinks=25)
    print(f"{test_output}")
    assert test_output == 55312 

    with open("../data/advent_of_code11/puzzle_input.txt", 'r') as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code11a(puzzle_input, blinks=25)
    print(f"{puzzle_output}")

    puzzle_output = advent_of_code11b(puzzle_input, blinks=75)
    print(f"{puzzle_output}")

