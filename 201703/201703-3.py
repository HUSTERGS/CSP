# score 100

from sys import stdin
import re

list_store = []
paragraph_store = []


def handle_inner(line):
    # Text
    line = re.sub(r"_(.+?)_", r"<em>\1</em>", line)
    line = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', line)
    return line


def generate_list():
    global list_store
    temp = "<ul>\n"
    for line in list_store:
        temp += f"<li>{handle_inner(line)}</li>\n"
    list_store = []
    temp += "</ul>"
    print(temp)


def generate_para():
    global paragraph_store
    print("<p>", end="")
    for line in paragraph_store[:-1]:
        print(handle_inner(line))
    print(f"{handle_inner(paragraph_store[-1])}</p>")
    paragraph_store = []


while True:
    line = stdin.readline()
    if not line:
        if len(list_store):
            generate_list()
        if len(paragraph_store):
            generate_para()
        break
    line = line.strip()
    if line == "":
        if len(list_store):
            generate_list()
        if len(paragraph_store):
            generate_para()
        continue
    # 分级
    if re.match(r"#+ .+", line):
        inner = re.findall(r"#+ (.+)", line)[0]
        for i in range(6, 0, -1):
            if line.startswith("#" * i):
                print(f"<h{i}>{handle_inner(inner)}</h{i}>")
                break
    elif re.match(r"\* .+", line):
        list_store.append(re.findall(r"\* (.+)", line)[0])
    else:
        paragraph_store.append(line)
