import importlib
import typer
import glob

def main(day_no: str):
  globbed_dirs = glob.glob("day-*",)
  if f"day-{day_no}" in globbed_dirs:
    print(f"Executing the main.py in day-{day_no}")
    solution = importlib.import_module(f"day-{day_no}.main")
    solution.main()
  else:
    print(f"Day {day_no} does not exist, please create it.")

if __name__ == "__main__":
  typer.run(main)
