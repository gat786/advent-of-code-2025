from typing import List

def read_content(file_name: str = "input"):
  content = []
  with open(file=file_name,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content

def top_two(num_str: str) -> List:
  previous_items = set()
  all_combinations = set()
  # top = { "value": -1, "position": -1}
  # second_top = { "value": -1, "position": -1}

  # for key, num in enumerate(num_str):
  #   num_value = int(num)
  #   if num_value > top["value"]:
  #     second_top = top
  #     top = { "value": num_value, "position": key }
  #   elif num_value > second_top["value"]:
  #     second_top = { "value": num_value, "position": key }

  for num in num_str:
    for prev_element in previous_items:
      combination = int(f"{prev_element}{num}")
      all_combinations.add(int(combination))
    previous_items.add(num)

  return all_combinations

def main():
  content = read_content()

  maxs = []
  for line in content:
    combinations = top_two(line)
    maxs.append(max(combinations))

  print(sum(maxs))
    # big_num = int(f"{first}{second}")
    # total_sum += big_num

  # print(total_sum)

if __name__ == "__main__":
  main()
