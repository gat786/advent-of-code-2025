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

if __name__ == "__main__":
  content = read_content()
  matrix: List[List[Coordinate]] = []
  for line_index, line in enumerate(content):
    line_list: List[Coordinate] = []
    for char_index, char in enumerate(line):
      coordinate = Coordinate(x=line_index, y=char_index, value=char)
      line_list.append(coordinate)
    matrix.append(line_list)

  can_be_fklfted_cnt = 0
  for line in matrix:
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
        can_be_fklfted_cnt += 1

  print(can_be_fklfted_cnt)
