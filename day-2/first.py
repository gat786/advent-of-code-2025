# this is the best answer i could come up with
# I was 1 short, because i was using python ranges and the ranges are end
# exclusive meaning if i start a range from 1 - 10 it will only return [1,2,3,4,5,6,7,8,9]
# and the last number of 1 of the ranges was something i needed to count
def read_content(file_name: str = "input"):
  content = []
  with open(file=file_name,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content

def is_invalid(number: str):
  if len(number) % 2 == 0:
    # can be invalid
    number_len_half = len(number) // 2
    if number[number_len_half:] == number[:number_len_half]:
      return True
  return False

def main():
  # it only contains 1 line
  content = read_content()[0]

  all_ids = content.split(",")

  invalid_id_list = []

  for id_set in all_ids:
    id_range_min_max = [int(x) for x in id_set.split("-")]
    print(f"trying: {id_range_min_max}")
    current_range_invalids = []
    for id in range(id_range_min_max[0], id_range_min_max[1]+1):
      if is_invalid(str(id)):
        current_range_invalids.append(id)
    invalid_id_list.extend(current_range_invalids)
    print(f"Found: {current_range_invalids}")

  print(f"Total sum: {sum(invalid_id_list)}")

if __name__ == "__main__":
  main()
