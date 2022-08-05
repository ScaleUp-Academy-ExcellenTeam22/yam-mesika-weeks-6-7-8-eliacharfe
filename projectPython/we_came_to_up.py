

def get_content_of_line(filepath: str, line_number: int) -> str:
    """
    Get a path to a file and a line number and return the content of the line in the file.
    :param filepath: The path to the file.
    :param line_number: The line to read.
    :return: The line.
    """
    if line_number < 0:
        raise ValueError("Value error: The number of line should be positive")
    with open(filepath, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        return lines[line_number]


if __name__ == '__main__':
    try:
        print(get_content_of_line("text.txt", 2))
    except FileNotFoundError:
        print("FileNotFoundError: File path is incorrect")
    except OSError:
        print("OSError: The type of file path should be a string")
    except TypeError:
        print("TypeError: The file path should be a string and the line number variable should"
              " contains only integer")
    except UnicodeDecodeError:
        print("UnicodeDecodeError: The file is not textual")
    except IndexError:
        print("IndexError: Line number is out of range")
    except ValueError as e:
        print(str(e))


