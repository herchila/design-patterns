class Button:
    def paint(self): pass

class LinuxButton(Button):
    def paint(self):
        return "Render a button in a Linux style"

class WindowsButton(Button):
    def paint(self):
        return "Render a button in a Windows style"

class GUIFactory:
    def create_button(self): pass

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

# Usage
def client_code(factory: GUIFactory):
    button = factory.create_button()
    print(button.paint())

client_code(LinuxFactory())  # Output: Render a button in a Linux style
client_code(WindowsFactory())  # Output: Render a button in a Windows style
