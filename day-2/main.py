# this is the best answer i could come up with
# I was 1 short, because i was using python ranges and the ranges are end
# exclusive meaning if i start a range from 1 - 10 it will only return [1,2,3,4,5,6,7,8,9]
# and the last number of 1 of the ranges was something i needed to count
from pathlib import Path
from typing import List
import math


def read_content(file_name: str = "input"):
  content = []
  path = Path.from_uri(f"file://{__file__}").parent
  file_path = path / file_name

  with open(file=file_path,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content

# Pair matching method -> I asked gemini about how to find divisors
# but implemented it myself
def get_divisors(number: int) -> List[int]:
  divisors = set()
  sqrt = math.floor(math.sqrt(number))

  for i in range (1, sqrt + 1):
    if number % i == 0:
      divisors.add(i)
      divisors.add(number // i)

  # we dont want the number itself in the given problem
  divisors.discard(number)
  return list(divisors)

def is_invalid(number: str):
  if len(number) % 2 == 0:
    # can be invalid
    number_len_half = len(number) // 2
    if number[number_len_half:] == number[:number_len_half]:
      return True
  return False

def is_invalid_second(number: str, check_size: int):
  # my solution, this does not work, outputs very low
  possible_multiple = math.floor(len(number) / check_size)
  return number == number[0:0+check_size] * possible_multiple
  # solution found on github
  # mid = len(number) // 2
  # return any(number == number[:l] * (len(number) // l) for l in range(1, mid + 1))

def sol_1():
  # it only contains 1 line
  content = read_content()[0]
  all_ids = content.split(",")
  invalid_id_list = []

  for id_set in all_ids:
    id_range_min_max = [int(x) for x in id_set.split("-")]
    # print(f"trying: {id_range_min_max}")
    current_range_invalids = []
    for id in range(id_range_min_max[0], id_range_min_max[1]+1):
      if is_invalid(str(id)):
        current_range_invalids.append(id)
    invalid_id_list.extend(current_range_invalids)
    # print(f"Found: {current_range_invalids}")

  print(f"Total sum: {sum(invalid_id_list)}")


def sol_2():
  # it only contains 1 line
  content = read_content()[0]
  all_ids = content.split(",")
  invalid_id_list = []

  for id_set in all_ids:
    id_range_min_max = [int(x) for x in id_set.split("-")]
    # print(f"trying: {id_range_min_max}")
    current_range_invalids = []
    for id in range(id_range_min_max[0], id_range_min_max[1]+1):
      all_divisors = get_divisors(len(str(id)))
      is_invalid_list = [is_invalid_second(str(id), divisor) for divisor in all_divisors]
      if True in is_invalid_list:
        current_range_invalids.append(id)
    invalid_id_list.extend(current_range_invalids)
    # print(f"Found: {current_range_invalids}")

  print(f"Total sum: {sum(invalid_id_list)}")

def main():
  sol_1()
  sol_2()

if __name__ == "__main__":
  print("################ FIRST ##################")
  sol_1()
  print("################ SECOND ##################")
  sol_2()
  # print(get_divisors(12))
