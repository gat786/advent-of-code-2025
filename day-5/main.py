from typing import List

def read_content(file_name: str = "input"):
  content = []
  from pathlib import Path
  path = Path.from_uri(f"file://{__file__}").parent
  file_path = path / file_name

  with open(file=file_path,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content

def is_fresh_check(number: int, ranges: List[str]) -> bool:
  for range_str in ranges:
    start, end = map(int, range_str.split("-"))
    if start <= number <= end:
      return True
  return False

def solution_1() -> int:
  content = read_content()
  ranges: List[str] = []
  ranges_end = False
  numbers = []
  is_fresh_count = 0
  for line in content:
    if line != "" and not ranges_end:
      ranges.append(line)
    elif line == "":
      ranges_end = True
    else:
      numbers.append(line)
      if is_fresh_check(int(line), ranges):
        is_fresh_count += 1
  print(f"{'#' * 25 } Solution 1 {'#' * 25}")
  print(is_fresh_count)
  return is_fresh_count

def solution_2() -> None:
  print(f"{'#' * 25 } Solution 2 {'#' * 25}")
  content = read_content()
  ranges: List[str] = []

  valid_ids = {}

  for line in content:
    if line != "":
      ranges.append(line)
    elif line == "":
      break;


  consolidated_ranges = []
  for range_index,range_str in enumerate(ranges):
    start, end = map(int, range_str.split("-"))

    if len(consolidated_ranges) == 0:
      consolidated_ranges.append((start, end))
      continue

    was_consolidated = False
    for c_range in consolidated_ranges:
      # check if it is overlapping
      if max(start, c_range[0]) <= min(end, c_range[1]):
        consolidated_ranges.remove(c_range)
        consolidated_ranges.append((min(start, c_range[0]), max(end, c_range[1])))
        was_consolidated = True
        break

    if not was_consolidated:
      consolidated_ranges.append((start, end))

  # valid_ids_count= len(valid_ids.keys())
  # print(consolidated_ranges)
  # print(len(consolidated_ranges))
  total_sum = 0
  for range in consolidated_ranges:
    # range[1] is end
    # range[0] is start
    total_sum += (range[1] - range[0]) + 1
  print(total_sum)
  # print(valid_ids_count)
  # return valid_ids_count

def main():
  solution_1()
  solution_2()

if __name__ == "__main__":
  main()

# My answer -> 355755429546761
# The answer that is received from github -> 350513176552950
