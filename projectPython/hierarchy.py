from typing import List, Text


class FileSystem:
    def __init__(self):
        self.list_file = []
        self.list_file.append(Directory('/'))

    def listdir(self, path) -> List[Text]:
        for my_dir in self.list_file:
            if my_dir.name == path:
                return [file.name for file in my_dir.list_files]
        return []

    def makedir(self, path):
        for my_dir in self.list_file:
            if my_dir.name == path:
                return
        self.list_file.append(Directory(path))

    def create(self, path, file_name='Empty File') -> bool:
        new_file = File(file_name)
        for my_dir in self.list_file:
            if my_dir.name == path and not my_dir.exist(file_name):
                my_dir.add_file(new_file)
                return True
        return False


class File:
    def __init__(self, name='Empty File'):
        self.closed = False
        self.name = name

    def __enter__(self):
        """For context manager."""
        return self

    def __exit__(self,) -> None:
        """Close the file."""
        self.close()

    def close(self) -> None:
        self.closed = True


class SingleFile(File):
    def __init__(self, weight, content, owner, name):
        super().__init__(name)
        self.weight = weight
        self.content = content
        self.owner = owner

    def read(self, user):
        return self.content if user == self.owner or user.manager else None

    def __repr__(self):
        return f"filename: '{self.name}', weight: {self.weight}, content: '{self.content}', owner: {self.owner}."


class TextFile(SingleFile):
    def __init__(self, weight, content, owner, name='Empty File'):
        super().__init__(weight, content, owner, name + '.txt')

    def count(self, string: str) -> int:
        return self.content.count(string)


class BinaryFile(SingleFile):
    def __init__(self, weight, content, owner, name='Empty File'):
        super().__init__(weight, content, owner, name)


class Image(BinaryFile):
    def __init__(self, weight, content, owner, extension='.jpg', name='Empty File'):
        super().__init__(weight, content, owner, name + extension)
        self.extension = extension

    def get_dimensions(self):
        pass


class Directory(File):
    def __init__(self, name='Empty Directory'):
        super().__init__(name)
        self.list_files = []

    def add_file(self, file):
        self.list_files.append(file)

    def exist(self, filename):
        for file in self.list_files:
            if file.name == filename:
                return True
        return False

    def __repr__(self):
        return f"directory: /{self.name}: {[file for file in self.list_files]}"


class User:
    def __init__(self, username, password, manager=False):
        self.username = username
        self.password = password
        self.manager = manager

    def __str__(self):
        return f"(username: {self.username}, password: {self.password}, manager: {self.manager})"


if __name__ == '__main__':
    user_normal = User('Bob', '12345678')
    user_manager = User('Jhon', '12341234@#', True)
    print(user_normal)
    print(user_manager)

    text_file = TextFile(1, "Some text content, with text in it", user_normal, 'myTextFile')
    print(text_file)

    print("read text file: " + text_file.read(user_normal))
    print("text file count ('text'): " + str(text_file.count('text')))

    binary_file = BinaryFile(2, b"binary file", user_manager, 'myBinFile')
    print(binary_file)

    image_file = Image(8, b'image', User('Paul', "pswd123"), '.png', 'myImageFile')
    print(image_file)

    directory = Directory('myDir')
    directory.add_file(text_file)
    directory.add_file(binary_file)
    directory.add_file(image_file)

    inner_dir = Directory('Dirname')
    inner_dir.add_file(TextFile(3, "text file text", user_manager, 'Txt file of manager'))
    directory.add_file(inner_dir)

    print(directory)

    file_system = FileSystem()

    file_system.makedir('pathDir')

    file_system.create('pathDir')
    file_system.create('pathDir', 'text.txt')

    for name_file in file_system.listdir('pathDir'):
        print(name_file)





