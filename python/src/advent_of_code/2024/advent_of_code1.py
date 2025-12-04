from typing import List


def advent_of_code1(list_1: List[int], list_2: List[int]) -> int:
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    distance_list = [abs(sorted_list_1[x] - sorted_list_2[x]) for x in range(len(sorted_list_1))]

    distance = sum(distance_list)

    return distance

def advent_of_code1b(list_1: List[int], list_2: List[int]) -> int:
    """ calculate similarity score"""

    similarity_list = [0] * len(list_1)

    for item in range(len(list_1)):
        for item_2 in range(len(list_2)):
            
            if list_1[item] == list_2[item_2]:
                similarity_list[item] += 1

    similarity = sum([list_1[item] * similarity_list[item] for item in range(len(list_1))])

    return similarity


if __name__ == "__main__":

    # test example
    distance = advent_of_code1(list_1 = [3, 4, 2, 1, 3, 3], list_2=[4, 3, 5, 3, 9, 3]) 
    assert distance == 11
    print(f"the distance of the two lists is: {distance}!")

    # get puzzle input through context manager
    with open("../data/advent_of_code1/puzzle_input.txt", "r") as f:
        f = [line.split() for line in f if line.strip()]
        list_1 = [int(line[0]) for line in f]
        list_2 = [int(line[1]) for line in f]
    
    distance  = advent_of_code1(list_1, list_2)
    print(f"the distance of the two lists is: {distance}!")

    # test example 2
    similarity_score = advent_of_code1b(list_1 = [3, 4, 2, 1, 3, 3], list_2=[4, 3, 5, 3, 9, 3]) 
    print(f"the similarity of the two lists is: {similarity_score}!")
    assert similarity_score == 31

    # puzzle input
    similarity_score = advent_of_code1b(list_1, list_2)
    print(f"the similarity of the two lists is: {similarity_score}!")

