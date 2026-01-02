from utils import read
from typing import List
import math
import operator

def solution_1(content: List[str]):
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

  sol1_sum = int(sum(list_of_answers))
  print(f"Solution 1: {sol1_sum}")
  return sol1_sum

def solution_2(content: List[str]):
  list_of_answers = []
  num_lines = [x for x in content[:-1]]
  ops_line = content[-1]

  nums_list = []
  ops_list = []

  for char_index, char in enumerate(ops_line):
    number = "".join([x[char_index] for x in num_lines])
    if char != " ":
      ops_list.append(char)
      nums_list.append([int(number)])
      continue

    if len(number.strip()) > 0:
      curr_operator_index = len(ops_list) - 1
      nums_list[len(ops_list) - 1].append(int(number))

  for oper_index, oper in enumerate(ops_list):
    if oper == "+":
      list_of_answers.append(sum(nums_list[oper_index]))
    elif oper == "*":
      list_of_answers.append(math.prod(nums_list[oper_index]))

  sol2_sum = int(sum(list_of_answers))
  print(f"Solution 2: {sol2_sum}")
  return sol2_sum

def main():
  from pathlib import Path
  cwd = Path.from_uri(f"file://{__file__}").parent
  content = read.read_content(f"{cwd}/input")
  solution_1(content=content)
  solution_2(content=content)

if __name__ == "__main__":
  main()
