

class FileSystem:
    def __init__(self):
        pass


class File:
    def __init__(self, name):
        self.name = name


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

    def count(self, string: str):
        pass


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

    def __repr__(self):
        return f"directory: {[file for file in self.list_files]}"


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

    text_file = TextFile(1, "Some text content", user_normal, 'myTextFile')
    print(text_file)

    binary_file = BinaryFile(2, b"binary file", user_manager, 'myBinFile')
    print(binary_file)

    image_file = Image(8, b'image', User('Paul', "pswd123"), '.png', 'myImageFile')
    print(image_file)

    directory = Directory('myDir')
    directory.add_file(text_file)
    directory.add_file(binary_file)
    directory.add_file(image_file)
    print(directory)


