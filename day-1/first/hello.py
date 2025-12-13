import operator
from token import MINUS

def read_content(file_name: str ="input.txt"):
  content = []
  with open(file=file_name,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content


def main():
  content = read_content()
  # print(content)
  starting_point = 50
  nozs = 0
  for line in content:
    operation = operator.sub if line[0] == "L" else operator.add
    number = int(line[1:], base = 10)
    operation_result = operation(starting_point, number) % 100
    # print(starting_point, number, operation_result, operation)
    starting_point = operation_result
    if starting_point == 0:
      nozs = nozs + 1

  print(nozs)


if __name__ == "__main__":
  main()
