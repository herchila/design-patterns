class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

# Usage
s = Singleton.getInstance()
print(s)

s1 = Singleton.getInstance()
print(s1)  # Will print the same instance as s
