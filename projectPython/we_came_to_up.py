

def get_content_of_line(filepath: str, line_number: int):
    with open(filepath, "r") as file:
        lines = file.readlines()
        return lines[line_number]


if __name__ == '__main__':
    print(get_content_of_line("text.txt", 2))
