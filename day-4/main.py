from functools import total_ordering
from dataclasses import dataclass
from typing import List, Tuple

def read_content(file_name: str = "input"):
  content = []
  with open(file=file_name,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content

@dataclass
class Coordinate:
  x: int
  y: int
  value: str

def get_adjacent_points(coordinate: Coordinate, matrix: List[List[Coordinate]]) -> List[Coordinate]:
  adjacent_points = [(coordinate.x + dx, coordinate.y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),(-1,-1),(-1,1),(1,-1),(1,1)]]
  return [Coordinate(x=point[0], y=point[1], value=matrix[point[0]][point[1]].value) for point in adjacent_points if point[0] >= 0 and point[0] < len(matrix) and point[1] >= 0 and point[1] < len(matrix[0])]

def get_can_be_fklfted_matrix(matrix: List[List[Coordinate]]) -> List[List[Coordinate]]:
  can_be_fklfted_matrix: List[List[Coordinate]] = []
  for line_index, line in enumerate(matrix):
    can_be_fklfted_line: List[Coordinate] = []
    for coordinate in line:
      if coordinate.value != "@":
        # if it is not a paper roll, skip it
        continue

      # if it is a paper roll, then calculate the number of adjacent points
      adjacent_points = get_adjacent_points(coordinate, matrix)
      no_of_adj_rolls = 0

      # check if adjacent points are paper rolls
      # if they are increment the count of adjacent paper rolls
      for point in adjacent_points:
        if point.value == "@":
          no_of_adj_rolls += 1

      # if the number of adjacent paper rolls is less than 4, then
      # the paper roll can be forklifted
      if no_of_adj_rolls < 4:
        can_be_fklfted_line.append(coordinate)
    can_be_fklfted_matrix.append(can_be_fklfted_line)

  return can_be_fklfted_matrix

def part1_solution(matrix: List[List[Coordinate]]):
  can_be_fklfted_matrix = get_can_be_fklfted_matrix(matrix)
  count = 0
  for line in can_be_fklfted_matrix:
    for coordinate in line:
      count += 1
  print("Count of forklifted paper rolls:", count)

def part2_solution(matrix: List[List[Coordinate]]):
  forklifting_done = False
  iteration = 0
  total_forklifted_count = 0
  while not forklifting_done:
    can_be_fklfted_matrix = get_can_be_fklfted_matrix(matrix)
    forklifted_count = 0
    for line in can_be_fklfted_matrix:
      for coordinate in line:
        matrix[coordinate.x][coordinate.y].value = "x"
        forklifted_count += 1

    print(f"Iteration: {iteration}, Forklifted count: {forklifted_count}")
    iteration += 1
    total_forklifted_count += forklifted_count
    forklifting_done = forklifted_count == 0

  for line in matrix:
    for coordinate in line:
      if coordinate.value == "x":
        coordinate.value = "."

  print("Final matrix:")
  for line in matrix:
    print("".join([coordinate.value for coordinate in line]))

  print("Total forklifted count:", total_forklifted_count)

if __name__ == "__main__":
  content = read_content()
  matrix: List[List[Coordinate]] = []
  for line_index, line in enumerate(content):
    line_list: List[Coordinate] = []
    for char_index, char in enumerate(line):
      coordinate = Coordinate(x=line_index, y=char_index, value=char)
      line_list.append(coordinate)
    matrix.append(line_list)

  # part1_solution(matrix)
  part2_solution(matrix)
