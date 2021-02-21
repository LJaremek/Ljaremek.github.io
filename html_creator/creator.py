from copy import deepcopy

def read_data(path):
    data = []
    with open(path, "r", encoding = "utf8") as file:
        for line in file:
            line = line.strip().split(";")
            data.append(line)
    return data


start = open("start.txt", encoding = "utf8").read()
left = open("left.txt", encoding = "utf8").read()
right = open("right.txt", encoding = "utf8").read()
end = open("end.txt", encoding = "utf8").read()
data = read_data("data.txt")

def make_html():
    file = open("index.html", "w+", encoding = "UTF8")
    print(start, file = file)
    left_side = True
    for line in data:
        if left_side:
            copy = deepcopy(left)
        else:
            copy = deepcopy(right)
        left_side = not left_side
        copy = copy.replace("TITLE", line[0], 2)
        copy = copy.replace("DESCRIPTION", line[1])
        copy = copy.replace("LINK", line[2], 1)
        copy = copy.replace("LINK_LOOK", line[3])
        copy = copy.replace("VIDEO", line[4])
        print(copy, file = file)
    print(end, file = file)
    file.close()

if __name__ == "__main__":
    make_html()
