from typing import List

def read_content(file_name: str = "input"):
  content = []
  with open(file=file_name,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content

def all_12_digit_combination(num_str: str) -> List:
  all_combos = []
  for num_index, num in enumerate(num_str[:-11]):
    current_combination = [num]
    current_charachter_index = num_index
    while len(current_combination) < 12:
      leave_remaining = (11 - len(current_combination))
      remaining_slice = num_str[current_charachter_index+1:(-leave_remaining) if leave_remaining != 0 else None]
      next_num = max(remaining_slice)
      current_combination.append(next_num)
      current_charachter_index = current_charachter_index + (remaining_slice.index(next_num) + 1)

    all_combos.append(int("".join(current_combination)))
  return all_combos

def all_twos_combinations(num_str: str) -> List:
  previous_items = set()
  all_combinations = set()

  for num in num_str:
    for prev_element in previous_items:
      combination = int(f"{prev_element}{num}")
      all_combinations.add(int(combination))
    previous_items.add(num)

  return all_combinations

def main():
  content = read_content()

  ################### PART 1 Solution ###########################
  # maxs = []
  # for line in content:
  #   combinations = all_twos_combinations(line)
  #   maxs.append(max(combinations))

  # print(sum(maxs))

  ################### PART 2 Solution ###########################
  maxs = []
  for line in content:
    all_combo = all_12_digit_combination(line)
    max_value = max(all_combo)
    maxs.append(max_value)
  total = sum(maxs)
  print(total)


if __name__ == "__main__":
  main()
