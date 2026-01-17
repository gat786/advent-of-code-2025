from pathlib import Path
from dataclasses import dataclass
from utils import read
from typing import List

cwd = Path.from_uri(f"file://{__file__}").parent

def solution_1(content: List[str]):
  solved_matrix = current_matrix = [list(x) for x in content]
  split_count = 0

  for line_index, line in enumerate(current_matrix):
    if line_index == 0:
      start_index = current_matrix[line_index].index("S")
      solved_matrix[0+1][start_index] = "|"
    elif line_index > 0 and line_index % 2 == 0:
      prev_line = solved_matrix[line_index - 1]

      for item_index, item in enumerate(line):
        above_item = prev_line[item_index] if len(prev_line) > 0 else "."
        if above_item == "|" and item == "^":
          solved_matrix[line_index][item_index - 1] = solved_matrix[line_index][item_index + 1] = "|"
          solved_matrix[line_index + 1][item_index - 1] = solved_matrix[line_index + 1][item_index + 1] = "|"
          split_count += 1
        if above_item == "|" and item == ".":
          solved_matrix[line_index][item_index] = "|"
          solved_matrix[line_index + 1][item_index] = "|"

  with open(f"{cwd}/output-part1.md", "w") as fp:
    fp.write("```\n")
    for line in solved_matrix:
      fp.write(f"{"".join(line)}\n")
    fp.write("```\n")

  print(split_count)

  return split_count

def solution_2(content: List[str]):
  current_matrix = [list(x) for x in content]
  solved_matrix: List[List[int]] = [[0] * len(x) for x in content]
  split_count = 0

  for line_index, line in enumerate(current_matrix):
    if line_index == 0:
      start_index = current_matrix[line_index].index("S")
      solved_matrix[0+1][start_index] = 1
    elif line_index > 0 and line_index % 2 == 0:
      prev_line = solved_matrix[line_index - 1]

      for item_index, item in enumerate(line):
        above_item = prev_line[item_index] if len(prev_line) > 0 else 0
        if above_item > 0 and item == "^":
          solved_matrix[line_index][item_index - 1] += above_item
          solved_matrix[line_index][item_index + 1] += above_item
          solved_matrix[line_index + 1][item_index - 1] += above_item
          solved_matrix[line_index + 1][item_index + 1] += above_item
          split_count += 1

        if above_item > 0 and item == ".":
          solved_matrix[line_index][item_index] = above_item
          solved_matrix[line_index + 1][item_index] = above_item

  with open(f"{cwd}/output-part2.md", "w") as fp:
    fp.write("```\n")
    for line in solved_matrix:
      fp.write(f"{"".join([str(x) for x in line])}\n")
    fp.write("```\n")

  solution = sum([j for i in solved_matrix for j in i])
  print(solution)

  return solution

def main():
  content = read.read_content(f"{cwd}/input")
  solution_1(content=content)
  solution_2(content=content)

if __name__ == "__main__":
  main()
