from pathlib import Path
import operator
import json

# this is the best answer i could come up with
def read_content(file_name: str ="input.txt"):
  content = []
  path = Path.from_uri(f"file://{__file__}").parent
  file_path = path / file_name

  with open(file=file_path,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content

def turn_dial(
  starting_point: int,
  move: str
) -> tuple[int,int]:
  operation = operator.sub if move[0] == "L" else operator.add
  operate_by = int(move[1:], 10)
  operation_result = operation(starting_point, operate_by)
  number_complete_turns = 0
  # breakpoint()
  if (operation_result > 99 or operation_result < 0):
    number_complete_turns = abs(operation_result // 100)
    operation_result = operation_result % 100
    # breakpoint()

  return (operation_result, number_complete_turns)


def main():
  # content = read_content()
  content = read_content()
  # print(content)
  starting_point = 50
  nozs = 0
  for line in content:
    result, turns_taken = turn_dial(starting_point=starting_point, move=line)
    if result == 0:
      nozs = nozs + 1
    elif turns_taken != 0:
      nozs = nozs + turns_taken
      print(json.dumps({"sp": starting_point, "mv": line, "result":result, "tt": turns_taken}))
    starting_point = result

  print(nozs)


if __name__ == "__main__":
  main()
