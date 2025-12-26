from utils import read
from typing import List
import math
import operator

def solution_1():
  from pathlib import Path
  cwd = Path.from_uri(f"file://{__file__}").parent
  content = read.read_content(f"{cwd}/input")
  list_of_numbers: List[List[int]] = [[] for _ in range(len(content[0].split()))]
  list_of_operators: List[List] = [[] for _ in range(len(content[0].split()))]
  list_of_answers: List[float] = [0.0 for _ in range(len(content[0].split()))]
  for line_index, line in enumerate(content):
    items_in_line = line.split()
    for item_index, item in enumerate(items_in_line):
      if item.isdigit():
        list_of_numbers[item_index].append(int(item))
      else:
        match item:
          case '+':
            list_of_operators[item_index].append(operator.add)
            list_of_answers[item_index] = math.fsum(list_of_numbers[item_index])
          case '*':
            list_of_operators[item_index].append(operator.mul)
            list_of_answers[item_index] = math.prod(list_of_numbers[item_index])

  print(sum(list_of_answers))






  # Your solution code here

def main():
  solution_1()

if __name__ == "__main__":
  main()
