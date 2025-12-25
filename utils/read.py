def read_content(file_name: str = "input",):
  content = []

  with open(file=file_name,mode="r", encoding="utf-8") as fp:
    for line in fp:
      linecontent = line.strip()
      content.append(linecontent)

  return content
