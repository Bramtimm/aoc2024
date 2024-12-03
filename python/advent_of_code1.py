from typing import List


def advent_of_code1(list_1: List[int], list_2: List[int]) -> int:
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    distance_list = [abs(sorted_list_1[x] - sorted_list_2[x]) for x in range(len(sorted_list_1))]

    distance = sum(distance_list)

    return distance

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
    # print(list_1)
    print(list_2)
    distance  = advent_of_code1(list_1, list_2)
    print(f"the distance of the two lists is: {distance}!")



# There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?
# // Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

# // Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

# // In the example list above, the pairs and distances would be as follows:

# // The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
# // The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
# // The third-smallest number in both lists is 3, so the distance between them is 0.
# // The next numbers to pair up are 3 and 4, a distance of 1.
# // The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
# // Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
# // To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

# // Your actual left and right lists contain many location IDs. What is the total distance between your lists?