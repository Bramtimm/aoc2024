from typing import List

def advent_of_code2a(report_matrix: List[List[int]]) -> int:

    safe_reports = 0
    
    for row in report_matrix:
        # if The levels are either all increasing or all decreasing.
        if row == sorted(row) or row == sorted(row, reverse=True):
            # Any two adjacent levels differ by at least one and at most three.
            if all(abs(row[item+1]-row[item]) in [1,2,3] for item in range(len(row)-1)):
                safe_reports+=1
        
    return safe_reports  

if __name__ == "__main__":

    # test example
    test_input = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]]

    safe_reports = advent_of_code2a(test_input)
    print(f"there are {safe_reports} safe reports in the test!")
    assert safe_reports == 2 

    # puzzle input 2a
    with open("../data/advent_of_code2/puzzle_input.txt", "r") as f:
        report_matrix = [line.split() for line in f if line.strip()]
        report_matrix = [list(map(int, line)) for line in report_matrix]
        
    safe_reports = advent_of_code2a(report_matrix)
    print(f"there are {safe_reports} safe reports in the test!")