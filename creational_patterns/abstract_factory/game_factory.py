from abc import ABC, abstractmethod

# Abstract factory class
class GameFactory(ABC):
    @abstractmethod
    def create_graphics_renderer(self):
        pass

    @abstractmethod
    def create_sound_player(self):
        pass

    @abstractmethod
    def create_input_handler(self):
        pass

# Concrete factory for PC
class PCGameFactory(GameFactory):
    def create_graphics_renderer(self):
        return PCGraphicsRenderer()

    def create_sound_player(self):
        return PCSoundPlayer()

    def create_input_handler(self):
        return PCInputHandler()

# Concrete factory for Mobile
class MobileGameFactory(GameFactory):
    def create_graphics_renderer(self):
        return MobileGraphicsRenderer()

    def create_sound_player(self):
        return MobileSoundPlayer()

    def create_input_handler(self):
        return MobileInputHandler()

# Abstract product classes
class GraphicsRenderer(ABC):
    @abstractmethod
    def render(self):
        pass

class SoundPlayer(ABC):
    @abstractmethod
    def play_sound(self):
        pass

class InputHandler(ABC):
    @abstractmethod
    def handle_input(self):
        pass

# Concrete product classes for PC
class PCGraphicsRenderer(GraphicsRenderer):
    def render(self):
        print("Rendering using PC graphics")

class PCSoundPlayer(SoundPlayer):
    def play_sound(self):
        print("Playing sound on PC")

class PCInputHandler(InputHandler):
    def handle_input(self):
        print("Handling PC input")

# Concrete product classes for Mobile
class MobileGraphicsRenderer(GraphicsRenderer):
    def render(self):
        print("Rendering using Mobile graphics")

class MobileSoundPlayer(SoundPlayer):
    def play_sound(self):
        print("Playing sound on Mobile")

class MobileInputHandler(InputHandler):
    def handle_input(self):
        print("Handling Mobile input")

# Client code
def game_client(factory: GameFactory):
    renderer = factory.create_graphics_renderer()
    sound_player = factory.create_sound_player()
    input_handler = factory.create_input_handler()

    renderer.render()
    sound_player.play_sound()
    input_handler.handle_input()

# Usage example
pc_factory = PCGameFactory()
game_client(pc_factory)

mobile_factory = MobileGameFactory()
game_client(mobile_factory)
