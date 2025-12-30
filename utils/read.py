def read_content(file_name: str = "input",):
  content = []

  with open(file=file_name,mode="r", encoding="utf-8") as fp:
    content_read = fp.read()
    content = content_read.splitlines()

  return content
