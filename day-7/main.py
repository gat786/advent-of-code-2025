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
  solved_matrix = current_matrix = [list(x) for x in content]

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
