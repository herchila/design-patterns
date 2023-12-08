class FileSystemEntity:
    def display(self):
        raise NotImplementedError


class File(FileSystemEntity):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")


class Directory(FileSystemEntity):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, entity):
        self.children.append(entity)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()


# Usage
# Create files
file1 = File("File1.txt")
file2 = File("File2.doc")

# Create a directory and add files to it
directory = Directory("MyDirectory")
directory.add(file1)
directory.add(file2)

# Create a subdirectory and add it to the directory
subdirectory = Directory("MySubdirectory")
directory.add(subdirectory)

# Display structure
directory.display()