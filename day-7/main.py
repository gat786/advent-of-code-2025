from dataclasses import dataclass
from utils import read
from typing import List

start       = "S"
splitter    = "^"
ray         = "|"
passthrough = "."

@dataclass
class Coordinate:
  x: int
  y: int

def solution_1(content: List[str]):
  ray_uninitialised = True
  ray_map = {}
  for line_index, line in enumerate(content):
    for char_index, char in enumerate(line):
      if ray_uninitialised and char == start:
        print(f"Starting found at {line_index}:{char_index}")
        ray_uninitialised = False
        ray_map[line_index] = [char_index]

      if not ray_uninitialised:
        pre_line_ray_points = ray_map[line_index - 1]
        new_line = line
        if char_index in pre_line_ray_points:
          match(char):
            case ".":
              # change this point to ray
              new_line = line[:char_index] + "|" + line[char_index + 1:]
              ray_map[line_index].append(char_index)
            case "^":
              # change below two dots to left and right of this to rays
              pass





  return 0

def solution_2(content: List[str]):
  return 0

def main():
  from pathlib import Path
  cwd = Path.from_uri(f"file://{__file__}").parent
  content = read.read_content(f"{cwd}/input")
  solution_1(content=content)
  solution_2(content=content)

if __name__ == "__main__":
  main()
