class Image:
    def display(self): pass

class HighResolutionImage(Image):
    def display(self):
        print("Displaying high-resolution image")

class ImageProxy(Image):
    def __init__(self):
        self.image = None

    def display(self):
        if self.image is None:
            self.image = HighResolutionImage()
        self.image.display()

# Usage
proxy_image = ImageProxy()
proxy_image.display()  # Displaying high-resolution image
