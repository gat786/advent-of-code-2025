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
  list_of_line_items: List[List[str]] = [[] for _ in range(len(content[:-1]))]
  list_of_numbers: List[List[str]] = [[] for _ in range(len(content[0].split()))]
  list_of_operators: List[List] = [[] for _ in range(len(content[0].split()))]
  list_of_answers: List[float] = [0.0 for _ in range(len(content[0].split()))]
  for line_index, line in enumerate(content[:-1]):
    prev_char = None
    curr_char = None
    curr_number = ''
    list_items = []
    for char in line:
      curr_char = char

      if prev_char == ' ' and curr_char != " ":
        list_items.append(curr_number[:-1])
        curr_number = curr_char
      else:
        curr_number += curr_char

      prev_char = curr_char
    list_of_line_items[line_index] = list_items

  for line_index, line in enumerate(list_of_line_items):
    for line_item_index, line_item in enumerate(line):
      list_of_numbers[line_item_index].append(line_item)

  print(list_of_numbers)

    # items_in_line = line.split()
    # for item_index, item in enumerate(items_in_line):
    #   if item.isdigit():
    #     list_of_numbers[item_index].append(int(item))
  return 0
  for line_index, line in enumerate(content[-1:]):
    items_in_line = line.split()
    for item_index, item in enumerate(items_in_line):
      print(list_of_numbers[item_index])
      biggest_number = max(list_of_numbers[item_index])
      # no of digits in biggest number
      no_of_digits = len(str(biggest_number))
      # convert numbers to proper cephalopod format
      altered_list = []
      for i in range(no_of_digits):
        new_number = (''.join(str(x).ljust(no_of_digits, ' ')[i] for x in list_of_numbers[item_index])).strip()
        altered_list.append(int(new_number))
      print(altered_list)
      match item:
        case '+':
          sum_altered_list = math.fsum(altered_list)
          list_of_answers[item_index] = sum_altered_list
        case '*':
          product_altered_list = math.prod(altered_list)
          list_of_answers[item_index] = product_altered_list

  sol2_sum = int(sum(list_of_answers))
  print(f"Solution 2: {sol2_sum}")
  return sol2_sum

def main():
  from pathlib import Path
  cwd = Path.from_uri(f"file://{__file__}").parent
  content = read.read_content(f"{cwd}/input")
  solution_2(content=content)

if __name__ == "__main__":
  main()
