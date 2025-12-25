from utils import read

def solution_1():
  from pathlib import Path
  cwd = Path.from_uri(f"file://{__file__}").parent
  content = read.read_content(f"{cwd}/input")
  print(content)
  # Your solution code here

def main():
  solution_1()

if __name__ == "__main__":
  main()
